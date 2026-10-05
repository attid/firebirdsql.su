---
title: "PROCEDURE"
old_id: procedure
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# PROCEDURE

## Версии сервера
все

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
PROCEDURE

## Описание
PROCEDURE - зарезервированное слово SQL, служащее для обращения в работе с хранимыми процедурами.

## Пример
```sql
CREATE OR ALTER PROCEDURE PRO$POS (
    SUBSTR VARCHAR(100),
    STR VARCHAR(100))
RETURNS (
    POS INTEGER)
AS
DECLARE VARIABLE SUBSTR2 VARCHAR(201);
DECLARE VARIABLE TMP VARCHAR(100);
BEGIN
  IF (SubStr IS NULL OR Str IS NULL)
  THEN BEGIN Pos = NULL; EXIT; END

  SubStr2 = SubStr || '%';
  Tmp = '';
  Pos = 1;
  WHILE (Str NOT LIKE SubStr2 AND Str NOT LIKE Tmp) DO BEGIN
    SubStr2 = '_' || SubStr2;
    Tmp = Tmp || '_';
    Pos = Pos + 1;
  END

  IF (Str LIKE Tmp) THEN Pos = 0;

  SUSPEND;
END
```
```sql
SELECT POS from PRO$POS('e', 'test')
```
```sql
DROP PROCEDURE PRO$POS
```

## См. также
[CREATE PROCEDURE](/create_procedure/),  [DROP PROCEDURE](/drop_procedure/),  [ALTER PROCEDURE](/alter_procedure/)

## Источник
%Firebird%\doc\
