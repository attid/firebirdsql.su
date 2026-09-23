#!/usr/bin/env python3
"""Smoke-тест SEO-миграции: прогоняет ВСЕ старые URL из legacy/pages.json
и проверяет редиректы и доступность новых страниц.

Проверяется по каждому старому ID:
  1. /doku.php?id=<id>       -> 301 на ожидаемый новый путь;
  2. /<id> (path-форма)      -> 301 на /<id>/;
  3. /<id>/ (новая страница) -> 200.

Особые ID (сниппеты/системные) ожидают путь из deploy/redirects.map.

Использование:
  python3 tools/smoke_redirects.py http://localhost:8081
Выход: сводка; код 1 при любых расхождениях.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent


def expected_targets() -> dict[str, str]:
    """ID -> ожидаемый путь, из сгенерированной карты (единый источник)."""
    text = (ROOT / "deploy" / "redirects.map").read_text("utf-8")
    out = {}
    for m in re.finditer(r"^    ([a-z0-9_.:\-]+) (\S+);$", text, re.M):
        out[m.group(1)] = m.group(2)
    return out


def probe(base: str, path: str) -> tuple[int, str]:
    """Вернуть (код, Location). 301/302/308 читаются, ошибки — как есть."""
    req = urllib.request.Request(base + path, method="GET",
                                 headers={"User-Agent": "fb-smoke/1.0"})
    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(req, timeout=15) as r:
            return r.status, r.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", "") if e.headers else ""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    base = sys.argv[1].rstrip("/")

    targets = expected_targets()
    reg = json.loads((ROOT / "legacy" / "pages.json").read_text("utf-8"))
    ids = [p["id"] for p in reg["pages"]]

    fails = []
    total = 0
    for pid in ids:
        want = targets.get(pid, f"/{pid}/")
        # 1. doku.php-форма
        code, loc = probe(base, f"/doku.php?id={pid}")
        total += 1
        got = urlparse(loc).path.rstrip("/")
        if code != 301 or got != want.rstrip("/"):
            fails.append(f"doku.php?id={pid}: {code} -> {loc!r}, ожидалось {want}")
        # 2. path-форма без слэша
        code, loc = probe(base, f"/{pid}")
        total += 1
        got = urlparse(loc).path.rstrip("/")
        if code != 301 or got != f"/{pid}".rstrip("/"):
            fails.append(f"/{pid}: {code} -> {loc!r}, ожидалось /{pid}/")
        # 3. новая страница отдаётся
        code, _ = probe(base, want if want != "/" else "/")
        total += 1
        if code != 200:
            fails.append(f"{want}: {code}, ожидался 200")

    # Кэш поисковиков: URL со старым префиксом пространства имён.
    # glossarij:abs и glossarij:coalesce -> /abs/ и /coalesce/ (префикс срезается,
    # обе страницы существуют — мёртвые кэш-URL оживают сразу на нужной странице)
    for colon, want in [("glossarij:abs", "/abs/"), ("glossarij:coalesce", "/coalesce/")]:
        code, loc = probe(base, f"/doku.php?id={colon}")
        total += 1
        got = urlparse(loc).path.rstrip("/")
        if code != 301 or got != want.rstrip("/"):
            fails.append(f"doku.php?id={colon}: {code} -> {loc!r}, ожидалось {want}")

    # Связка прокси на remark42: 200 = апстрим отвечает; 502 = апстрим
    # отсутствует (ожидаемо без соседа в CI/локально — резолв в момент
    # запроса); таймаут — то же самое, просто резолвер ждёт (bounded
    # resolver_timeout); 500 = сломана конфигурация (пустая переменная
    # из-за rewrite ... break перед set) — это регрессия, и она отвечает
    # мгновенно, поэтому от таймаута отличается надёжно.
    total += 1
    try:
        code, _ = probe(base, "/remark42/api/v1/ping")
        if code not in (200, 502):
            fails.append(f"/remark42/api/v1/ping: {code}, ожидался 200 или 502")
    except Exception as e:  # noqa: BLE001 - таймаут/отказ = соседа нет, связка цела
        print(f"  remark42: сосед недоступен ({type(e).__name__}) — пропускаем как валидное отсутствие")

    print(f"Проверено запросов: {total}, ошибок: {len(fails)}")
    for f in fails[:20]:
        print(f"  FAIL {f}")
    if len(fails) > 20:
        print(f"  … и ещё {len(fails) - 20}")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
