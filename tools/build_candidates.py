#!/usr/bin/env python3
"""Чистый приоритизированный список кандидатов на новые статьи.

Из матрицы LR × контент отбираются langref-конструкции без нашей страницы,
артефакты (заголовки глав книги) и не-статьи (ключевые слова, контекстные
константы) отсеиваются. Приоритет: чем новее версия, где появилась
конструкция, тем выше (новое = никто не описал; старое = описано в сотне
мест). Выход: tools/candidates.md
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSIONS = ["2.5", "3.0", "4.0", "5.0", "6.0"]

# не-статьи: ключевые слова, контекстные константы, псевдо-имена
SKIP = {
    "function", "procedure", "sysdba", "real", "deleting", "inserting",
    "updating", "order_by", "order by", "current_role", "current_user",
    "current_time", "current_timestamp", "current_date", "current_transaction",
    "current_connection", "sqlcode", "gdscode", "all", "at", "call", "binary",
    "begin", "active", "user", "role", "package", "domain", "index",
    "table", "view", "trigger", "exception", "sequence", "generator",
    "value", "values", "default", "nulls", "row", "rows",
}


def vkey(v):
    return [int(p) for p in v.split(".")]


def main() -> int:
    d = json.loads((ROOT / "tools" / "version_matrix.json").read_text("utf-8"))
    m, versions = d["matrix"], d["versions"]

    cats = {"function": [], "statement": [], "systable": [], "misc": []}
    skipped = 0
    for k, r in m.items():
        if r["ours"]:
            continue
        name = r["display"]
        if re.search(r"[а-яё]", name, re.I):
            skipped += 1  # заголовок главы книги
            continue
        ku = k.upper()
        if ku in SKIP or name.upper() in SKIP:
            skipped += 1
            continue
        ver = [v for v in versions if r["in"][v]]
        newest = min(ver, key=vkey) if ver else "?"  # первое появление
        # категории
        if name.upper().startswith(("RDB$", "MON$")):
            cat = "systable"
        elif re.match(r"^(ALTER|CREATE|DROP|RECREATE|SET|EXECUTE|GRANT|REVOKE|DECLARE|COMMENT|RELEASE|SELECT|INSERT|UPDATE|DELETE|MERGE|COMMIT|ROLLBACK|SAVEPOINT)", name, re.I):
            cat = "statement"
        elif "(" in name or re.match(r"^[A-Z][A-Z0-9_$]*$", name):
            cat = "function"
        else:
            cat = "misc"
        cats[cat].append((newest, vkey(newest), name, k, ver))

    out = ["# Кандидаты на новые статьи (очищено от артефактов)", "",
           "Источники: LR 2.5–6.0 (sim1984/ibase.ru). Артефакты (заголовки глав,",
           f"ключевые слова) отсеяны: {skipped}. Приоритет — по новизне версии:",
           "5.0/6.0 фичи никто в рунете ещё не описал.", ""]

    prio_order = ["6.0", "5.0", "4.0", "3.0", "2.5"]
    for cat, title in [("function", "Функции"),
                       ("statement", "Операторы DDL/DML"),
                       ("systable", "Системные таблицы (мониторинг и метаданные; отдельная книга)"),
                       ("misc", "Прочее (разобрать вручную)")]:
        items = sorted(cats[cat], key=lambda t: (-t[1][0], t[2].lower()))
        out += [f"## {title} — {len(items)}", "",
                f"Группировка по первому появлению в LR (2.5 = пробел ещё с тех времён).", ""]
        by_ver = {}
        for newest, _, name, k, ver in items:
            by_ver.setdefault(newest, []).append((name, k, ver))
        for v in prio_order:
            if v not in by_ver:
                continue
            out.append(f"### появилось в {v} ({len(by_ver[v])})")
            for name, k, ver in sorted(by_ver[v]):
                out.append(f"- {name} → `/{k}/` ({', '.join(ver)})")
            out.append("")
        out.append("")

    (ROOT / "tools" / "candidates.md").write_text("\n".join(out) + "\n", "utf-8")
    total = sum(len(v) for v in cats.values())
    print(f"Кандидатов после чистки: {total} (артефактов отсеяно: {skipped})")
    for cat, items in cats.items():
        print(f"  {cat}: {len(items)}")
    print("выход: tools/candidates.md")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
