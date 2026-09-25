kimi version 2.0.2
• The user gave facts that appear truncated mid-sentence (the prompt cut off at "запретив передавать в него значен"). But I have enough. Write the page in Russian following the strict format. The task is to write a reference page — presumably output it as text (no file path given). I'll output the page in my final message. Or maybe write to a file? No file specified; deliver in the reply. Actually the page content should appear in final message. Let me compose.

  Facts known: Firebird 3.0 (user said), DSQL availability, syntax, params table, description: creates stored function, name uniqueness, composite statement header+body, terminator note, input params by value, NOT NULL. Facts cut off — I should use only what's given plus what's in the visible facts. Don't invent too much. Description 150-250 words: назначение, ключевые предложения, отличия от хранимых процедур и UDF.

  Differences from procedures: function returns a value via RETURNS, can be used in expressions; procedures invoked via EXECUTE PROCEDURE and return output params. UDF: legacy external functions declared with DECLARE EXTERNAL FUNCTION; CREATE FUNCTION creates PSQL stored functions (or UDR external via ENGINE). Deterministic clause. SQL SECURITY.

  The facts include DETERMINISTIC and external routine spec, rights-clause. I can mention these. UDF distinction: I need to be careful — facts only say "имя должно быть уникальным среди имён всех хранимых функций и внешних (UDF) функций". The user asks for differences from stored procedures and UDF. That's general knowledge; the user explicitly asked for it, so include briefly: stored function returns scalar value and callable in SQL expressions; UDF is legacy external mechanism (DECLARE EXTERNAL FUNCTION), superseded by stored functions/UDR. This is standard documented knowledge; acceptable.

  Word count 150-250 words for description. Write it.

• # CREATE FUNCTION

  ## Доступно в

  DSQL (появился в Firebird 3.0)

  ## Формат

  ```sql
  CREATE FUNCTION funcname [(<inparam> [, <inparam> ...])]
    RETURNS <type> [NOT NULL] [COLLATE collation]
    [DETERMINISTIC]
    <routine-body>

  <inparam> ::= <param_decl> [{= | DEFAULT} <value>]

  <value> ::= {literal | NULL | context_var}

  <param_decl> ::= paramname <type> [NOT NULL] [COLLATE collation]

  <type> ::=
      datatype
    | [TYPE OF] domain
    | TYPE OF COLUMN rel.col

  <routine-body> ::=
      <psql-routine-spec>
    | <external-routine-spec>

  <psql-routine-spec> ::=
    [SQL SECURITY {DEFINER | INVOKER}] <psql-routine-body>

  <external-routine-spec> ::=
    EXTERNAL NAME '<module-name>!<routine-name>[!<misc-info>]'
    ENGINE engine
    [AS extbody]
  ```

  ## Описание

  Оператор `CREATE FUNCTION` создаёт новую хранимую функцию — подпрограмму, которая принимает входные параметры и возвращает одиночное значение, поэтому её можно вызывать прямо в SQL-выражениях (в списке выбора `SELECT`, в условиях, в присваиваниях). В этом её главное отличие от хранимой процедуры: процедура выполняется оператором `EXECUTE PROCEDURE` и возвращает данные через выходные параметры, тогда как функция обязана вернуть значение через `RETURNS` и встраивается в выражения. От устаревших внешних функций (UDF, объявляемых через `DECLARE EXTERNAL FUNCTION`) хранимая функция отличается тем, что её тело пишется на PSQL и исполняется внутри сервера; при этом тот же оператор позволяет создать внешнюю функцию на базе UDR через предложение `EXTERNAL NAME ... ENGINE ...`.

  Имя хранимой функции (до 63 символов) должно быть уникальным среди имён всех хранимых функций и внешних (UDF) функций; для подпрограмм достаточно уникальности в рамках охватывающего модуля. Желательно также избегать совпадений с именами функций в PSQL-пакетах: из пакета нельзя вызвать одноимённую функцию глобального пространства имён — всегда будет вызвана функция пакета.

  `CREATE FUNCTION` — составной оператор из заголовка и тела. Заголовок определяет имя, объявляет входные параметры и тип возвращаемого значения. Тело состоит из необязательных объявлений локальных переменных, подпрограмм и именованных курсоров и одного или нескольких блоков операторов, заключённых во внешний блок `BEGIN ... END`; объявления и операторы завершаются точкой с запятой.

  Входные параметры заключаются в скобки после имени и передаются по значению: их изменение внутри функции не влияет на аргументы вызывающей программы. Для параметра можно указать `NOT NULL`, порядок сортировки `COLLATE` и значение по умолчанию через `=` или `DEFAULT`. Тип параметра и возвращаемого значения задаётся типом данных SQL, доменом (`TYPE OF domain`) либо типом столбца таблицы или представления (`TYPE OF COLUMN rel.col`). Предложение `DETERMINISTIC` помечает функцию как детерминированную, а `SQL SECURITY` задаёт контекст прав доступа.

  При работе в `isql` и подобных редакторах из-за конфликта точек с запятой внутри тела с терминатором оператора перед компиляцией функции используйте `SET TERM`.

  ## Пример

  ```sql
  SET TERM ^ ;

  CREATE FUNCTION FN_FULL_NAME (
      FIRST_NAME  TYPE OF COLUMN EMPLOYEE.FIRST_NAME,
      LAST_NAME   TYPE OF COLUMN EMPLOYEE.LAST_NAME
  )
  RETURNS VARCHAR(85) NOT NULL
  AS
  BEGIN
    RETURN LAST_NAME || ', ' || FIRST_NAME;
  END^

  SET TERM ; ^

  -- Вызов функции в SQL-выражении
  SELECT FN_FULL_NAME(FIRST_NAME, LAST_NAME) AS FULL_NAME
  FROM EMPLOYEE;
  ```

  Замечание: предоставленный в задании выдержек текст фактов обрывается на ограничении `NOT NULL` входного параметра («запретив передавать в него значен…») — описание выше опирается только на приведённую часть фактов и общедокументированные сведения об отличиях функций от процедур и UDF, которые вы явно попросили включить.

To resume this session: kimi -r session_1ccd1a92-5519-468f-a169-2f82592850eb
