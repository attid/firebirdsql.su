---
title: "CURRENT_DATE"
old_id: current_date
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CURRENT_DATE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/), [ISQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

CURRENT_DATE

## Описание
Контекстная переменная возвращает текущую дату.

## Пример
```sql
SELECT CURRENT_DATE FROM RDB$DATABASE
```

## Смотри также
[CURRENT_TIMESTAMP](/current_timestamp/)

## Источник
2.0 Release Notes

($firebird)/doc/sql.extensions/README.current_time.txt
