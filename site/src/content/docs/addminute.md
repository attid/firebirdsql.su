---
title: "ADDMINUTE()"
old_id: addminute
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ADDMINUTE()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| + | + | + | + | + | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
addminute(timestamp,integer)

## Описание
внешняя функция UDF идущая в комплекте с сервером 

добавляет заданное кол-во минут к первому аргументу

для того чтобы она была доступна надо её подключит к базе следующим запросом
```sql
DECLARE EXTERNAL FUNCTION ADDMINUTE
    TIMESTAMP,
    INTEGER
RETURNS TIMESTAMP
ENTRY_POINT 'addMinute' MODULE_NAME 'fbudf';
```

## Пример
```sql
  select current_timestamp, addminute(current_timestamp, 3) from rdb$database
```

## См. также
[ADDMILLISECOND()](/addmillisecond/) [ADDSECOND()](/addsecond/) [ADDMINUTE()](/addminute/) [ADDDAY()](/addday/) [ADDWEEK()](/addweek/) [ADDMONTH()](/addmonth/) [ADDYEAR()](/addyear/) 

## Источник
%firebird%\UDF\
