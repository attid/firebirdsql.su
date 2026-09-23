#!/usr/bin/env python3
"""Проверка СОБРАННОГО сайта: сырой синтаксис не должен попадать в вывод.

В отличие от check_conversion.py (проверяет исходники Markdown), этот скрипт
сканирует готовые HTML в site/dist — то, что реально видит пользователь.

Ищем в видимом тексте страниц (теги и скрипты вырезаны, сущности декодированы):
  ```        — не закрытый/утёкший fence
  ===        — wiki-заголовок
  **         — markdown-жирность
  |---|      — разделитель markdown-таблицы
  [[ ]]      — wiki-ссылка
  {{         — include-плагин
  %%         — wiki-экранирование
  <br>       — тег как текст
  \\x00      — плейсхолдеры конвертера (NUL-байты)
  \\x00CODE/NOFMT/INC — то же, словом

Код-блоки (содержимое <pre>) проверяются так же: сырой синтаксис там
тоже был бы артефактом конвертации.

Выход: сводка + контекст каждого совпадения. Код возврата 1, если что-то найдено.
"""

import html as htmllib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "site" / "dist"

PATTERNS = {
    "fence ```": "```",
    "wiki heading ===": "===",
    "md bold **": "**",
    "md table |---": "|---",
    "wiki link [[": "[[",
    "include {{": "{{",
    "noformat %%": "%%",
    "<br> as text": "<br>",
    "NUL placeholder": "\x00",
}

# Легитимные вхождения, не являющиеся утечками конвертера:
# [[:…]]  — POSIX-классы в SQL (SIMILAR TO '[[:DIGIT:]]');
# %%i/%%~ — переменные батников Windows в примерах кода;
# ****    — маска пароля в примерах вывода утилит;
# ============  — псевдографика в выводе isql внутри примеров;
# groups.google.com — задокументированный честный артефакт исходной вики
#   (незакрытая двухстрочная ссылка в indices_maintenance; гигиена, этап 4);
# [[INDICATOR] — вложенные опциональные скобки в грамматике FETCH.
KNOWN_OK = ["[[:", "%%i", "%%~", "****", "============", "groups.google.com",
            "[[INDICATOR]"]


def visible_text(page_html: str) -> str:
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", page_html, flags=re.S | re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    return htmllib.unescape(t)


def main() -> int:
    pages = sorted(DIST.glob("**/index.html"))
    if not pages:
        print(f"Нет собранных страниц в {DIST}. Сначала npm run build.")
        return 2

    hits_total = 0
    per_pattern: dict[str, int] = {}
    for f in pages:
        text = visible_text(f.read_text("utf-8", errors="replace"))
        for name, pat in PATTERNS.items():
            if pat in ("\x00",):
                raw = f.read_bytes()  # NUL ищем в сырых байтах
                if b"\x00" in raw:
                    per_pattern[name] = per_pattern.get(name, 0) + 1
                    print(f"  HIT {name}: {f.relative_to(DIST)}")
                    hits_total += 1
                continue
            for m in re.finditer(re.escape(pat), text):
                ctx = text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
                if any(ok in ctx for ok in KNOWN_OK):
                    continue
                per_pattern[name] = per_pattern.get(name, 0) + 1
                print(f"  HIT {name} в {f.relative_to(DIST)}: …{ctx}…")
                hits_total += 1
                if per_pattern[name] > 5:
                    print(f"    (далее по {name} не показываю, ищи отчёт)")

    print(f"\nСтраниц проверено: {len(pages)}; совпадений: {hits_total}")
    print(per_pattern or "ЧИСТО: сырой синтаксис в вывод не утёк")
    return 0 if hits_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
