---
title: "IF"
old_id: if
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# IF

## Версии сервера
все

## Доступно в
PSQL

## Формат
1) Полный формат оператора
```sql
IF (<condition>)THEN
BEGIN
  ....
  <operators1>
  ....
END
ELSE
BEGIN
  ....
  <operators2>
  ....
END
```
2) сокращенный формат оператора
```sql
IF (<condition>)THEN
BEGIN
  ....
  <operators1>
  ....
END
```
3) В случае наличия одного оператора, следующего в ветвлении алгоритма, операторные скобки BEGIN … END можно опустить.
```sql
IF (<condition>)THEN
  <operator1>;
ELSE
  <operator2>;
```
## Описание
Оператор условного перехода IF подмножества PSQL служит для организации ветвления алгоритмов триггеров и хранимых процедур.
Если условие <condition> истинно, то выполняется <operator1>, иначе <operator2>.
## Пример
1. Использование в триггере.
```sql
CREATE OR ALTER TRIGGER TRIGG_MYTABLE_BIU_10 FOR MYTABLE 
ACTIVE BEFORE INSERT OR UPDATE POSITION 10
AS
BEGIN
  IF (NEW.ID IS NULL) THEN
    NEW.ID = GEN_ID(MY_GENERATOR, 1);
  IF INSERTING THEN
  BEGIN
    NEW.DATE_INS = CURRENT_TIMESTAMP;
    NEW.USER_INS = CURRENT_USER;
  END
  ELSE
  BEGIN
    NEW.DATE_UPD = CURRENT_TIMESTAMP;
    NEW.USER_UPD = CURRENT_USER;
  END
END
```
2. Использование в хранимой процедуре.
```sql
CREATE OR ALTER PROCEDURE MY_PROC(
  GROUP_ID INTEGER
)RETURNS(
   ID   INTEGER
  ,NAME VARCHAR(255)
)AS
BEGIN
  FOR
    SELECT TB.ID, TB.NAME
    FROM   MYTABLE TB
    WHERE  ((TB.GROUP_ID+0) = :GROUP_ID)
    INTO   :ID, :NAME
  DO
    IF (:ID > 10000) THEN
    BEGIN
      ID = :ID - 10000;
      SUSPEND;
    END
END
```
## См. также
FOR, [WHILE](/while/), SUSPEND, INSERTING, UPDATING
## Источник
