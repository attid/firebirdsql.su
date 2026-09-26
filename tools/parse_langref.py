#!/usr/bin/env python3
"""Извлекает конструкции языка из русских Language Reference (sim1984/langrefNN,
исходники ibase.ru-книг) и строит матрицу «конструкция → версия».

Форматы:
  langref25/30 — DocBook XML: section > info/title + formalpara «Доступно в:»
  langref40/50/60 — AsciiDoc: `=== `ИМЯ()`  ` + блок «.Доступно в»

Нормализация имён — та же, что в конвертере (cleanID + транслит), чтобы
матчить со страницами сайта. Результат:
  tools/version_matrix.json — {конструкция: [2.5?, 3.0?, 4.0?, 5.0?, 6.0?]}
  tools/langref_report.md   — сводка + сверка с нашими страницами
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "docs" / "langref-src"
VERSIONS = ["2.5", "3.0", "4.0", "5.0", "6.0"]
DIRS = {"2.5": "langref25", "3.0": "langref30", "4.0": "langref40",
        "5.0": "langref50", "6.0": "langref60"}

TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "x", "ц": "c", "ч": "ch", "ш": "sh", "щ": "ch",
    "ъ": "", "ы": "y", "ь": "", "э": "eh", "ю": "ju", "я": "ja",
}


def norm(name: str) -> str:
    """Нормализация имени конструкции под наши old_id (как cleanID конвертера)."""
    s = name.strip()
    # «CHAR_LENGTH( <string> )» -> «CHAR_LENGTH»; аргументы не часть имени
    if "(" in s:
        s = s[: s.index("(")].strip()
    s = s.replace("()", "").strip()
    # варианты 6.0 «ALTER INDEX ... ACTIVE» -> базовое имя «ALTER INDEX»
    s = re.sub(r"\s*\.\.\..*$", "", s).strip()
    s = s.lower().replace("$", "")  # DokuWiki cleanID выкидывает $
    s = "".join(TRANSLIT.get(ch, ch) for ch in s)
    s = s.replace(" ", "_")
    return re.sub(r"[^a-z0-9_.\-]", "", s)


def compact(name: str) -> str:
    """Второй ключ: без подчёркиваний/дефисов — add_day ≡ addday."""
    return norm(name).replace("_", "").replace("-", "")


# ---------- AsciiDoc (4.0/5.0/6.0) ----------

# Конструкции: заголовок уровня 2-3, начинающийся с бэктиков; в заголовке
# может быть несколько имён через запятую («CHAR_LENGTH()», «CHARACTER_LENGTH()»)
# или аргументы («CHAR_LENGTH( <string> )»). Подсекции с текстом до бэктиков
# («Ограничение `NOT NULL`») не начинаются с бэктика и отсекаются.
# Второй вид: заголовки капсом БЕЗ бэктиков («== SET TRANSACTION») в главах
# transaction/dml старших версий.
ADOC_HEADING = re.compile(r"^={2,3}\s+`")
ADOC_HEADING_CAPS = re.compile(r"^={2,3}\s+([A-Z][A-Z0-9 ()\[\]<>|,._\-]*[A-Z0-9)\]])\s*$")


def adoc_names(line: str) -> list[str]:
    return re.findall(r"`([^`]+)`", line)


def heading_names(line: str) -> list[str]:
    """Имена из заголовка: бэктик-спаны либо капс-текст."""
    if "`" in line:
        return adoc_names(line)
    m = ADOC_HEADING_CAPS.match(ln if (ln := line.strip()) else "")
    return [m.group(1)] if m else []


def extract_adoc(version: str) -> dict[str, dict]:
    out = {}
    files = sorted((SRC / DIRS[version]).rglob("*.adoc"))
    for f in files:
        text = f.read_text("utf-8", errors="replace")
        cur_keys = []
        pending_avail = False
        for ln in text.split("\n"):
            stripped = ln.strip()
            is_btick = ADOC_HEADING.match(ln)
            is_caps_m = ADOC_HEADING_CAPS.match(stripped) if "`" not in ln else None
            if is_btick or is_caps_m:
                names = adoc_names(ln) if is_btick else [is_caps_m.group(1)]
                cur_keys = [norm(n) for n in names]
                cur_keys = [k for k in cur_keys if k]
                for raw, k in zip(names, cur_keys):
                    rec = out.setdefault(k, {"name": raw.strip(), "files": set()})
                    rec["files"].add(f.name)
                pending_avail = False
                continue
            if cur_keys and stripped == ".Доступно в":
                pending_avail = True
                continue
            if cur_keys and pending_avail and stripped:
                avail = stripped
                for k in cur_keys:
                    out[k]["available"] = avail
                pending_avail = False
    for v in out.values():
        v["files"] = sorted(v["files"])
    return out


# ---------- DocBook XML (2.5/3.0) ----------

NS = {"d": "http://docbook.org/ns/docbook"}


def extract_xml(version: str) -> dict[str, dict]:
    out = {}
    for f in sorted((SRC / DIRS[version]).glob("*.xml")):
        # keywords.xml — словарь зарезервированных слов, не конструкции
        if f.name == "keywords.xml":
            continue
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError as e:
            print(f"  WARN: {f.name}: {e}", file=sys.stderr)
            continue
        for s in root.findall(".//d:section", NS):
            t = s.find("d:info/d:title", NS)
            if t is None or not t.text:
                continue
            # заголовок бывает совмещённым: «CHAR_LENGTH, CHARACTER_LENGTH»
            for name in t.text.split(","):
                name = name.strip()
                if not name:
                    continue
                cur = norm(name)
                if not cur:
                    continue
                rec = out.setdefault(cur, {"name": name, "files": set()})
                rec["files"].add(f.name)
                if "available" not in rec:
                    for fp in s.findall("d:formalpara", NS):
                        ft = fp.find("d:title", NS)
                        if ft is not None and "Доступно в" in (ft.text or ""):
                            rec["available"] = " ".join(
                                "".join(fp.itertext()).split())
                        break
    for v in out.values():
        v["files"] = sorted(v["files"])
    return out


# ---------- наши страницы ----------

def our_pages() -> dict[str, dict]:
    out = {}
    for f in (ROOT / "site" / "src" / "content" / "docs").glob("*.md"):
        text = f.read_text("utf-8")
        m_title = re.search(r'^title:\s*"(.+?)"', text, re.M)
        m_sec = re.search(r"^section:\s*(\S+)", text, re.M)
        m_type = re.search(r"^type:\s*(\S+)", text, re.M)
        pid = f.stem
        out[pid] = {
            "title": m_title.group(1) if m_title else pid,
            "section": m_sec.group(1) if m_sec else "?",
            "type": m_type.group(1) if m_type else "?",
        }
    return out


# ---------- таблицы «Версии сервера» из тел наших страниц ----------

def wiki_version_tables() -> dict[str, list[str]]:
    """Из MD-таблиц «Версии сервера»: страница -> версии с «Да»."""
    out = {}
    for f in (ROOT / "site" / "src" / "content" / "docs").glob("*.md"):
        text = f.read_text("utf-8")
        m = re.search(
            r"## Версии сервера\s*\n((?:\|.*\n)+)", text)
        if not m:
            continue
        rows = [r for r in m.group(1).strip().split("\n") if r]
        if len(rows) < 3:
            continue
        header = [c.strip() for c in rows[0].strip("|").split("|")]
        versions = [h for h in header if re.fullmatch(r"[0-9.]+", h)]
        if not versions:
            continue
        cols = [i for i, h in enumerate(header) if h in versions]
        yes = []
        for row in rows[2:]:  # rows[1] — разделитель
            cells = [c.strip() for c in row.strip("|").split("|")]
            for i in cols:
                if i < len(cells) and cells[i] in ("Да", "**Да**", "+", "**+**"):
                    yes.append(header[i])
        if yes:
            out[f.stem] = sorted(set(yes),
                                 key=lambda v: [int(p) for p in v.split(".")])
    return out


def main() -> int:
    langref: dict[str, dict[str, dict]] = {}
    for v in VERSIONS:
        mode = extract_xml if v in ("2.5", "3.0") else extract_adoc
        langref[v] = mode(v)
        print(f"{v}: {len(langref[v])} конструкций")

    all_names = set()
    for v in VERSIONS:
        all_names |= set(langref[v])
    matrix = {}
    for name in all_names:
        matrix[name] = {
            "display": next(langref[v][name]["name"]
                            for v in VERSIONS if name in langref[v]),
            "in": {v: (name in langref[v]) for v in VERSIONS},
        }

    ours = our_pages()
    tables = wiki_version_tables()
    compact_ours = {compact(meta["title"]): pid for pid, meta in ours.items()}

    matched, ours_only, langref_only = [], [], []
    matched_via: dict[str, str] = {}
    for pid, meta in ours.items():
        if pid in matrix:
            matched.append((pid, meta))
            matched_via[pid] = "id"
        elif compact(meta["title"]) in matrix:
            # матчим и по компактному нормализованному заголовку
            lang_name = compact(meta["title"])
            matched.append((pid, meta))
            matched_via[pid] = f"заголовок -> {lang_name}"
        else:
            ours_only.append((pid, meta))
    for name in matrix:
        if name not in {p for p, _ in matched} and name not in matched_via.values():
            langref_only.append(name)
    # страницы-не-конструкции (лендинги, статьи, служебные) — отдельный список
    ours_only_terms = [(p, m) for p, m in ours_only if m["type"] == "term"]
    ours_only_other = [(p, m) for p, m in ours_only if m["type"] != "term"]

    for name, rec in matrix.items():
        rec["ours"] = name in matched_via
        rec["wiki_versions"] = tables.get(name)

    (ROOT / "tools" / "version_matrix.json").write_text(
        json.dumps({"matrix": matrix, "versions": VERSIONS, "wiki_tables": tables},
                   ensure_ascii=False, indent=1), "utf-8")

    rep = ["# Матрица версий: Language Reference × наш контент", "",
           f"Конструкций в руководствах (объединённо): {len(matrix)}; "
           f"страниц у нас: {len(ours)}; совпало: {len(matched)}.", "",
           f"## У нас (type=term), но нет в руководствах — кандидаты deprecated/until: {len(ours_only_terms)}", ""]
    for pid, meta in sorted(ours_only_terms):
        rep.append(f"- `{pid}` — {meta['title']}")
    rep += ["", f"## Служебные/статьи (не конструкции, матчить не требуется): {len(ours_only_other)}", ""]
    for pid, meta in sorted(ours_only_other):
        rep.append(f"- `{pid}` ({meta['section']}/{meta['type']}) — {meta['title']}")
    rep += ["", f"## В руководствах, но нет у нас — кандидаты в новые статьи: {len(langref_only)}", ""]
    for name in sorted(langref_only):
        rec = matrix[name]
        ver = [v for v in VERSIONS if rec["in"][v]]
        rep.append(f"- `{name}` — {rec['display']} (есть в: {', '.join(ver)})")
    (ROOT / "tools" / "langref_report.md").write_text(
        "\n".join(rep) + "\n", "utf-8")

    print(f"совпало: {len(matched)}, у нас нет в руководствах (terms): {len(ours_only_terms)}, "
          f"служебных: {len(ours_only_other)}, новых кандидатов: {len(langref_only)}")
    print("выход: tools/version_matrix.json, tools/langref_report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
