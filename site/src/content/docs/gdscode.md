---
title: "GDSCODE"
old_id: gdscode
section: glossary
type: term
firebird:
  since: "1.5.3"
  until: 
  deprecated: false
---

# GDSCODE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
GDSCODE
```

## Описание
GDSCODE возвращает внутри [PSQL](/raznovidnosti_jazyka_sql/)-блока, хранимой процедуры или триггера код ошибки Firebird. Конструкция введена с целью обработки ошибок выполнения [PSQL](/raznovidnosti_jazyka_sql/)-блоков.

Если никакой ошибки не произошло, GDSCODE возвращает 0.

Вместо числовых значений GDSCODE можно использовать соответствующие им литералы.

## Пример
```sql
WHEN GDSCODE 335544551, GDSCODE 335544552,
     GDSCODE 335544553, GDSCODE 335544707 
DO
BEGIN
  EXECUTE PROCEDURE SOME_PROC(GDSCODE);
  EXIT;
END
```

или

```sql
WHEN GDSCODE grant_obj_notfound, GDSCODE grant_fld_notfound,
     GDSCODE grant_nopriv, GDSCODE grant_nopriv_on_base 
DO
BEGIN
  EXECUTE PROCEDURE SOME_PROC(GDSCODE);
  EXIT;
END
```

## См. также
[WHEN](/when/),  SQLCODE, [GDSCODES](/gdscodes/)

## Источник
2008-07-09 
http://www.firebirdsql.org/refdocs/langrefupd15-gdscode.html
