#!/usr/bin/env python3
"""Проверка и выгрузка данных из Google Analytics 4 и Search Console.

Ключ сервис-аккаунта: ga4-sa.json в корне (gitignored).
Скрипт: подписывает JWT через openssl, получает access token, находит
GA4-свойство и сайт GSC автоматически, делает пробные отчёты.

Использование: python3 tools/ga_pull.py [--days 14]
"""

import base64
import json
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEY_FILE = ROOT / "ga4-sa.json"
SCOPES = ("https://www.googleapis.com/auth/analytics.readonly "
          "https://www.googleapis.com/auth/webmasters.readonly")


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def access_token(key: dict) -> str:
    now = int(time.time())
    header = b64url(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    payload = b64url(json.dumps({
        "iss": key["client_email"],
        "scope": SCOPES,
        "aud": "https://oauth2.googleapis.com/token",
        "exp": now + 3600,
        "iat": now,
    }).encode())

    # приватный ключ из JSON -> временный PEM для openssl
    with tempfile.NamedTemporaryFile("w", suffix=".pem", delete=False) as pem:
        pem.write(key["private_key"])
        pem_path = pem.name
    signing_input = f"{header}.{payload}".encode()
    sig = subprocess.run(
        ["openssl", "dgst", "-sha256", "-sign", pem_path],
        input=signing_input, capture_output=True, check=True,
    ).stdout
    Path(pem_path).unlink()
    jwt = f"{header}.{payload}.{b64url(sig)}"

    body = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt,
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["access_token"]


def api_get(token: str, url: str) -> dict:
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def api_post(token: str, url: str, payload: dict) -> dict:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Bearer {token}",
                 "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main() -> int:
    days = "14"
    if "--days" in sys.argv:
        days = sys.argv[sys.argv.index("--days") + 1]

    key = json.loads(KEY_FILE.read_text("utf-8"))
    tok = access_token(key)
    print(f"access token OK ({key['client_email']})")

    # --- GA4: находим свойство ---
    summaries = api_get(tok, "https://analyticsadmin.googleapis.com/v1beta/accountSummaries")
    props = [(s["displayName"], p["property"], p["displayName"])
             for s in summaries.get("accountSummaries", [])
             for p in s.get("propertySummaries", [])]
    if not props:
        sys.exit("GA4: сервис-аккаунт не видит ни одного свойства — "
                 "добавь его email как Viewer в Администратор → Управление доступом")
    prop_id, prop_name = None, None
    for _, pid, pname in props:
        if "firebird" in pname.lower() or "firebird" in _ .lower():
            prop_id, prop_name = pid.split("/")[-1], pname
            break
    if not prop_id:
        prop_id, prop_name = props[0][1].split("/")[-1], props[0][2]
    print(f"GA4 свойство: {prop_name} (id {prop_id})")

    report = api_post(
        tok,
        f"https://analyticsdata.googleapis.com/v1beta/properties/{prop_id}:runReport",
        {"dateRanges": [{"startDate": f"{days}daysAgo", "endDate": "today"}],
         "metrics": [{"name": "sessions"}, {"name": "screenPageViews"}],
         "dimensions": [{"name": "date"}],
         "orderBys": [{"dimension": {"dimensionName": "date"}}]},
    )
    print("GA4, сессии/просмотры по дням (последние дни):")
    for row in report.get("rows", [])[-7:]:
        print(f"  {row['dimensionValues'][0]['value']}: "
              f"{row['metricValues'][0]['value']} сессий, "
              f"{row['metricValues'][1]['value']} просмотров")

    # --- Search Console ---
    sites = api_get(tok, "https://www.googleapis.com/webmasters/v3/sites")
    mine = [s for s in sites.get("siteEntry", [])
            if "firebirdsql.su" in s.get("siteUrl", "")]
    if not mine:
        sys.exit("GSC: сайт не найден — добавь сервис-аккаунт в "
                 "Настройки → Пользователи и разрешения (право «Чтение»)")
    site_url = mine[0]["siteUrl"]
    print(f"GSC сайт: {site_url}")

    import datetime
    query = api_post(
        tok,
        "https://www.googleapis.com/webmasters/v3/sites/"
        + urllib.parse.quote(site_url, safe="") + "/searchAnalytics/query",
        {"startDate": (datetime.date.today()
                       - datetime.timedelta(days=int(days))).isoformat(),
         "endDate": datetime.date.today().isoformat(),
         "dimensions": ["date"],
         "rowLimit": 100},
    )
    print("GSC, клики/показы по дням (последние дни):")
    for row in query.get("rows", [])[-7:]:
        print(f"  {row['keys'][0]}: {row['clicks']} кликов, {row['impressions']} показов")

    return 0


if __name__ == "__main__":
    sys.exit(main())
