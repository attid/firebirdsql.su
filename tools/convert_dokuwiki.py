#!/usr/bin/env python3
"""Конвертер дампа DokuWiki (legacy/raw/*.txt) в Markdown (site/src/content/docs/).

Принципы (ADR-0004): механически, 1:1, без редакторских решений.
Схема frontmatter — ADR-0005: поля версий создаются пустыми, данные версий
проставляет отдельный скрипт этапа 4 (из таблиц «Версии сервера» в теле).

Покрытие синтаксиса — по фактическому составу корпуса (см. скан в истории
проекта): заголовки, ссылки [[..]], <code>/<file>, таблицы ^|, списки,%%,
''моно'', //курсив//, __подчёркивание__, сноски ((..)), :!:, \\, {{page>..}}.

Выход:
  site/src/content/docs/<old_id>.md
  tools/convert_report.json  — неразрешённые ссылки, пропущенные сниппеты,
                               таблицы без строки заголовка и пр.

Идемпотентно: перезаписывает выход целиком.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "legacy" / "raw"
OUT = ROOT / "site" / "src" / "content" / "docs"
REPORT = ROOT / "tools" / "convert_report.json"

# Страницы-сниппеты include-плагина и системные страницы: контент инлайнится
# или не переносится, отдельными страницами нового сайта они не становятся
# (редиректы для их старых URL — забота make_redirect_map, ему отдаётся
# skip-список в convert_report.json).
SNIPPET_IDS = {"operator", "datetype", "array_dim", "dom_search_condition", "sidebar"}

# Разделы по навигации старой вики (сайдбар); всё остальное — глоссарий.
SECTION_MAP = {
    "intro": [
        "o_sajte", "istochniki_i_avtory", "soglashenija_sintaksisa",
        "raznovidnosti_jazyka_sql", "tipy_dannyx",
    ],
    "install": [
        "samostojatelnaja_sborka_snapshota_firebird", "ustanovka_firebird_iz_snapshota",
        "ustanovka_firebird_na_linux", "skript_dlja_rezervirovanija_bazy_dannyx_na_python",
        "skript_dlja_rezervirovanija_bazy_dannyx_na_shell",
        "kak_ustanovit_na_linux_vtoroj_ehkzempljar_firebird",
        "podkljuchenie_k_baze_dannyx_iz_1s",
    ],
    "errors": ["obrabotka_oshibok", "gdscodes", "oshibki_pri_sozdanii_metadannyx"],
    "sql": [
        "matematicheskie_operacii_s_datoj", "execute_statement",
        "indices_maintenance", "transfer_table",
    ],  # sql0xx.* попадают по префиксу
    "groups": [
        "utils", "sistemnye_tablicy", "tablicy_monitoringa", "vstroennye_funkcii",
        "vstroennye_funkcii_po_gruppam", "operatory_konstrukcii_select",
        "ne_ispolzuemye_kljuchevye_slova", "ustanovka_apache_php_firebird_na_ubuntu",
    ],
    "glossary": ["glossarij", "1glossarij"],
}

CODE_RE = re.compile(r"<(code|file)(?:\s+([a-zA-Z0-9]+))?\s*>(.*?)</\1>", re.S)
NOFMT_RE = re.compile(r"%%([^\n]+?)%%")  # только в одну строку: иначе спарит %%
HEADING_RE = re.compile(r"^(={3,6})[ \t]*(.*?)[ \t]*(=+)[ \t]*(.*)$", re.M)
LINK_RE = re.compile(r"\[\[([^\n]+?)\]\]")  # текст с вложенными [] допустим
INCLUDE_RE = re.compile(r"^\{\{page>([a-z0-9_.:\-]+)\}\}\s*$", re.M)
ITALIC_RE = re.compile(r"(?<![:/])//([^/\n]+?)//")
MONO_RE = re.compile(r"''([^'\n]+?)''")
UNDER_RE = re.compile(r"__([^_\n]+?)__")
FOOTNOTE_RE = re.compile(r"\(\(([^)\n]+)\)\)")
SMILEY_MAP = {":!:": "\u26a0\ufe0f"}  # ⚠️
TABLE_ROW_RE = re.compile(r"^\s*([|^])")
LIST_RE = re.compile(r"^(\s+)([-*])\s+(.*)$")

_section_of = {}
for _sec, _ids in SECTION_MAP.items():
    for _i in _ids:
        _section_of[_i] = _sec


# Транслитерация кириллицы как в DokuWiki utf8_romanize (восстановлена по
# фактическим ID страниц вики: dlja, dannyx, ehkzempljar, konstrukcii,
# snapshota, podkljuchenie — внимание: ц→c, щ→ch)
TRANSLIT = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e",
    "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k", "л": "l", "м": "m",
    "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
    "ф": "f", "х": "x", "ц": "c", "ч": "ch", "ш": "sh", "щ": "ch",
    "ъ": "", "ы": "y", "ь": "", "э": "eh", "ю": "ju", "я": "ja",
}


def clean_id(raw: str) -> str:
    """Нормализация цели ссылки как в DokuWiki cleanID с транслитерацией:
    lower, кириллица -> латиница, пробел->_, выкидывание символов вне
    [a-z0-9_.:-]."""
    s = raw.strip().lower().split("#")[0]
    s = "".join(TRANSLIT.get(ch, ch) for ch in s)
    s = s.replace(" ", "_")
    return re.sub(r"[^a-z0-9_.:\-]", "", s)


def yaml_escape(s: str) -> str:
    """Экранирование для YAML-строки в двойных кавычках."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def section_for(pid: str) -> str:
    if pid in _section_of:
        return _section_of[pid]
    if pid.startswith("sql"):
        return "sql"
    return "glossary"


def type_for(pid: str, section: str) -> str:
    if pid in ("glossarij", "1glossarij"):
        return "landing"
    if pid in SECTION_MAP["groups"] or section == "groups":
        return "landing"
    return "term" if section == "glossary" else "article"


class Converter:
    def __init__(self, known_ids: set[str]):
        self.known_ids = known_ids
        self.unresolved: dict[str, list[str]] = {}

    # --- inline ---

    def _convert_link(self, m: re.Match) -> str:
        inner = m.group(1)
        target_raw, _, text = inner.partition("|")
        target_raw, text = target_raw.strip(), text.strip()
        if not target_raw:
            return ""  # [[]] — пустая ссылка, на вики не рендерилась
        if re.match(r"^https?://", target_raw):
            return f"[{text or target_raw}]({target_raw})"
        pid = clean_id(target_raw)
        if not text:
            text = target_raw
        if pid not in self.known_ids:
            self.unresolved.setdefault(pid, []).append(text)
            return text  # на старой вики это была бы красная ссылка
        return f"[{text}](/{pid}/)"

    def _inline(self, text: str) -> str:
        text = text.replace("[[]]", "")  # пустая ссылка: не рендерилась и у нас
        # DokuWiki разрешает жирность с внутренними пробелами (** текст **),
        # CommonMark — нет: подрезаем, иначе ** уходит в вывод литералом
        text = re.sub(r"\*\*[ \t]+(\S(?:.*?\S)?)[ \t]+\*\*", r"**\1**", text)
        text = LINK_RE.sub(self._convert_link, text)
        text = ITALIC_RE.sub(r"*\1*", text)
        text = MONO_RE.sub(r"`\1`", text)
        text = UNDER_RE.sub(r"<u>\1</u>", text)
        text = FOOTNOTE_RE.sub(r"(\1)", text)
        for src, dst in SMILEY_MAP.items():
            text = text.replace(src, dst)
        text = re.sub(r"(?<!\d)\.\.\.(?!\d)", "\u2026", text)  # ... -> …
        return text

    # --- таблицы ---

    @staticmethod
    def _split_cells(line: str) -> list[tuple[str, bool]]:
        r"""Разбор строки таблицы: разделители | и ^ вперемешку (DokuWiki это
        разрешает), | внутри [[ссылок]] и экранированные \| не режутся.
        Заголовочность ячейки определяет ЛЕВЫЙ разделитель."""
        line = line.strip()
        cells, cur, left_is_h = [], [], line[0] == "^"
        in_link = False
        i = 1
        while i < len(line):
            ch = line[i]
            if ch == "\\" and i + 1 < len(line) and line[i + 1] in "|^":
                cur.append(line[i + 1])
                i += 2
                continue
            if ch == "[" and line[i:i + 2] == "[[":
                in_link = True
            elif ch == "]" and line[i - 1] == "]":
                in_link = False
            if ch in "|^" and not in_link:
                cells.append(("".join(cur).strip(), left_is_h))
                cur, left_is_h = [], ch == "^"
            else:
                cur.append(ch)
            i += 1
        cells.append(("".join(cur).strip(), left_is_h))
        if len(cells) > 1 and not cells[-1][0]:
            cells.pop()  # фантом от замыкающего разделителя строки
        return cells

    @staticmethod
    def _code_inline(block: str) -> str:
        """Код-блок -> инлайновый код для ячейки таблицы: MD-таблицы не
        умеют многострочные fence внутри ячеек, переносы схлопываем."""
        lines = block.split("\n")
        body = " ".join(" ".join(lines[1:-1]).split()) if len(lines) > 2 else ""
        return f"`{body}`" if body else ""

    def _table(self, lines: list[str], stashed: dict) -> list[str]:
        rows = [[(self._inline(t), h) for t, h in self._split_cells(ln)]
                for ln in lines]
        ncols = max(len(r) for r in rows)
        has_header = rows and all(is_h for _, is_h in rows[0])
        header = rows[0] if has_header else [("", False)] * ncols
        body = rows[1:] if has_header else rows

        def md_row(cells: list[tuple[str, bool]]) -> str:
            out = []
            for i in range(ncols):
                txt, is_h = cells[i] if i < len(cells) else ("", False)
                # код-блок, попавший в ячейку, становится инлайновым кодом
                txt = re.sub(
                    r"\x00CODE(\d+)\x00",
                    lambda m: self._code_inline(stashed["code"][int(m.group(1))]),
                    txt,
                )
                # \\ в ячейке DokuWiki = перенос строки внутри ячейки
                txt = txt.replace("\\\\", "<br>")
                txt = txt.replace("|", "\\|")
                if not has_header and is_h:
                    txt = f"**{txt}**" if txt else ""
                out.append(txt)
            return "| " + " | ".join(out) + " |"

        out = [md_row(header), "|" + "---|" * ncols]
        out.extend(md_row(r) for r in body)
        return out

    # --- основной разбор ---

    def convert_body(self, text: str, known_ids: set[str], depth: int = 0) -> str:
        """Локальные стэши обязательны: рекурсия (include-сниппеты) не должна
        трогать состояние родителя, а результат сниппета вставляется
        плейсхолдером, чтобы родительский конвейер его не пережёвывал."""
        text = text.lstrip("\ufeff")

        stashed: dict[str, list[str]] = {"code": [], "nofmt": [], "inc": []}

        def stash_code(m: re.Match) -> str:
            lang = (m.group(2) or "").lower()
            body = m.group(3).strip("\n")
            stashed["code"].append(f"```{lang}\n{body}\n```")
            return f"\x00CODE{len(stashed['code']) - 1}\x00"

        def stash_nofmt(m: re.Match) -> str:
            stashed["nofmt"].append(f"`{m.group(1).strip()}`")
            return f"\x00NOFMT{len(stashed['nofmt']) - 1}\x00"

        def stash_include(m: re.Match) -> str:
            inc = m.group(1)
            f = RAW / f"{inc}.txt"
            if depth < 2 and f.is_file():
                snippet = self.convert_body(f.read_text("utf-8"), known_ids, depth + 1)
                stashed["inc"].append(snippet.strip())
                return f"\x00INC{len(stashed['inc']) - 1}\x00"
            return m.group(0)

        text = CODE_RE.sub(stash_code, text)
        text = NOFMT_RE.sub(stash_nofmt, text)
        text = INCLUDE_RE.sub(stash_include, text)

        # заголовки: первый H1 уходит в frontmatter и убирается из тела;
        # хвост после закрывающих = переносится на отдельную строку.
        # Предварительно отрываем маркер, склеенный с текстом («a===== X =====»):
        # без этого HEADING_RE его не видит и === утекает в вывод литералом.
        text = re.sub(r"(?<=[^\s=])(={3,6}[ \t]*\S)", r"\n\1", text)
        def heading(m: re.Match) -> str:
            lvl, txt, tail = len(m.group(1)), m.group(2), m.group(4)
            if not txt and not tail:
                return ""  # линия из одних '=' — мусор
            out = "#" * (lvl - 5 if lvl >= 6 else lvl - 3) + " " + self._inline(txt)
            return out + ("\n" + self._inline(tail) if tail.strip() else "")

        text = HEADING_RE.sub(heading, text)

        out: list[str] = []
        table_buf: list[str] = []
        for ln in text.split("\n"):
            if TABLE_ROW_RE.match(ln):
                table_buf.append(ln)
                continue
            if table_buf:
                out.extend(self._table(table_buf, stashed))
                table_buf = []
            m = LIST_RE.match(ln)
            if m:
                indent, marker, content = m.groups()
                lvl = len(indent) // 2
                bullet = "1." if marker == "-" else "-"
                out.append("  " * lvl + f"{bullet} {self._inline(content)}")
                continue
            ln = re.sub(r"\\\\\s*$", r"\\", ln)  # \\ -> жёсткий перенос
            ln = ln.lstrip(" ")                # DokuWiki игнорирует отступ простого текста
            out.append(self._inline(ln))
        if table_buf:
            out.extend(self._table(table_buf, stashed))

        text = "\n".join(out)
        # Жирность, разорванная переводом строки («**\nтекст**»): DokuWiki
        # так умеет, CommonMark — нет. Склеиваем перед финальной сборкой.
        text = re.sub(r"\*\*[ \t]*\n[ \t]*(\S(?:[^\n]*?\S)?)[ \t]*\*\*",
                      r"**\1**", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"

        for i, block in enumerate(stashed["code"]):
            text = text.replace(f"\x00CODE{i}\x00", block)
        for i, block in enumerate(stashed["nofmt"]):
            text = text.replace(f"\x00NOFMT{i}\x00", block)
        for i, block in enumerate(stashed["inc"]):
            text = text.replace(f"\x00INC{i}\x00", block)
        return text

    def convert_page(self, pid: str, raw: str) -> tuple[str, str]:
        self.unresolved_page = {}
        raw = raw.lstrip("\ufeff")
        m = re.search(r"^={6}\s*(.+?)\s*={6}", raw, re.M)
        title = m.group(1).strip() if m else pid
        body = self.convert_body(raw, self.known_ids)
        section = section_for(pid)
        ptype = type_for(pid, section)
        front = (
            "---\n"
            f'title: "{yaml_escape(title)}"\n'
            f"old_id: {pid}\n"
            f"section: {section}\n"
            f"type: {ptype}\n"
            "firebird:\n"
            "  since: \n"
            "  until: \n"
            "  deprecated: false\n"
            "---\n\n"
        )
        return front, body


def main() -> int:
    reg = json.loads((ROOT / "legacy" / "pages.json").read_text("utf-8"))
    ids = [p["id"] for p in reg["pages"]]
    known = set(ids)
    conv = Converter(known)

    OUT.mkdir(parents=True, exist_ok=True)
    converted, no_h1 = [], []
    for pid in ids:
        if pid in SNIPPET_IDS:
            continue
        f = RAW / f"{pid}.txt"
        if not f.is_file():
            continue
        front, body = conv.convert_page(pid, f.read_text("utf-8"))
        (OUT / f"{pid}.md").write_text(front + body, "utf-8")
        converted.append(pid)
        if not re.search(r"^={6}", f.read_text("utf-8").lstrip("\ufeff"), re.M):
            no_h1.append(pid)

    unresolved = {k: sorted(set(v)) for k, v in conv.unresolved.items()}
    REPORT.write_text(json.dumps({
        "converted": len(converted),
        "skipped_snippets": sorted(SNIPPET_IDS),
        "pages_without_h1": no_h1,
        "unresolved_links": unresolved,
    }, ensure_ascii=False, indent=1), "utf-8")

    print(f"Сконвертировано: {len(converted)} страниц -> {OUT}")
    print(f"Сниппетов инлайнено (не страницы): {len(SNIPPET_IDS)}")
    print(f"Без H1 (title из id): {len(no_h1)}: {', '.join(no_h1[:10])}")
    print(f"Неразрешённых целей ссылок: {len(unresolved)}")
    for k in sorted(unresolved)[:15]:
        print(f"  - {k}: {', '.join(unresolved[k][:3])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
