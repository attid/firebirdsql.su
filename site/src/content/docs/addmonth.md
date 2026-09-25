---
title: "ADDMONTH()"
old_id: addmonth
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ADDMONTH()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| + | + | + | + | + | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
ADDMONTH( TIMESTAMP, INTEGER )

## Описание
внешняя функция UDF идущая в комплекте с сервером 

добавляет заданное кол-во месяцев к первому аргументу

для того чтобы она была доступна надо её подключит к базе следующим запросом
```sql
DECLARE EXTERNAL FUNCTION ADDMONTH
    TIMESTAMP,
    INTEGER
RETURNS TIMESTAMP
ENTRY_POINT 'addMonth' MODULE_NAME 'fbudf';
```

## Пример
```sql
  select current_timestamp, addmonth(current_timestamp, 3) from rdb$database
```

## См. также
[ADDMILLISECOND()](/addmillisecond/) [ADDSECOND()](/addsecond/) [ADDMINUTE()](/addminute/) [ADDDAY()](/addday/) [ADDWEEK()](/addweek/) [ADDMONTH()](/addmonth/) [ADDYEAR()](/addyear/) 

## Источник
%firebird%\UDF\
