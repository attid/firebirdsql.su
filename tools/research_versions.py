#!/usr/bin/env python3
"""Сбор доказательств версий для терминов из tools/versions_review.md.

Для каждого термина ищем по текстам ВСЕХ пяти руководств (adoc+xml,
без keywords.xml) вхождения его токенов — не только заголовки: старые
книги описывают AUTONOMOUS TRANSACTION / MON$-таблицы в прозе и синтаксисе.
Плюс вырезаем из нашей страницы прозу с упоминанием версий («в Firebird
X.Y», «появилась» и т.п.).

Выход: stdout с evidence-блоками — решения принимает человек/агент,
скрипт ничего не пишет в контент.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "langref-src"
DOCS = ROOT / "site" / "src" / "content" / "docs"
VERSIONS = ["2.5", "3.0", "4.0", "5.0", "6.0"]
DIRS = {"2.5": "langref25", "3.0": "langref30", "4.0": "langref40",
        "5.0": "langref50", "6.0": "langref60"}

# термин -> токены поиска (регистронезависимо, слово/фраза)
TERMS = {
    "addday": ["ADDDAY"],
    "addmillisecond": ["ADDMILLISECOND"],
    "addminute": ["ADDMINUTE"],
    "addmonth": ["ADDMONTH"],
    "addsecond": ["ADDSECOND"],
    "addweek": ["ADDWEEK"],
    "addyear": ["ADDYEAR"],
    "autoddl": ["AUTO DDL", "AUTODDL"],
    "autonomous_transaction": ["AUTONOMOUS"],
    "comment": ["COMMENT ON", "COMMENT statement"],
    "connect": ["CONNECT TO", "CONNECT statement", "<connect"],
    "constraint": []  # понятие, решения не требует
    ,
    "create_generator": ["CREATE GENERATOR"],
    "create_global_temporary_table": ["GLOBAL TEMPORARY"],
    "day": ["DAY("],
    "distinct": []  # ключевое слово всех версий
    ,
    "dow": ["DOW("],
    "drop_generator": ["DROP GENERATOR"],
    "first": ["SELECT FIRST", "FIRST "],
    "gbak": ["gbak"],
    "gdscodes": ["GDSCODE"],
    "gfix": ["gfix"],
    "gsec": ["gsec"],
    "hour": ["HOUR("],
    "if": ["IF (", "IF("],
    "inserting_updating_deleting": ["INSERTING", "UPDATING", "DELETING"],
    "instclient.exe": ["instclient"],
    "interval": ["BETWEEN"],
    "is_not_distinct_from": ["IS NOT DISTINCT FROM", "IS [NOT] DISTINCT"],
    "join": ["JOIN"],
    "minute": ["MINUTE("],
    "mon_attachments": ["MON$ATTACHMENTS"],
    "mon_database": ["MON$DATABASE"],
    "mon_transactions": ["MON$TRANSACTIONS"],
    "month": ["MONTH("],
    "new_old": ["NEW.", "OLD."],
    "rdb_check_constraints": ["RDB$CHECK_CONSTRAINTS"],
    "rdb_database": ["RDB$DATABASE"],
    "rdb_fields": ["RDB$FIELDS"],
    "rdb_generators": ["RDB$GENERATORS"],
    "rdb_index_segments": ["RDB$INDEX_SEGMENTS"],
    "rdb_indices": ["RDB$INDICES"],
    "rdb_ref_constraints": ["RDB$REF_CONSTRAINTS"],
    "rdb_relation_constraints": ["RDB$RELATION_CONSTRAINTS"],
    "rdb_relation_fields": ["RDB$RELATION_FIELDS"],
    "rdb_relations": ["RDB$RELATIONS"],
    "rdb_roles": ["RDB$ROLES"],
    "rdb_security_classes": ["RDB$SECURITY_CLASSES"],
    "rdb_transactions": ["RDB$TRANSACTIONS"],
    "rdb_trigger_messages": ["RDB$TRIGGER_MESSAGES"],
    "rdb_triggers": ["RDB$TRIGGERS"],
    "recursive": ["RECURSIVE"],
    "returns": ["RETURNS"],
    "second": ["SECOND("],
    "set_term": ["SET TERM"],
    "sweep": ["sweep"],
    "vremennye_tablicy": ["GLOBAL TEMPORARY", "GTT"],
    "weekday": ["WEEKDAY"],
    "year": ["YEAR("],
    "yearday": ["YEARDAY"],
}


def load_bodies() -> dict[str, str]:
    bodies = {}
    for v in VERSIONS:
        parts = []
        for f in (SRC / DIRS[v]).rglob("*"):
            if f.suffix in (".adoc", ".xml") and f.name != "keywords.xml":
                try:
                    parts.append(f.read_text("utf-8", errors="replace"))
                except OSError:
                    pass
        bodies[v] = "\n".join(parts)
    return bodies


def prose_versions(pid: str) -> list[str]:
    """Вытащить версии из прозы нашей страницы."""
    f = DOCS / f"{pid}.md"
    if not f.is_file():
        return []
    text = f.read_text("utf-8")
    body = re.sub(r"^---.*?---", "", text, flags=re.S)
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    found = re.findall(r"[Ff]irebird\s+([12]\.[0-9]|3\.0|4\.0|5\.0)", body)
    hits = re.findall(r"(?:появил|введён|добавлен|работает только|начиная)[^\n.]{0,80}", body, re.I)
    return found[:6], hits[:3]


def main() -> int:
    bodies = load_bodies()
    out = []
    for pid, tokens in TERMS.items():
        if not tokens:
            out.append(f"### {pid}\n  (понятие — версия не применима)\n")
            continue
        ev = {}
        for v in VERSIONS:
            hits = sum(bodies[v].upper().count(t.upper()) for t in tokens)
            ev[v] = hits
        pv, prose = prose_versions(pid)
        out.append(
            f"### {pid}\n"
            f"  вхождения: " + " ".join(f"{v}={ev[v]}" for v in VERSIONS) + "\n"
            + (f"  проза страницы, версии: {pv}\n" if pv else "")
            + ("".join(f"  проза: «{h.strip()[:90]}»\n" for h in prose))
        )
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
