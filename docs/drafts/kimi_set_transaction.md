kimi version 2.0.2
• The user wants a reference page for SET_TRANSACTION on firebirdsql.su. The facts cut off at "READ WRITE ... могут быть ка..." but I have enough. Format strictly. Available in: DSQL, ESQL (per facts). Syntax block verbatim from facts. Description 100-200 words. Example 1-2 SQL examples.

  Write the page as markdown output. Should I write it to a file? The user says "напиши справочную страницу" — output in reply is fine.

• # SET_TRANSACTION

  ## Доступно в

  DSQL, ESQL

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

  Все предложения оператора необязательны. Если не задано ни одного предложения, транзакция стартует со значениями по умолчанию: `READ WRITE`, `WAIT`, `ISOLATION LEVEL SNAPSHOT`.

  Основные характеристики транзакции:

  * режим доступа к данным (`READ WRITE` / `READ ONLY`);
  * режим разрешения блокировок (`WAIT` / `NO WAIT`) с возможным уточнением `LOCK TIMEOUT seconds` — временем ожидания оператора в секундах при конфликте;
  * уровень изоляции (`READ COMMITTED`, `SNAPSHOT`, `SNAPSHOT TABLE STABILITY`);
  * резервирование таблиц (предложение `RESERVING`).

  Необязательное предложение `NAME` задаёт имя транзакции и доступно только в ESQL; оно позволяет одновременно запускать несколько активных транзакций в одном приложении (должна быть объявлена одноимённая переменная базового языка). Если `NAME` не указано, оператор применяется к транзакции по умолчанию. Предложение `USING` (список хендлов баз данных, к которым транзакция может получить доступ) также доступно только в ESQL.

  Уровень `SNAPSHOT AT NUMBER snapshot_number` позволяет разделить снимок базы данных другой транзакции с указанным номером. Номер текущей транзакции можно получить через контекстную переменную `CURRENT_TRANSACTION`.

  ## Пример

  ```sql
  -- Транзакция только для чтения с уровнем изоляции READ COMMITTED
  SET TRANSACTION
     READ ONLY
     WAIT
     ISOLATION LEVEL READ COMMITTED RECORD_VERSION;

  -- Транзакция чтения/записи с ожиданием не более 10 секунд
  -- и резервированием таблицы для защищённой записи
  SET TRANSACTION
     READ WRITE
     WAIT LOCK TIMEOUT 10
     ISOLATION LEVEL SNAPSHOT
     RESERVING ORDERS FOR PROTECTED WRITE;
  ```

To resume this session: kimi -r session_6fc89285-9661-4901-92f6-2888f18244a8
