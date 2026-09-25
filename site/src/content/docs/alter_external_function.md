---
title: "ALTER EXTERNAL FUNCTION"
old_id: alter_external_function
section: glossary
type: term
firebird:
  since: "2.0"
  until: 
  deprecated: false
---

# ALTER EXTERNAL FUNCTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Да | Да | Да | Да | ? | ? |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ALTER EXTERNAL FUNCTION funcname
   <modification> [<modification>]

<modification>  ::=  ENTRY_POINT 'new-entry-point'
                     | MODULE_NAME 'new-module-name'
```
## Описание
Изменяет имя модуля внешней функции и/или точку входа. Существующие зависимости при этом сохраняются.

## Пример
```sql
ALTER EXTERNAL FUNCTION MY_ROUND  
    MODULE_NAME 'my_other_lib';
```

## См. также
[DECLARE EXTERNAL FUNCTION](/declare_external_function/)

## Источник
refdocs
