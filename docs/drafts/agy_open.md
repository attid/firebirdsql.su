# OPEN

## Доступно в
PSQL

## Формат
```sql
OPEN cursor_name;
```

## Описание
Оператор `OPEN` предназначен для открытия ранее объявленного курсора в процедурном коде PSQL. При выполнении оператора запускается ассоциированный с курсором оператор `SELECT`, формируя результирующий набор данных для последующего получения записей.

Оператор `OPEN` применим исключительно к курсорам, предварительно объявленным с помощью конструкции `DECLARE ... CURSOR`.

### Параметры
* `cursor_name` — имя открываемого курсора. Курсор с данным именем должен быть предварительно объявлен в текущем блоке кода.

### Особенности работы с параметрами
Если в операторе `SELECT`, привязанном к курсору, используются параметры (переменные), они должны быть предварительно объявлены как локальные переменные или как входные/выходные параметры до момента объявления самого курсора. При выполнении оператора `OPEN` параметрам запроса автоматически присваиваются текущие значения соответствующих переменных на момент открытия курсора.

## Пример

1. Использование оператора `OPEN` в хранимой процедуре:

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

2. Использование оператора `OPEN` с параметризованным курсором в блоке `EXECUTE BLOCK`:

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
