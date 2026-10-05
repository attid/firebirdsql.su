---
title: "DATEADD()"
old_id: dateadd
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DATEADD()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
DATEADD( <number> <timestamp_part> TO <date_time> ) или 
DATEADD( <timestamp_part>, <number>, <date_time> )

,где timestamp_part ::= { YEAR | MONTH | DAY | HOUR | MINUTE | SECOND | MILLISECOND }

⚠️ 
  1. <timestamp_part> равное YEAR, MONTH или DAY не может быть использовано с типом time.
  1. HOUR, MINUTE, SECOND или MILLISECOND не может быть использовано с типом date.

## Описание
Возвращает величину типа [DATE](/tipy_dannyx/), [TIME](/tipy_dannyx/) или [TIMESTAMP](/tipy_dannyx/), увеличенную (или уменьшенную, в случае <number> меньше нуля) на заданное количество единиц времени.

## Пример
```sql
  SELECT DATEADD(DAY, -1, current_date) AS yesterday FROM rdb$database;
```

или

```sql
  SELECT DATEADD(-1 DAY TO current_date) AS yesterday FROM rdb$database;
```

## См. также
[DATEDIFF()](/datediff/),
[matematicheskie_operacii_s_datoj](/matematicheskie_operacii_s_datoj/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
