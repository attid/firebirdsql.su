#!/usr/bin/env python3
"""Генерирует карту 301-редиректов со старых URL DokuWiki на новые страницы.

Вход: legacy/pages.json (полный список старых ID) + legacy/raw (для поиска
«родителя» include-сниппетов и системных страниц).

Выход (пересоздаётся целиком, руками не править — см. AGENTS.md):
  deploy/redirects.map       — nginx map $arg_id -> новый путь;
  deploy/nginx-redirects.conf — фрагмент server{}: редирект /doku.php?id=...
                                и path-формы /<page_id> (обе старые формы).

Схема соответствия честная 1:1: старый ID -> /<id>/ (ADR-0004).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "legacy" / "raw"
DEPLOY = ROOT / "deploy"

# Страницы, не ставшие страницами нового сайта (сниппеты include-плагина,
# системная навигация). Их старые URL уводим на «родителя»/главную.
SKIP_IDS = {"operator", "datetype", "array_dim", "dom_search_condition", "sidebar"}


def includer_top(snippet: str, ids: list[str]) -> str:
    """Верхний «родитель» сниппета по цепочке {{page>...}}:
    поднимаемся, пока не встретим обычную страницу."""
    current, seen = snippet, set()
    while True:
        parent = None
        for pid in ids:
            if pid in seen or pid == current:
                continue
            f = RAW / f"{pid}.txt"
            if f.is_file() and re.search(rf"\{{{{page>{current}}}}}", f.read_text("utf-8")):
                parent = pid
                break
        if parent is None:
            return ""
        if parent not in SKIP_IDS:
            return parent
        if parent in seen:
            return ""
        seen.add(parent)
        current = parent


def main() -> int:
    reg = json.loads((ROOT / "legacy" / "pages.json").read_text("utf-8"))
    ids = [p["id"] for p in reg["pages"]]

    entries: list[tuple[str, str]] = []
    for pid in ids:
        if pid in SKIP_IDS:
            top = includer_top(pid, ids)
            target = f"/{top}/" if top else "/"
        else:
            target = f"/{pid}/"
        entries.append((pid, target))

    entries.sort()
    map_lines = ["# Сгенерировано tools/make_redirect_map.py. Не редактировать руками.",
                 "# Только записи; обёртка map{} и default — в deploy/nginx.conf."]
    for pid, target in entries:
        map_lines.append(f"    {pid} {target};")
    DEPLOY.mkdir(exist_ok=True)
    (DEPLOY / "redirects.map").write_text("\n".join(map_lines) + "\n", "utf-8")

    conf = """# Сгенерировано tools/make_redirect_map.py. Не редактировать руками.
# Обе старые формы URL уходят 301 на новые страницы (docs/seo-migration.md).
# Рабочий вариант конфигурации — deploy/nginx.conf; этот файл — краткая шпаргалка.

server {
    # map $arg_id -> путь: см. nginx.conf (обёртка) + redirects.map (записи)

    # Форма 1: /doku.php?id=<page_id> (основная форма старых внутренних ссылок)
    location = /doku.php {
        return 301 $fb_new_path;
    }

    # Форма 2: /<page_id> без doku.php (например /abs, /sql003.summa_propisju)
    location ~ ^/(?:[a-z0-9_.\\-]+:)?(?<fb_path_id>[a-z0-9_.\\-]+)$ {
        return 301 /$fb_path_id/;
    }
}
"""
    (DEPLOY / "nginx-redirects.conf").write_text(conf, "utf-8")

    skipped = [(pid, t) for pid, t in entries if pid in SKIP_IDS]
    print(f"Карта: {len(entries)} записей -> {DEPLOY/'redirects.map'}")
    print(f"Особые (сниппеты/системные): {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
