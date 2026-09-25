kimi version 2.0.2
• Just write the reference page. Output it directly in markdown. User likely wants the page content. I'll output as final message (or write to a file?). No file path specified — output in the reply. Format: H1 OPEN, sections. "Доступно в" — PSQL only. Include params note about parameters. Description 100-200 words. Example 1-2 examples. No internal links.

• # OPEN

  ## Доступно в

  PSQL

  ## Формат

  ```sql
  OPEN cursor_name;
  ```

  **Параметры оператора OPEN**

  | Параметр | Описание |
  |---|---|
  | cursor_name | Имя курсора. Курсор с таким именем должен быть предварительно объявлен с помощью оператора `DECLARE ... CURSOR`. |

  ## Описание

  Оператор `OPEN` открывает ранее объявленный курсор, выполняет объявленный в нём оператор `SELECT` и получает записи из результирующего набора данных. Оператор `OPEN` применим только к курсорам, объявленным в операторе `DECLARE ... CURSOR`.

  Если в операторе `SELECT` курсора имеются параметры, то они должны быть объявлены как локальные переменные или входные (выходные) параметры до того, как объявлен курсор. При открытии курсора параметру присваивается текущее значение переменной. Это важно при повторном открытии курсора внутри цикла: каждый вызов `OPEN` заново вычисляет результирующий набор с учётом актуальных на момент открытия значений переменных, использованных в условиях выборки.

  После открытия курсор устанавливается перед первой записью результирующего набора. Последовательная выборка записей выполняется оператором `FETCH`, а по завершении работы курсор должен быть закрыт оператором `CLOSE`, чтобы освободить связанные с ним ресурсы.

  ## Пример

  Использование оператора `OPEN` в процедуре:

  ```sql
  SET TERM ^;

  CREATE OR ALTER PROCEDURE GET_RELATIONS_NAMES
  RETURNS (
    RNAME CHAR(31)
  )
  AS
    DECLARE C CURSOR FOR (
      SELECT RDB$RELATION_NAME
      FROM RDB$RELATIONS);
  BEGIN
    OPEN C;
    WHILE (1 = 1) DO
    BEGIN
      FETCH C INTO :RNAME;
      IF (ROW_COUNT = 0) THEN
        LEAVE;
      SUSPEND;
    END
    CLOSE C;
  END^

  SET TERM ;^
  ```

  Использование оператора `OPEN` с параметрами. Курсор `CUR_F` использует в условии выборки переменную `RELATION`, поэтому при каждом открытии он получает набор полей для текущего отношения:

  ```sql
  EXECUTE BLOCK
  RETURNS (
    SCRIPT BLOB SUB_TYPE TEXT)
  AS
    DECLARE VARIABLE FIELDS VARCHAR(8191);
    DECLARE VARIABLE FIELD_NAME TYPE OF RDB$FIELD_NAME;
    DECLARE VARIABLE RELATION RDB$RELATION_NAME;
    DECLARE VARIABLE SOURCE TYPE OF COLUMN RDB$RELATIONS.RDB$VIEW_SOURCE;
    -- именованный курсор
    DECLARE VARIABLE CUR_R CURSOR FOR (
      SELECT
        RDB$RELATION_NAME,
        RDB$VIEW_SOURCE
      FROM
        RDB$RELATIONS
      WHERE
        RDB$VIEW_SOURCE IS NOT NULL);
    -- Именованный курсор
    DECLARE CUR_F CURSOR FOR (
      SELECT
        RDB$FIELD_NAME
      FROM
        RDB$RELATION_FIELDS
      WHERE
        -- Важно! Переменная должна быть объявлена ранее
        RDB$RELATION_NAME = :RELATION);
  BEGIN
    OPEN CUR_R;
    WHILE (1 = 1) DO
    BEGIN
      FETCH CUR_R
        INTO :RELATION, :SOURCE;
      IF (ROW_COUNT = 0) THEN
        LEAVE;

      FIELDS = NULL;
      -- Курсор CUR_F использует
      -- значение переменной RELATION инициализированной ранее
      OPEN CUR_F;
      WHILE (1 = 1) DO
      BEGIN
        FETCH CUR_F
          INTO :FIELD_NAME;
        IF (ROW_COUNT = 0) THEN
          LEAVE;
        IF (FIELDS IS NULL) THEN
          FIELDS = TRIM(FIELD_NAME);
        ELSE
          FIELDS = FIELDS || ', ' || TRIM(FIELD_NAME);
      END
      CLOSE CUR_F;

      SCRIPT = 'CREATE VIEW ' || RELATION;

      IF (FIELDS IS NOT NULL) THEN
        SCRIPT = SCRIPT || ' (' || FIELDS || ')';

      SCRIPT = SCRIPT || ' AS ' || ASCII_CHAR(13);
      SCRIPT = SCRIPT || SOURCE;

      SUSPEND;
    END
    CLOSE CUR_R;
  END
  ```

  См. также: `FETCH`, `CLOSE`, `DECLARE ... CURSOR`.

To resume this session: kimi -r session_e0eedeed-2b55-4cd4-9ccb-a366c81bf4a9
