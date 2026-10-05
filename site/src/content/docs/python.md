---
title: "Подключение к Firebird из Python"
old_id: python
section: groups
type: article
date: "2026-10-05"
firebird:
  since: 
  until: 
  deprecated: false
---

# Подключение к Firebird из Python

Драйвер [firebirdsql](https://pypi.org/project/firebirdsql/) — **чистый Python**: не требует ни клиентской библиотеки fbclient, ни компиляции, ставится в venv и контейнеры одной командой. Работает по сети с Firebird 2.5 и новее (проверено на 5.0).

## Установка

```bash
pip install firebirdsql==1.4.7
```

## Подключение и запрос

```python
import firebirdsql

con = firebirdsql.connect(
    dsn="firebird:/var/lib/firebird/data/employee.fdb",
    user="SYSDBA",
    password="masterkey",
    charset="utf-8",
)

cur = con.cursor()
cur.execute(
    "SELECT FIRST_NAME, LAST_NAME, SALARY "
    "FROM EMPLOYEE ORDER BY SALARY DESC ROWS 5"
)
for first, last, salary in cur.fetchall():
    print(f"  {first} {last} — {salary:.2f}")

con.close()
```

> ⚠️ **Нюанс с портом, пойманный на практике.** Формат DSN — `host:port:path`,
> но с Firebird 5 и драйвером 1.4.7 при явном порте
> (`firebird/3050:/path`) подключение падает с
> «unavailable database». Порт опускается (`firebird:/path`) —
> используется 3050 по умолчанию.

- **charset="utf-8"** — для кириллицы указывайте всегда.

## Параметризованные запросы

Плейсхолдер `?`, значения — кортежем:

```python
cur.execute(
    "SELECT FIRST_NAME, LAST_NAME FROM EMPLOYEE WHERE DEPT_NO = ?",
    (dept,),
)
```

## Альтернативные драйверы

| Драйвер | Что требует | Когда брать |
|---|---|---|
| firebirdsql (pure) | ничего | по умолчанию, контейнеры, venv |
| [fdb](https://pypi.org/project/fdb/) | fbclient | легаси-проекты, старые версии Firebird |
| [firebird-driver](https://pypi.org/project/firebird-driver/) | fbclient | официальный современный, FB 3+ |

Для асинхронных приложений (FastAPI, aiogram) есть
[asyncio-диалект SQLAlchemy](/python_async/) поверх этих драйверов.

## Пример целиком

Рабочий пример с этим кодом — в [репозитории сайта](https://github.com/attid/firebirdsql.su/tree/main/examples/python): Dockerfile + docker compose с Firebird 5.0.4 и демо-базой employee, прогоняется одной командой.

## Что почитать дальше

- [Работа с Firebird из Python асинхронно](/python_async/) — если у вас asyncio-стек
- [Порты Firebird](/port_3050/) — что открывать в firewall
- [Типы данных](/tipy_dannyx/) — что придёт из базы в ваши переменные
