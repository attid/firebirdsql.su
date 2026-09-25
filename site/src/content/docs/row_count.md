---
title: "ROW_COUNT"
old_id: row_count
section: glossary
type: term
firebird:
  since: "2.0"
  until: 
  deprecated: false
---

# ROW_COUNT

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Да | Да | Да | Да | Да | ? |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
ROW_COUNT

## Описание
возвращает кол-во измененных или выбранных записей предыдущего запроса

может использоваться в процедурах и тригерах

⚠️ не может использоваться в [EXECUTE STATEMENT](/execute_statement/)

## Пример
```sql
execute block returns (result varchar(30))
as
declare variable vtest integer;
begin
  update rdb$functions fr
     set fr.rdb$function_name = fr.rdb$function_name
   where 1 = 1;
  result = 'Обновили '||row_count||' записей';
  suspend;

  update rdb$functions fr
     set fr.rdb$function_name = fr.rdb$function_name
   where fr.rdb$function_name = 'test';
  result = 'Обновили '||row_count||' записей';
  suspend;

  for select fr.rdb$function_type
        from rdb$functions fr
       where fr.rdb$function_name like 'RDB$%'
        into :vtest do
  begin
  end

  result = 'Получили '||row_count||' записей';
  suspend;
end
```

выводом будет что-то вроде 
Обновили 64 записей
Обновили 0 записей
Получили 2 записей

## Источник
Firebird_v1.5.3.ReleaseNotes.pdf 

Firebird_v2.0.0.ReleaseNotes.pdf
