---
title: "INSERTING, UPDATING, DELETING"
old_id: inserting_updating_deleting
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# INSERTING, UPDATING, DELETING

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
INSERTING
UPDATING
DELETING
```

## Описание
Псевдологические переменные INERTING, UPDATING, DELETING доступны <u>только</u> внутри текста триггеров и служат для определения текущего контекста действия триггера. Эти переменные могут быть полезны для триггеров, вызываемых одновременно при вставке, изменении или удалении данных.

## Пример
Следующий пример показывает, как вести учет версии записи при помощи триггера перед вставкой или изменением записи. В момент вставки записи начальное значение домена VERSION_NUMBER таблицы VERSIONEDTABLE инициализируется нулем. Затем, при последующих изменениях записи, новое значение домена получается инкрементом старого.
```sql
SET TERM !!!;

CREATE TRIGGER SET_VERSION_NUMBER_BIU_0 FOR VERSIONEDTABLE
ACTIVE BEFORE INSERT OR UPDATE POSITION 0
AS
BEGIN
  IF (INSERTING) THEN
    NEW.VERSION_NUMBER = 0;
  ELSE
    IF (UPDATING) THEN
      NEW.VERSION_NUMBER = OLD.VERSION_NUMBER + 1;
END
!!!

SET TERM; !!!
```

## См. также
[OLD](/new_old/), [NEW](/new_old/), [SET TERM](/set_term/), [CREATE TRIGGER](/create_trigger/), [ALTER TRIGGER](/alter_trigger/), RDB$TRIGGERS

## Источник
Firebird 1.5 Release Notes
