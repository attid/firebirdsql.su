#!/usr/bin/env python3
"""Сверка URL из выгрузки Метрики с покрытием миграции.

Для каждого URL входа (CSV выгрузка «Страницы входа») определяет:
  - покрыт картой редиректов / совпадает со страницей нового сайта;
  - или НЕ покрыт (дыра — теряем трафик после переключения).

Классификация старых форм:
  /doku.php?id=<page_id>  -> id должен быть в redirects.map;
  /<page_id>[/:...]       -> path-форма, тоже должна решаться;
  прочее (/lib/, /feed.php, ?do=...) -> служебное, проверяем вручную.

Использование:
  python3 tools/check_traffic_urls.py docs/metrics-baseline/metrika_entry_urls.csv
Выход: сводка в stdout + markdown-отчёт рядом с CSV (coverage_report.md).
"""

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parent.parent


def load_redirects() -> dict[str, str]:
    text = (ROOT / "deploy" / "redirects.map").read_text("utf-8")
    return dict(re.findall(r"^    ([a-z0-9_.:\-]+) (\S+);$", text, re.M))


def classify(url: str, redirects: dict[str, str], pages: set[str]) -> tuple[str, str]:
    """(категория, пояснение). Категории: ok_new, ok_redirect, soft404, HOLE.

    soft404 — URL, контента по которому не было И НА СТАРОЙ вики (красные
    ссылки, вики-механика do=...): nginx уводит их default-ом на главную
    (или честный 404 в path-форме). Это не потеря, старый сайт там тоже
    показывал «страница не существует»."""
    parts = urlsplit(url)
    path, query = parts.path, parts.query

    if path == "/" and not query:
        return "ok_new", "главная нового сайта"

    # старая форма /doku.php?id=... (в т.ч. с do=-параметрами поверх)
    if path == "/doku.php":
        pid = (parse_qs(query).get("id") or [""])[0].lower()
        if pid in redirects:
            return "ok_redirect", f"id={pid} -> {redirects[pid]}"
        if ":" in pid:  # ns:-префикс из кэша поиска: срезается nginx-регексом
            tail = pid.split(":")[-1]
            if tail in pages or tail in redirects:
                return "ok_redirect", f"id={pid} -> /{tail}/ (срез ns:)"
        if pid in pages:
            return "ok_redirect", f"id={pid} -> /{pid}/"
        return "soft404", f"id={pid or '—'} не существовал и на старой вики -> default /"

    # новая страница
    if path in pages or path.rstrip("/") in pages:
        return "ok_new", "страница нового сайта"

    # path-форма вики /<page_id>
    m = re.match(r"^/([a-z0-9_.\-]+?)/?$", path, re.I)
    if m:
        pid = m.group(1).lower()
        if pid in redirects:
            return "ok_redirect", f"path-форма -> {redirects[pid]}"
        if pid in pages:
            return "ok_redirect", f"path-форма -> /{pid}/"
        return "soft404", f"/{pid} не существовал и на старой вики -> 404"

    # служебное старой вики
    if path.startswith(("/lib/", "/_detail", "/_media", "/feed.php", "/index.php")):
        return "soft404", "служебный URL старой вики"

    return "HOLE", f"неизвестный путь {path}" + (f"?{query[:60]}" if query else "")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    csv_path = Path(sys.argv[1]).resolve()
    redirects = load_redirects()
    reg = json.loads((ROOT / "legacy" / "pages.json").read_text("utf-8"))
    pages = {p["id"] for p in reg["pages"]}

    rows = []
    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for r in reader:
            url, visits = r.get("Страница входа", ""), r.get("Визиты", "0")
            if not url or url == "Итого и средние" or not visits.isdigit():
                continue
            rows.append((url, int(visits)))

    by_cat: dict[str, int] = {}
    holes: list[tuple[str, int, str]] = []
    softs: list[tuple[str, int, str]] = []
    for url, visits in rows:
        cat, note = classify(url, redirects, pages)
        by_cat[cat] = by_cat.get(cat, 0) + visits
        if cat == "HOLE":
            holes.append((url, visits, note))
        if cat == "soft404":
            softs.append((url, visits, note))

    total = sum(by_cat.values())
    lines = [
        "# Покрытие URL-трафика Метрики картой редиректов",
        "",
        f"Источник: `{csv_path.name}`; строк с URL: {len(rows)}; визитов: {total}.",
        "",
        "| Категория | Визиты | Доля |",
        "|---|---|---|",
    ]
    for cat in ("ok_redirect", "ok_new", "soft404", "HOLE"):
        v = by_cat.get(cat, 0)
        lines.append(f"| {cat} | {v} | {v/total*100:.2f}% |")
    lines += ["",
              "soft404 — контента не было и на старой вики (красные ссылки,",
              "вики-механика do=...): уходят default-ом на главную, потерей не являются.",
              "",
              f"## Дыры (HOLE) — {len(holes)} URL, {by_cat.get('HOLE', 0)} визитов", ""]
    for url, visits, note in sorted(holes, key=lambda x: -x[1])[:50]:
        lines.append(f"- {visits} визитов: `{url}` — {note}")
    lines += ["", f"## soft404 — {len(softs)} URL, топ по визитам", ""]
    for url, visits, note in sorted(softs, key=lambda x: -x[1])[:15]:
        lines.append(f"- {visits} визитов: `{url}`")

    report = csv_path.parent / "coverage_report.md"
    report.write_text("\n".join(lines) + "\n", "utf-8")

    print(f"URL: {len(rows)}, визитов: {total}")
    for cat, v in sorted(by_cat.items()):
        print(f"  {cat:12} {v:6} ({v/total*100:.2f}%)")
    print(f"Отчёт: {report}")
    return 0 if by_cat.get("HOLE", 0) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
