---
title: "DECLARE EXTERNAL FUNCTION"
old_id: declare_external_function
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DECLARE EXTERNAL FUNCTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Доступно в

[DSQL](/raznovidnosti_jazyka_sql/) [ESQL](/raznovidnosti_jazyka_sql/)

## Формат
```
DECLARE EXTERNAL FUNCTION localname
   [<type_decl> [, <type_decl> ...]]
   RETURNS {<return_type_decl> | PARAMETER 1-based_pos} [FREE_IT]
   ENTRY_POINT 'function_name' MODULE_NAME 'library_name'

<type_decl>         ::=  sqltype [BY DESCRIPTOR] | CSTRING(length)
<return_type_decl>  ::=  sqltype [BY {DESCRIPTOR|VALUE}] | CSTRING(length)
```
## Описание
DECLARE EXTERNAL FUNCTION создает внешнюю пользовательскую функцию (UDF). Локальное имя функции может быть выбрано любым; это имя под которым функция будет известна вашей базе данных. 

## Пример
```sql
DECLARE EXTERNAL FUNCTION MY_ROUND 
    DOUBLE PRECISION NULL, 
    INTEGER NULL 
    RETURNS DOUBLE PRECISION FREE_IT 
    ENTRY_POINT 'my_round' 
    MODULE_NAME 'my_lib';
```

## См. также
[ALTER EXTERNAL FUNCTION](/alter_external_function/), CSTRING, [Типы данных](/tipy_dannyx/)

## Источник
refdocs
