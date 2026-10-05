#!/usr/bin/env python3
"""Снимок статуса Яндекс.Вебмастера для firebirdsql.su (ИКС, страницы в
поиске, исключённые, проблемы).

Токен: .env → YANDEX_OAUTH_TOKEN (нужны скоупы webmaster:hostinfo +
webmaster:verify). Снимок дописывается в
docs/metrics-baseline/webmaster_snapshots.jsonl (локально, не в гит).

Использование: python3 tools/webmaster_pull.py
"""

import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER_ID = "613921"          # из GET /v4/user
HOST_ID = "https:firebirdsql.su:443"
OUT = ROOT / "docs" / "metrics-baseline" / "webmaster_snapshots.jsonl"


def load_token() -> str:
    for line in (ROOT / ".env").read_text("utf-8").splitlines():
        if line.startswith("YANDEX_OAUTH_TOKEN="):
            return line.split("=", 1)[1].strip()
    sys.exit("Нет YANDEX_OAUTH_TOKEN в .env")


def get(token: str, path: str) -> dict:
    req = urllib.request.Request(
        f"https://api.webmaster.yandex.net/v4/user/{USER_ID}/hosts/{HOST_ID}{path}",
        headers={"Authorization": f"OAuth {token}"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main() -> int:
    token = load_token()
    summary = get(token, "/summary")
    snapshot = {
        "date": datetime.date.today().isoformat(),
        "sqi": summary.get("sqi"),
        "searchable_pages": summary.get("searchable_pages_count"),
        "excluded_pages": summary.get("excluded_pages_count"),
        "problems": summary.get("site_problems"),
    }
    with open(OUT, "a", encoding="utf-8") as f:
        f.write(json.dumps(snapshot, ensure_ascii=False) + "\n")
    print(json.dumps(snapshot, ensure_ascii=False, indent=1))
    print(f"-> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
