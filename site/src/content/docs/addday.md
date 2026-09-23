---
title: "ADDDAY()"
old_id: addday
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ADDDAY()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| + | + | + | + | + | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
ADDDAY(timestamp,integer)

## Описание
внешняя функция UDF идущая в комплекте с сервером 

добавляет заданное кол-во дней к первому аргументу

для того чтобы она была доступна надо её подключит к базе следующим запросом

В версии 2.1 и выше эквивалентно конструкции DATEADD(DAY, integer, timestamp)

## Пример
```sql
  select current_timestamp, addday(current_timestamp, 3) from rdb$database
```

## См. также
[ADDMILLISECOND()](/addmillisecond/) [ADDSECOND()](/addsecond/) [ADDMINUTE()](/addminute/) [ADDDAY()](/addday/) [ADDWEEK()](/addweek/) [ADDMONTH()](/addmonth/) [ADDYEAR()](/addyear/) 

[DATEADD()](/dateadd/) [DATEDIFF()](/datediff/)

## Источник
%firebird%\UDF\
