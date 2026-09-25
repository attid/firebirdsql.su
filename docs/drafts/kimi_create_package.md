kimi version 2.0.2
• Write the reference page. Just output markdown. No file requested — probably just output text. User asked to write a page; likely output the markdown in reply.

• # CREATE PACKAGE

  ## Доступно в

  DSQL

  ## Формат

  ```
  CREATE PACKAGE package_name
  [SQL SECURITY {DEFINER | INVOKER}]
  AS
  BEGIN
    [<package_item> ...]
  END

  <package_item> ::=
      <function_decl>;
    | <procedure_decl>;

  <function_decl> ::=
    FUNCTION func_name [(<in_params>)]
    RETURNS <type> [NOT NULL] [COLLATE collation]
    [DETERMINISTIC]

  <procedure_decl> ::=
    PROCEDURE proc_name [(<in_params>)]
    [RETURNS (<out_params>)]

  <in_params>  ::= <param_decl> [{= | DEFAULT} <value>] [, ...]
  <out_params> ::= <param_decl> [, ...]
  <param_decl> ::= paramname <type> [NOT NULL] [COLLATE collation]
  <type>       ::= <datatype> | [TYPE OF] domain_name | TYPE OF COLUMN rel.col
  <value>      ::= {literal | NULL | context_var}
  ```

  ## Описание

  Оператор `CREATE PACKAGE` создаёт заголовок нового пакета. Имя пакета должно быть уникальным среди имён всех пакетов и может содержать до 63 символов.

  Заголовок пакета содержит только объявления процедур и функций: имена, входные параметры (с возможными значениями по умолчанию) и типы возвращаемых значений. Тела реализуются отдельно оператором `CREATE PACKAGE BODY`. Процедуры и функции, объявленные в заголовке, доступны вне тела пакета через полный идентификатор `package_name.procedure_name` и `package_name.function_name`. Процедуры и функции, определённые в теле пакета, но не объявленные в заголовке, не видны вне тела пакета — это главное отличие пакета от отдельных хранимых процедур и функций: пакет позволяет скрыть внутреннюю реализацию и выставить наружу только нужный интерфейс.

  Имена процедур и функций, объявленных в заголовке, должны быть уникальны среди имён процедур и функций, объявленных в заголовке и теле пакета. Желательно, чтобы они не пересекались с именами хранимых процедур и функций из глобального пространства имён: внутри пакета при совпадении имён всегда будет вызвана процедура/функция пакета.

  Необязательное предложение `SQL SECURITY` задаёт привилегии, с которыми выполняются процедуры и функции пакета: `INVOKER` — с привилегиями вызывающего пользователя (по умолчанию), `DEFINER` — с привилегиями владельца пакета, дополненными привилегиями, выданными самому пакету оператором `GRANT`. Переопределять привилегии выполнения для отдельных процедур и функций пакета запрещено. Привилегии по умолчанию для новых объектов можно изменить оператором `ALTER DATABASE SET DEFAULT SQL SECURITY {DEFINER | INVOKER}`.

  В редакторах, требующих завершения операторов точкой с запятой (например, `isql`), перед созданием пакета следует сменить терминатор оператора с помощью `SET TERM`.

  ## Пример

  ```sql
  SET TERM ^;

  CREATE PACKAGE APP_UTIL
  SQL SECURITY DEFINER
  AS
  BEGIN
    FUNCTION FORMAT_NAME(FIRST_NAME VARCHAR(50), LAST_NAME VARCHAR(50))
      RETURNS VARCHAR(120) NOT NULL DETERMINISTIC;

    PROCEDURE RECALC_BALANCE(ACCOUNT_ID BIGINT, AS_OF DATE DEFAULT CURRENT_DATE)
      RETURNS (NEW_BALANCE NUMERIC(15,2));
  END^

  SET TERM ;^
  ```

To resume this session: kimi -r session_1e715a70-032d-48ac-a2a6-45ad14f504c0
