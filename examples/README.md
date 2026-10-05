# Примеры подключения к Firebird из популярных языков

Каждый пример делает **одно и то же** (сравнивайте языки глазами):
подключается к `employee.fdb` — штатной демо-базе Firebird — и выводит
топ-5 сотрудников по зарплате. Всё выполняется в контейнерах,
на хост ничего не ставить.

Каждый пример проверен запуском в Docker (см. историю коммитов);
если пример сломается из-за новой версии драйвера — CI или ручной
прогон это покажет.

## Запуск

```bash
./init.sh                        # firebird 5.0.4 + employee.fdb (идемпотентно)
docker compose run --rm go       # Go (nakagami/firebirdsql v0.9.21)
docker compose run --rm python   # Python (firebirdsql 1.4.7, pure)
docker compose run --rm php      # PHP (pdo_firebird собирается из исходников PHP)
docker compose run --rm fpc      # Free Pascal (SQLdb, сборка через lazarus-build-station)

docker compose down -v           # погасить всё и убрать данные
```

Требования: Docker + docker compose. Хост `firebird` внутри сети compose —
имя сервиса, порт 3050 не пробрасывается наружу.

## Проверенные нюансы (не выдуманы — пойманы при прогоне)

- **Python (firebirdsql 1.4.7)**: DSN с явным портом (`firebird/3050:...`)
  против Firebird 5 падает «unavailable database» — порт опускаем
  (`firebird:/path`), 3050 используется по умолчанию.
- **PHP**: в официальном php-образе `pdo_firebird` нет — собирается
  из исходников PHP против `firebird-dev` Debian (см. Dockerfile).
- **Free Pascal**: FPC 3.2.2 ищет `libfbclient.so.2.5.1` (зашитое имя),
  Debian ставит клиент с другим soname — в Dockerfile симлинк с
  автопоиском реальной библиотеки через ldconfig. Клиент 3.0.8 (Ubuntu)
  работает с сервером 5.0.4 по сети без проблем.
- **compose run** не пересобирает образ по правке файлов — после правки
  кода явно `docker compose build <язык>`.
- Пароль SYSDBA в контейнере задаётся переменной **`FIREBIRD_ROOT_PASSWORD`**
  (не ISC_PASSWORD).

## Откуда employee.fdb

Каноническая демо-база собирается из штатных скриптов Firebird
[`empddl.sql`](firebird/empddl.sql) + [`empdml.sql`](firebird/empdml.sql)
(схема + данные, тег v5.0.4, лицензия IPL — заголовки сохранены).
Официальный docker-образ сам employee не кладёт: `FIREBIRD_DATABASE`
создаёт пустую базу, скрипты накатываются `init.sh`.
