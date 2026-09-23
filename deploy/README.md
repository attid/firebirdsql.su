# deploy/ — развёртывание

Готовый стек этапа 2: nginx + статика + карта 301 + remark42 за rate limiting.

## Как это устроено

1. **CI собирает образ**: каждый пуш в `main` — GitHub Actions
   (`.github/workflows/docker.yml`) собирает образ из `deploy/Dockerfile`,
   гоняет smoke-тест редиректов по всему `legacy/pages.json` и пушит в
   реестр: `ghcr.io/attid/firebirdsql-site:latest` (+ тег `sha-…`).
   Одноразово после первого пуша: сделать пакет публичным
   (GitHub → Packages → firebirdsql-site → Package settings → Change
   visibility → Public), чтобы сервер тянул без авторизации.
2. **Сервер — Portainer** (файлы .env на сервере запрещены):
   Stacks → Add stack → вставить содержимое `docker-compose.yml` →
   в разделе **Environment** задать переменные (обязательные помечены
   в файле): `SECRET`, `TELEGRAM_TOKEN`, `AUTH_YANDEX_CID/CSEC`,
   `AUTH_GOOGLE_CID/CSEC`, `ADMIN_SHARED_ID`, опционально `REMARK_URL`,
   `TZ`. Deploy stack.
3. Сайт поднимается на `127.0.0.1:8081` — наружу его выводит существующий
   реверс-прокси хоста. Обновление: в Portainer → Stack → Recreate
   (образ :latest перетянется), либо Press «Pull and redeploy».

Локальная разработка без Portainer: `deploy/.env` рядом с compose
(см. `.env.example`) — подстановки `${...}` compose делает сам.

## Файлы

| Файл | Назначение |
|------|-----------|
| `Dockerfile` | Двухэтапная сборка: node (astro build + pagefind) → nginx:alpine |
| `docker-compose.yml` | Сервисы: `site`, `remark42`, закомментированный слот `ai` (ADR-0007) |
| `nginx.conf` | Полный конфиг: карта 301 (обе старые формы URL + срезание `ns:`-префикса из кэша поисковиков), rate limiting, кэш ассетов, честный 404 |
| `redirects.map` | Генерируется `tools/make_redirect_map.py` — руками не править |
| `nginx-redirects.conf` | Краткая шпаргалка редиректов (генерируется там же) |
| `.env.example` | Заготовка секретов remark42 (Telegram/Яндекс/Google) |

## Первый запуск на сервере

```bash
cd <репо>/deploy
cp .env.example .env        # заполнить SECRET, токены бота и OAuth-ключи
docker compose up -d --build
```

Сайт поднимается на `127.0.0.1:8081` — наружу его выводит существующий
реверс-прокси хоста (внешний TLS уже есть у текущей конфигурации сервера).

## Проверка перед переключением и после

```bash
# по всему legacy/pages.json: обе старые формы -> 301, новые -> 200
python3 tools/smoke_redirects.py http://localhost:8081

# то же на проде после переключения
python3 tools/smoke_redirects.py https://firebirdsql.su
```

## Защита (DDoS / злоупотребления)

- `limit_req`: `/remark42/` — 10 r/m с burst 20; будущий `/api/ai/` — 6 r/m
  с burst 3 (правила уже в конфиге, ADR-0007);
- `limit_conn perip 30`; таймауты и `client_max_body_size` на проксируемых
  location; штатные лимиты remark42;
- апстрим remark42 резолвится в момент запроса — nginx стартует даже без него.

## Откат

Старый контейнер вики не удалять до подтверждения стабильности. Откат —
возврат upstream реверс-прокси на старый порт/контейнер, минуты (см.
docs/seo-migration.md).
