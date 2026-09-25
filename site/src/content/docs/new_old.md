---
title: "NEW, OLD"
old_id: new_old
section: glossary
type: term
firebird:
  since: "1.5.3"
  until: 
  deprecated: false
---

# NEW, OLD

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
NEW.< имя столбца >
OLD.< имя столбца >
```

## Описание
Контекстные псевдообъектные переменные NEW и OLD доступны <u>только</u> внутри текста триггеров и служат для обращения соответственно к новым и к старым значениям столбцов записи через точечную нотацию.

## Пример
Следующий пример показывает, как при помощи контекстной переменной NEW организовывается автоинкрементное значение первичного ключа ID таблицы MYTABLE.
```sql
SET TERM !!!;

CREATE TRIGGER MYTABLE_BI_000 FOR MYTABLE
ACTIVE BEFORE INSERT POSITION 0
AS
BEGIN
  IF (NEW.ID IS NULL) THEN
    NEW.ID = GEN_ID(GENR_MYTABLE_ID, 1);
END
!!!

SET TERM; !!!
```

Следующий пример заставляет при изменении значения столбца FLAG выполнять процедуру MY_PROC
```sql
SET TERM !!!;

CREATE TRIGGER MYTABLE_BU_010 FOR MYTABLE
ACTIVE BEFORE UPDATE POSITION 10
AS
BEGIN
  IF (NEW.FLAG <> OLD.FLAG) THEN
    EXECUTE PROCEDURE MYPROC(NEW.FLAG);
END
!!!

SET TERM; !!!
```

## См. также
[GEN_ID()](/gen_id/), [INSERTING, UPDATING, DELETING](/inserting_updating_deleting/), [SET TERM](/set_term/), [CREATE TRIGGER](/create_trigger/), [ALTER TRIGGER](/alter_trigger/)

## Источник
