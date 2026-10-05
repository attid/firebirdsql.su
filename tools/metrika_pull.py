#!/usr/bin/env python3
"""Выгрузка «Страницы входа» из API Яндекс.Метрики.

Токен читается из .env в корне репо (YANDEX_OAUTH_TOKEN), файл gitignored.
Выход — CSV в том же формате, что и ручная выгрузка интерфейса, поэтому
прямого скармливается tools/check_traffic_urls.py.

Использование:
  python3 tools/metrika_pull.py --from 2026-09-26 --to 2026-10-04 \
      [--counter 25113035] [--out docs/metrics-baseline/metrika_entry.csv]
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://api-metrika.yandex.net/stat/v1/data"


def load_token() -> str:
    env = ROOT / ".env"
    for line in env.read_text("utf-8").splitlines():
        if line.startswith("YANDEX_OAUTH_TOKEN="):
            return line.split("=", 1)[1].strip()
    sys.exit("Нет YANDEX_OAUTH_TOKEN в .env (корень репо)")


def fetch(token: str, params: dict) -> dict:
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"OAuth {token}"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if attempt == 2:
                raise
            print(f"  повтор ({e})", file=sys.stderr)
            time.sleep(3)
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="date_from", required=True)
    ap.add_argument("--to", dest="date_to", required=True)
    ap.add_argument("--counter", default="25113035")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    token = load_token()
    rows, offset, limit = [], 1, 1000
    while True:
        params = {
            "id": args.counter,
            "metrics": "ym:s:visits",
            "dimensions": "ym:s:startURL",
            "date1": args.date_from,
            "date2": args.date_to,
            "sort": "-ym:s:visits",
            "limit": limit,
            "offset": offset,
        }
        d = fetch(token, params)
        data = d.get("data", [])
        for row in data:
            url = row["dimensions"][0]["name"]
            visits = int(row["metrics"][0])
            if visits > 0:
                rows.append((url, visits))
        print(f"  получено {len(data)} строк (offset {offset})")
        if len(data) < limit:
            break
        offset += limit

    out = Path(args.out) if args.out else \
        ROOT / "docs" / "metrics-baseline" / f"metrika_entry_{args.date_from}_{args.date_to}.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Страница входа", "Визиты"])
        w.writerows(rows)

    total = sum(v for _, v in rows)
    print(f"Готово: {len(rows)} URL, {total} визитов -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
