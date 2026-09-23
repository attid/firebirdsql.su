# site/ — новый сайт на Astro

Каркас появляется на этапе 1 (см. ROADMAP.md). Решения: Astro + Pagefind,
контент в Markdown в `src/content/`, конвертируется из `legacy/raw/`
скриптом `tools/convert_dokuwiki.py`.

Схема URL: `/<slug>/`, плоская, честное 1:1 с ID страниц DokuWiki
(вся старая вика лежит в корневом пространстве имён: `abs` → `/abs/`).
Разделы сайта (глоссарий, FAQ, SQL-рецепты) — навигацией и коллекциями
контента, не вложенностью URL.

Сборка (появится с каркасом):

    npm install
    npm run build   # astro build + pagefind
