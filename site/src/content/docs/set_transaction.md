---
title: "SET TRANSACTION"
old_id: set_transaction
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# SET TRANSACTION

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/)

## Формат
```
SET TRANSACTION
   [NAME tr_name]
   [<tr_option> ...]

<tr_option> ::=
     READ {ONLY | WRITE}
   | [NO] WAIT
   | [ISOLATION LEVEL] <isolation level>
   | NO AUTO UNDO
   | AUTO RELEASE TEMP BLOBID
   | RESTART REQUESTS
   | IGNORE LIMBO
   | LOCK TIMEOUT seconds
   | AUTO COMMIT
   | RESERVING <tables>
   | USING <dbhandles>

<isolation level> ::=
    SNAPSHOT [TABLE [STABILITY]]
  | SNAPSHOT AT NUMBER snapshot_number
  | READ COMMITTED [{[NO] RECORD_VERSION | READ CONSISTENCY}]

<tables> ::= <table_spec> [, <table_spec> ...]

<table_spec> ::= tablename [, tablename ...]
  [FOR [SHARED | PROTECTED] {READ | WRITE}]

<dbhandles> ::= dbhandle [, dbhandle ...]
```

## Описание
Оператор `SET TRANSACTION` задаёт параметры транзакции и стартует её. Старт транзакции осуществляется только клиентскими приложениями, но не сервером (за исключением автономных транзакций и некоторых фоновых системных потоков, например sweep).

Все предложения оператора необязательны. Если не задано ни одного, транзакция стартует со значениями по умолчанию: `READ WRITE`, `WAIT`, `ISOLATION LEVEL SNAPSHOT`.

Основные характеристики транзакции:

* режим доступа к данным (`READ WRITE` / `READ ONLY`);
* режим разрешения блокировок (`WAIT` / `NO WAIT`) с уточнением `LOCK TIMEOUT seconds` — временем ожидания в секундах при конфликте;
* уровень изоляции (`READ COMMITTED`, `SNAPSHOT`, `SNAPSHOT TABLE STABILITY`);
* резервирование таблиц (предложение `RESERVING`).

Необязательное предложение `NAME` задаёт имя транзакции и доступно только в ESQL; оно позволяет запускать несколько активных транзакций в одном приложении (требуется одноимённая переменная базового языка). Без `NAME` оператор применяется к транзакции по умолчанию. Предложение `USING` (список хендлов баз данных, к которым транзакция может получить доступ) также доступно только в ESQL.

Уровень `SNAPSHOT AT NUMBER snapshot_number` позволяет разделить снимок базы данных другой транзакции с указанным номером. Номер текущей транзакции доступен через контекстную переменную `CURRENT_TRANSACTION`.

## Пример
```sql
-- Транзакция только для чтения с уровнем изоляции READ COMMITTED
SET TRANSACTION
   READ ONLY
   WAIT
   ISOLATION LEVEL READ COMMITTED RECORD_VERSION;

-- Чтение/запись, ожидание не более 10 секунд
-- и резервирование таблицы для защищённой записи
SET TRANSACTION
   READ WRITE
   WAIT LOCK TIMEOUT 10
   ISOLATION LEVEL SNAPSHOT
   RESERVING ORDERS FOR PROTECTED WRITE;
```

## См. также
[COMMIT](/commit/), [ROLLBACK](/rollback/), [SAVEPOINT](/savepoint/), [Таблицы мониторинга](/tablicy_monitoringa/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
