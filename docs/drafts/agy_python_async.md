# Работа с Firebird из Python асинхронно

Современный стек веб-разработки и микросервисов на Python — FastAPI, Litestar, aiogram, Celery/Arq и чистый `asyncio` — построен вокруг неблокирующего ввода-вывода (event loop). Если в таком сервисе выполнить синхронный запрос к базе данных, весь цикл событий заблокируется на время выполнения SQL-запроса, и приложение перестанет отвечать другим пользователям.

Для работы с СУБД Firebird в асинхронном стеке используется библиотека **`sqlalchemy-firebird-async`** (лицензия MIT, статус Production/Stable), которая предоставляет асинхронный диалект для SQLAlchemy 2.0+ (GitHub: [github.com/attid/sqlalchemy-firebird-async](https://github.com/attid/sqlalchemy-firebird-async), PyPI: `sqlalchemy-firebird-async`).

---

## Зачем асинхронность с Firebird

Традиционные драйверы Firebird для Python работают синхронно. Когда обработчик FastAPI или хэндлер Telegram-бота вызывает синхронную функцию обращения к БД, поток event loop «замирает». Пока Firebird выполняет выборку или ожидает блокировку транзакции, другие запросы и сетевые пакеты встают в очередь.

Асинхронный диалект SQLAlchemy решает эту проблему: запросы либо выполняются через неблокирующий сетевой протокол, либо прозрачно делегируются в пул потоков (worker threads) без блокировки основного event loop.

---

## Выбор бэкенда

`sqlalchemy-firebird-async` поддерживает три бэкенда, каждый из которых ориентирован на свои сценарии:

1. **`fdb`** — легаси C-драйвер, работающий через клиентскую библиотеку Firebird (`fbclient`). Вызовы оборачиваются в пул потоков. Наиболее быстрый, зрелый и стабильный вариант для нагруженных систем.
2. **`firebird-driver`** — официальный современный драйвер для Firebird 3+, также работающий через пул потоков.
3. **`firebirdsql`** — драйвер на чистом Python asyncio. Экспериментальный: в оригинальном апстриме есть известные баги, существует патченный форк `attid/pyfirebirdsql`. Работает заметно медленнее C-библиотек.

---

## Установка

Устанавливайте библиотеку вместе с выбранным экстра-пакетом драйвера:

```bash
# Рекомендуемый вариант (наивысшая производительность):
pip install "sqlalchemy-firebird-async[fdb]"

# Для официального драйвера Firebird 3+:
pip install "sqlalchemy-firebird-async[firebird-driver]"

# Для чистого Python asyncio (экспериментальный):
pip install "sqlalchemy-firebird-async[firebirdsql]"
```

---

## Схемы URL подключения

Общий формат строки подключения:

```text
firebird+fdb_async://user:password@host:port/path/to/db
```

| Схема URL | Драйвер / Бэкенд | Особенности |
|---|---|---|
| `firebird+fdb_async://` | `fdb` | C-библиотека в пуле потоков, максимальная скорость |
| `firebird+firebird_async://` | `firebird-driver` | Официальный драйвер в пуле потоков, можно указать `?charset=UTF8` |
| `firebird+firebirdsql_async://` | `firebirdsql` | Чистый Python asyncio, без внешних C-зависимостей |

---

## Быстрый старт с кодом

Пример инициализации асинхронного движка и выполнения запроса через SQLAlchemy 2.0:

```python
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import text

dsn = "firebird+fdb_async://sysdba:masterkey@localhost:3050//firebird/data/employee.fdb"
engine = create_async_engine(dsn, echo=True)

async def main():
    async_session = async_sessionmaker(engine, expire_on_commit=False)
    
    async with async_session() as session:
        result = await session.execute(text("SELECT FIRST 5 emp_no, first_name, last_name FROM employee"))
        for row in result:
            print(row.emp_no, row.first_name, row.last_name)

    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())
```

> **Примечание:** Для схемы `firebird+firebird_async://` при необходимости можно явно задать кодировку:
> ```python
> dsn = "firebird+firebird_async://sysdba:masterkey@localhost:3050//firebird/data/employee.fdb?charset=UTF8"
> ```

---

## Производительность и бенчмарки

Бенчмарк автора библиотеки демонстрирует поведение бэкендов при конкурентной нагрузке (тест: 8 параллельных задач по 5 000 запросов, суммарно 40 000 строк):

| Бэкенд / Конфигурация | Общее время (`total`) | Фактор параллелизма | Разница в скорости |
|---|---|---|---|
| `fdb` (в пуле потоков) | **4.53 с** | **6.16x** | Базовый ориентир (быстрее всех) |
| Патченный `firebirdsql` (asyncio) | **116.2 с** | — | ~25x медленнее `fdb` (~4x медленнее на одиночных) |

**Вывод:** для реальных production-нагрузок и высоконагруженных сервисов рекомендуется использовать бэкенд **`fdb`**.

---

## Подводные камни и нюансы

- **Требование к `fbclient` для `fdb`:** Так как `fdb` является C-обёрткой, в системе (или Docker-контейнере) обязательно должна быть установлена клиентская библиотека Firebird (`libfbclient.so` в Linux или `fbclient.dll` в Windows).
- **Экспериментальность `firebirdsql`:** Чистый Python-драйвер не требует C-библиотек, но апстрим содержит ошибки, а скорость парсинга сетевых пакетов средствами интерпретатора существенно уступает скомпилированным C-библиотекам.
- **Два слэша в пути к БД:** Обратите внимание на синтаксис DSN для абсолютных путей на Linux-серверах: `//firebird/data/employee.fdb` (первый слэш разделяет хост/порт и путь, второй начинает путь от корня ФС).

---

## Что почитать дальше

- Настройка пула соединений (`QueuePool`, `AsyncAdaptedQueuePool`) в SQLAlchemy 2.0 для многопоточных бэкендов.
- Интеграция `sqlalchemy-firebird-async` в Dependency Injection фреймворка FastAPI (`async with session:`).
- Управление транзакциями Firebird (уровни изоляции `READ COMMITTED`, `SNAPSHOT`) в асинхронных сессиях SQLAlchemy.
- Оптимизация сборки Docker-образов для Python с установкой `libfbclient2` / `libfbclient3`.
