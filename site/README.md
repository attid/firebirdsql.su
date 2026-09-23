# site/ — новый сайт на Astro

Каркас этапа 1. Контент — Markdown в `src/content/docs/` (конвертируется из
`legacy/raw/` скриптом `tools/convert_dokuwiki.py`).

- Схема URL: `/<old_id>/` — плоская, точный 1:1 с ID страниц DokuWiki
  (id = имя файла без слагификации, см. `generateId` в `src/content.config.ts`).
- Разделы (глоссарий/FAQ/SQL-рецепты/утилиты) — навигацией и коллекциями,
  не вложенностью URL.
- Поиск: Pagefind (локальный индекс, строится в `npm run build` после Astro).
- Тёмная/светлая тема: `data-theme` + localStorage, без мигания.
- Подсветка SQL: Shiki dual themes (`github-light`/`github-dark`).
- Кнопка «копировать» на код-блоках.
- `/download/` — страница загрузки со ссылками на официальные бинарники.
- `/en/` — зарезервированное пространство под будущую локализацию (noindex).

## Команды

    npm install
    npm run build     # astro build + pagefind --site dist
    npm run preview   # локальный просмотр dist
    npm run dev       # dev-сервер (поискового индекса в dev нет — это норма)

## Контентная схема

Frontmatter каждой страницы: `title`, `old_id`, `section`
(glossary|intro|install|errors|sql|groups), `type` (term|article|landing),
`firebird.{since,until,deprecated}` (ADR-0005; поля могут быть пустыми,
удалять нельзя). Валидируется зодом-схемой при сборке.
