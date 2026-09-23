---
title: "EXECUTE BLOCK"
old_id: execute_block
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# EXECUTE BLOCK

## Версии сервера
Firebird 2.0 

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
EXECUTE BLOCK [ (inparam datatype = :<название параметра>, …) ]
[ RETURNS (outparam datatype, …) }
AS
[DECLARE VARIABLE varparam datatype; …]
BEGIN
…
END

inparam - входящие параметры

outparam - исходящие параметры

varparam - переменые доступные внутри блока

datatype - [тип данных](/tipy_dannyx/)

## Описание
функция позволяет выполнять набор [PSQL](/raznovidnosti_jazyka_sql/) команд без создания процедуры.

Поддерживает как входные так и выходные параметры.

## Пример
```sql
execute block returns (result varchar(30))
AS
declare variable vtest integer;
begin
  UPDATE rdb$functions fr
     SET fr.rdb$function_name = fr.rdb$function_name
   WHERE 1 = 1;
  result = 'Обновили '||row_count||' записей';
  suspend;
 
  UPDATE rdb$functions fr
     SET fr.rdb$function_name = fr.rdb$function_name
   WHERE fr.rdb$function_name = 'test';
  result = 'Обновили '||row_count||' записей';
  suspend;
 
  FOR SELECT fr.rdb$function_type
        FROM rdb$functions fr
       WHERE fr.rdb$function_name LIKE 'RDB$%'
        INTO :vtest do
  begin
  end
 
  result = 'Получили '||row_count||' записей';
  suspend;
end
```

Или

```sql
execute block (pass1 varchar(255) = :pass1)
as
begin
  if (exists (select id from toptions2 where name = 'dbpass')) then
    update TOPTIONS2 set val = :pass1 where name = 'dbpass';
  else
    insert into TOPTIONS2 (name,  val) values ('dbpass', :pass1);
end
```
## Источник
\doc\sql.extensions\README.execute_block.txt
