---
title: "DATEDIFF()"
old_id: datediff
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DATEDIFF()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
DATEDIFF(<timestamp_part> FROM <date_time1> TO <date_time2>)
или
DATEDIFF(<timestamp_part>, <date_time1>, <date_time2>)

,где timestamp_part ::= { YEAR | MONTH | DAY | HOUR | MINUTE | SECOND | MILLISECOND }

## Описание
Возвращает разницу между <date_time1> и <date_time2> в выбранных единицах времени.

Если <date_time2> больше (позднее) <date_time1>, то результат положительный.

Если <date_time2> меньше <date_time1>, то результат отрицательный.

Если <date_time1> равно <date_time2>, то результат нулевой.

## Пример
```sql
  SELECT DATEDIFF(DAY, (CAST('TOMORROW' as date) -10), current_date) AS datediffresult FROM rdb$database;
```

## См. также
[DATEADD()](/dateadd/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
