#!/usr/bin/env python3
"""Проверка чистоты конвертации: ищет остатки вики-синтаксиса DokuWiki
в Markdown-выходе ВНЕ код-блоков (``` ... ```).

Выход: сводка по паттернам + до трёх примеров на каждый (файл:строка).
Код возврата: 0 если чисто, 1 если есть остатки.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "site" / "src" / "content" / "docs"

PATTERNS = {
    "wiki-link [[": r"\[\[",
    "include {{": r"\{\{",
    "code tag <code/<file": r"</?(code|file)[ >]",
    "noformat %%": r"%%",
    "smiley :!:": r":!:",
    "raw heading =": r"^={3,}",
    "table row ^": r"^\^",
    "footnote ((": r"\(\(",
    "mono ''": r"''.+?''",
    "NOTOC/~~": r"~~",
    "double backslash \\\\": r"\\\\$",
    "underline __x__": r"__[^\s_][^_\n]*?__",
}

# Задокументированные «честные» остатки — артефакты исходного контента,
# которые старая вика тоже рендерила буквально (чинятся в этапе 4, гигиена).
# indices_maintenance: двухстрочная незакрытая ссылка на Google Groups.
KNOWN_FAITHFUL = [
    ("indices_maintenance.md", "groups.google.com"),
]


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def main() -> int:
    total_hits = 0
    for name, pat in PATTERNS.items():
        rx = re.compile(pat, re.M)
        hits = []
        for f in sorted(DOCS.glob("*.md")):
            for i, ln in enumerate(strip_fences(f.read_text("utf-8")).split("\n"), 1):
                if rx.search(ln):
                    if any(f.name == fn and marker in ln for fn, marker in KNOWN_FAITHFUL):
                        continue
                    hits.append(f"{f.name}:{i}: {ln.strip()[:80]}")
        if hits:
            total_hits += len(hits)
            print(f"{name}: {len(hits)}")
            for h in hits[:3]:
                print(f"    {h}")
        else:
            print(f"{name}: 0")
    print(("ЧИСТО" if total_hits == 0 else f"ОСТАТКОВ: {total_hits}"))
    return 0 if total_hits == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
