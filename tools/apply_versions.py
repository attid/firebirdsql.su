#!/usr/bin/env python3
"""Вносит вычисленные версии (firebird.since) в frontmatter страниц.

Правила (docs/article-workflow.md, честность данных):
  - since = самый ранний ДОКАЗАННЫЙ номер версии:
    min(таблица «Версии сервера» в теле страницы, первое присутствие в LR 2.5-6.0);
  - страницам без доказательств (нет ни таблицы, ни вхождения в LR) флаг
    НЕ ставится — они попадают в tools/versions_review.md на ручной разбор;
  - until/deprecated автоматически не трогаем: отсутствие в LR != удалено.

Запуск: python3 tools/apply_versions.py [--dry]
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "site" / "src" / "content" / "docs"
VERSIONS = ["2.5", "3.0", "4.0", "5.0", "6.0"]


def vkey(v: str):
    return [int(p) for p in v.split(".")]


def main() -> int:
    dry = "--dry" in sys.argv
    data = json.loads((ROOT / "tools" / "version_matrix.json").read_text("utf-8"))
    matrix = data["matrix"]
    wiki_tables = data.get("wiki_tables", {})

    changed, skipped, review = [], [], []
    for f in sorted(DOCS.glob("*.md")):
        pid = f.stem
        rec = matrix.get(pid)
        text = f.read_text("utf-8")

        m_since = re.search(r"^  since:\s*(\"[^\"]*\")?\s*$", text, re.M)
        if not m_since:
            continue  # не наш формат frontmatter — не трогаем
        already = m_since.group(1)
        if already:
            continue  # уже заполнено — не перетираем

        since = None
        reasons = []
        if rec:
            present = [v for v in VERSIONS if rec["in"][v]]
            if present:
                since, reasons = present[0], ["LR"]
        wiki = wiki_tables.get(pid) or (rec or {}).get("wiki_versions") or []
        if wiki:
            w = min(wiki, key=vkey)
            if since is None or vkey(w) < vkey(since):
                since, reasons = w, ["wiki-таблица"]

        if since is None:
            review.append(pid)
            continue

        new_text = re.sub(
            r"^  since:\s*(\"[^\"]*\")?\s*$", f'  since: "{since}"', text,
            count=1, flags=re.M)
        if new_text != text:
            if not dry:
                f.write_text(new_text, "utf-8")
            changed.append((pid, since, "+".join(reasons)))

    (ROOT / "tools" / "versions_review.md").write_text(
        "# Ручной разбор: страницы без доказательств версии\n\n"
        "Ни таблицы «Версии сервера» в теле, ни вхождения в LR 2.5–6.0.\n\n"
        + "\n".join(f"- `{p}`" for p in sorted(review)) + "\n", "utf-8")

    print(f"{'DRY: ' if dry else ''}записан since: {len(changed)}; "
          f"на ручной разбор: {len(review)}")
    for pid, since, why in changed[:12]:
        print(f"  {pid}: since={since} ({why})")
    if len(changed) > 12:
        print(f"  … ещё {len(changed) - 12}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
