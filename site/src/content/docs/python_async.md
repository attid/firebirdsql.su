---
title: "Работа с Firebird из Python асинхронно"
old_id: python_async
section: groups
type: article
date: "2026-09-24"
firebird:
  since: 
  until: 
  deprecated: false
---

# Работа с Firebird из Python асинхронно

У вас FastAPI-сервис, aiogram-бот или любой другой asyncio-код — и в него нужно прикрутить Firebird. Стандартный путь «возьму fdb и вызову из хэндлера» упирается в неприятный факт: драйверы Firebird блокирующие, и каждый запрос к базе намертво вешает event loop. Один медленный SELECT — и весь сервис стоит.

Выхода два: городить ручные обёртки через `run_in_executor` или взять готовый асинхронный диалект SQLAlchemy. Разберём второй — библиотеку [**sqlalchemy-firebird-async**](https://github.com/attid/sqlalchemy-firebird-async) (MIT, статус Production/Stable, требует SQLAlchemy 2.0+).

## Выбор бэкенда

Диалект работает поверх трёх драйверов:

- **fdb** — легаси C-драйвер, запускается в пуле потоков. Быстрый и стабильный, рекомендуемый вариант под нагрузку.
- **firebird-driver** — официальный драйвер для Firebird 3+, тоже через пул потоков. Выбор, если нужен современный поддерживаемый драйвер.
- **firebirdsql** — чистый Python asyncio без потоков. Экспериментально: у апстримного драйвера есть асинхронные баги, существует патченный форк [attid/pyfirebirdsql](https://github.com/attid/pyfirebirdsql), но даже с ним он примерно вчетверо медленнее — для продакшена пока не вариант.

## Установка

Бэкенд ставится extra-зависимостью:

```bash
pip install "sqlalchemy-firebird-async[fdb]"
# или
pip install "sqlalchemy-firebird-async[firebird-driver]"
# или (экспериментально)
pip install "sqlalchemy-firebird-async[firebirdsql]"
```

## Быстрый старт

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text

dsn = "firebird+fdb_async://sysdba:masterkey@localhost:3050//firebird/data/employee.fdb"

engine = create_async_engine(dsn, echo=True)

async def main():
    async with engine.connect() as conn:
        result = await conn.execute(text("select * from EMPLOYEE"))
        for row in result:
            print(row)

asyncio.run(main())
```

Формат строки: `firebird+<бэкенд>_async://user:password@host:port/path/to/db`. Для современного драйвера можно добавить кодировку: `...employee.fdb?charset=UTF8`.

## Схемы URL

| Бэкенд | Схема URL |
|---|---|
| fdb (легаси, пул потоков) | `firebird+fdb_async://user:pass@host:port/db_path` |
| firebird-driver (FB 3+) | `firebird+firebird_async://user:pass@host:port/db_path` |
| firebirdsql (asyncio) | `firebird+firebirdsql_async://user:pass@host:port/db_path` |

## Производительность

Бенчмарк автора библиотеки: 8 конкурентных задач по 5000 запросов (4 raw SQL + 4 ORM), суммарно 40 тысяч строк.

| Метрика | fdb (пул потоков) | firebirdsql (патченный) |
|---|---|---|
| Общее время | **4,53 с** | 116,20 с |
| Параллелизм | 6,16x | 7,94x |

Вывод честный: пул потоков с C-драйвером пока быстрее «настоящего» asyncio-драйвера на порядок — берите fdb-бэкенд, пока firebirdsql не пофиксят.

## Подводные камни

- Для fdb-бэкенда нужен установленный **fbclient** (клиентская библиотека Firebird) — сам пакет её не возит.
- firebirdsql считается экспериментальным: падения и странности возможны даже с патчем.
- SQLAlchemy ниже 2.0 не поддерживается — старый 1.4-стек не подойдёт.

## Что почитать дальше

- [Порты Firebird](/port_3050/) — какой порт указывать в строке подключения
- [ODBC-драйвер](/odbc/) — если Python не единственный потребитель базы
- [Глоссарий](/glossarij/) — сами SQL-запросы с примерами
