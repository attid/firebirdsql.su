# SET_TRANSACTION

## Доступно в
DSQL, ESQL

## Формат

```sql
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

Оператор `SET TRANSACTION` задаёт параметры транзакции и осуществляет её запуск. Старт транзакции инициируется клиентскими приложениями; сервер выполняет запуск только для автономных транзакций и служебных фоновых процессов (например, sweep). Одно клиентское приложение может одновременно запускать произвольное количество транзакций. Каждой транзакции последовательно присваивается 64-битный номер, доступный через контекстную переменную `CURRENT_TRANSACTION`. Общее число транзакций ограничено значением 2^48^ - 1 с момента создания или восстановления базы данных из резервной копии.

Все параметры оператора являются необязательными. Если параметры не заданы явно, транзакция стартует с конфигурацией по умолчанию: `READ WRITE WAIT ISOLATION LEVEL SNAPSHOT`.

Ключевые характеристики транзакции:
* **Режим доступа:** `READ WRITE` (чтение и запись) или `READ ONLY` (только чтение);
* **Разрешение блокировок:** `WAIT` (ожидание), `NO WAIT` (без ожидания) или ограничение времени ожидания `LOCK TIMEOUT seconds`;
* **Уровень изоляции:** `READ COMMITTED`, `SNAPSHOT`, `SNAPSHOT TABLE STABILITY` или подключение к существующему снимку через `SNAPSHOT AT NUMBER`;
* **Резервирование таблиц:** предложение `RESERVING`.

Предложения `NAME` (имя транзакции) и `USING` (список хендлов баз данных) доступны исключительно в ESQL.

## Пример

```sql
-- Запуск транзакции только для чтения с уровнем изоляции Read Committed и таймаутом блокировки
SET TRANSACTION READ ONLY WAIT
  ISOLATION LEVEL READ COMMITTED READ CONSISTENCY
  LOCK TIMEOUT 10;

-- Запуск транзакции на запись с изоляцией Snapshot и резервированием таблицы
SET TRANSACTION READ WRITE WAIT
  ISOLATION LEVEL SNAPSHOT
  RESERVING customer FOR PROTECTED WRITE;
```
