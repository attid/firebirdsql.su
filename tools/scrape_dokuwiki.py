#!/usr/bin/env python3
"""Снимает полный дамп страниц DokuWiki firebirdsql.su через публичный export_raw.

Источники:
  - список страниц: doku.php?do=index (полное дерево пространств имён);
  - текст страниц:  doku.php?do=export_raw&id=<page_id>  (несуществующая
    страница возвращает HTML вместо raw — так детектируем битые);
  - медиафайлы:     lib/exe/fetch.php?media=<id> (по ссылкам {{...}} и <img>
    в raw-тексте).

Выход:
  legacy/raw/<ns>/<page>.txt  — raw DokuWiki-разметка;
  legacy/media/<ns>/<file>    — медиафайлы;
  legacy/pages.json           — реестр: id, статус, размер, пути.

Зависимости: только стандартная библиотека.
Идемпотентно: существующие непустые файлы пропускаются (--force — перекачать).
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE = "https://firebirdsql.su"
OUT = Path(__file__).resolve().parent.parent / "legacy"
DELAY = 0.15  # пауза между запросами, секунды
UA = "firebirdsql-su-migration/0.1 (one-time dump for static site rebuild)"
TIMEOUT = 30

LINK_RE = re.compile(r"[?&]id=([A-Za-z0-9_.:\-]+)")
BRACE_MEDIA_RE = re.compile(r"\{\{([^}]+)\}\}")
IMG_MEDIA_RE = re.compile(r"(?:src|href)=\"[^\"]*fetch\.php\?media=([^\"&]+)")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    last_err = None
    for _ in range(2):  # одна повторная попытка на сетевой сбой
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read()
        except Exception as e:  # noqa: BLE001 - регистрируем любую ошибку сети
            last_err = e
            time.sleep(1.0)
    raise RuntimeError(f"fetch failed: {url}: {last_err}")


def page_ids() -> list[str]:
    html = fetch(f"{BASE}/doku.php?do=index").decode("utf-8", "replace")
    ids = sorted(set(LINK_RE.findall(html)))
    return ids


def raw_path(page_id: str) -> Path:
    parts = [p for p in page_id.split(":")]
    stem = parts[-1] if parts[-1] else "start"
    return OUT / "raw" / Path(*parts[:-1]) / f"{stem}.txt"


def dump_page(page_id: str, force: bool) -> dict:
    path = raw_path(page_id)
    if not force and path.exists() and path.stat().st_size > 0:
        return {"id": page_id, "ok": True, "bytes": path.stat().st_size,
                "file": str(path.relative_to(OUT)), "cached": True}

    url = f"{BASE}/doku.php?do=export_raw&id={urllib.parse.quote(page_id, safe=':')}"
    body = fetch(url)
    # Существующая страница отдаёт raw-текст; несуществующая — HTML-страницу.
    ok = not body.lstrip()[:512].lstrip().startswith((b"<!DOCTYPE", b"<html"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    return {"id": page_id, "ok": ok, "bytes": len(body),
            "file": str(path.relative_to(OUT)), "cached": False}


def media_ids(text: str) -> set[str]:
    out = set()
    for grp in BRACE_MEDIA_RE.findall(text):
        ref = grp.split("|")[0].split("?")[0].strip()
        # page>... — include-плагин (вставка другой вики-страницы, не медиа);
        # такие страницы снимаются в общем порядке как обычные.
        if not ref or ref.startswith(("rss>", "page>", "http://", "https://", "//")):
            continue
        out.add(ref)
    for ref in IMG_MEDIA_RE.findall(text):
        out.add(urllib.parse.unquote(ref).split("?")[0])
    return out


def dump_media(mid: str, force: bool) -> dict:
    rel = "/".join(mid.replace(":", ":").split(":"))
    path = OUT / "media" / rel
    if not force and path.exists() and path.stat().st_size > 0:
        return {"id": mid, "ok": True, "file": str(path.relative_to(OUT)), "cached": True}
    url = f"{BASE}/lib/exe/fetch.php?media={urllib.parse.quote(mid, safe=':')}"
    try:
        body = fetch(url)
    except Exception as e:  # noqa: BLE001
        return {"id": mid, "ok": False, "error": str(e)}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)
    return {"id": mid, "ok": True, "bytes": len(body),
            "file": str(path.relative_to(OUT)), "cached": False}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--force", action="store_true",
                    help="перекачать даже уже сохранённые файлы")
    args = ap.parse_args()

    ids = page_ids()
    print(f"Страниц в индексе: {len(ids)}")
    pages = []
    for i, pid in enumerate(ids, 1):
        try:
            rec = dump_page(pid, args.force)
        except Exception as e:  # noqa: BLE001
            rec = {"id": pid, "ok": False, "error": str(e)}
        pages.append(rec)
        if i % 25 == 0:
            print(f"  страницы: {i}/{len(ids)}")
        time.sleep(DELAY)

    mids = set()
    for rec in pages:
        f = OUT / rec.get("file", "")
        if rec.get("ok") and f.is_file():
            mids |= media_ids(f.read_text("utf-8", "replace"))
    print(f"Медиафайлов в ссылках: {len(mids)}")

    media = []
    for i, mid in enumerate(sorted(mids), 1):
        media.append(dump_media(mid, args.force))
        if i % 25 == 0:
            print(f"  медиа: {i}/{len(mids)}")
        time.sleep(DELAY)

    reg = {
        "source": BASE,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "pages_total": len(pages),
        "pages_ok": sum(1 for p in pages if p.get("ok")),
        "pages_broken": [p["id"] for p in pages if not p.get("ok")],
        "media_total": len(media),
        "media_ok": sum(1 for m in media if m.get("ok")),
        "pages": pages,
        "media": media,
    }
    (OUT / "pages.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"Готово: страниц ok {reg['pages_ok']}/{len(pages)}, "
          f"битых {len(reg['pages_broken'])}, "
          f"медиа ok {reg['media_ok']}/{len(media)}")
    if reg["pages_broken"]:
        print("Битые (несуществующие) страницы:")
        for pid in reg["pages_broken"]:
            print(f"  - {pid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
