---
title: "LAST_DAY"
old_id: last_day
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# LAST_DAY

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
LAST_DAY(OF <period> FROM date_or_timestamp)

<period> ::= YEAR | QUARTER | MONTH | WEEK
```

| Параметр | Описание |
|---|---|
| `date_or_timestamp` | Выражение типа `DATE` или `TIMESTAMP [WITH \| WITHOUT] TIME ZONE` |

Тип результата: `DATE` или `TIMESTAMP` соответствующей разновидности.

## Описание
Функция `LAST_DAY` возвращает последний день указанного периода — года, квартала, месяца или недели — для заданной даты или отметки времени.

Тип результата соответствует типу аргумента. При передаче `TIMESTAMP` возвращаемое значение сохраняет временную часть исходной отметки.

Период задаётся ключевым словом после `OF`:

- `YEAR` — последний день года;
- `QUARTER` — последний день квартала;
- `MONTH` — последний день месяца;
- `WEEK` — последний день недели.

Обратите внимание: последним днём недели считается **суббота** — в соответствии с тем, что возвращает `EXTRACT` с частью `WEEKDAY`.

Функция удобна для вычисления границ отчётных периодов, дат окончания подписок, биллинга и других задач, где нужна дата конца периода, содержащего заданную дату. Обратная операция — `FIRST_DAY`.

## Пример
```sql
SELECT LAST_DAY(OF MONTH FROM current_date) FROM rdb$database;
SELECT LAST_DAY(OF YEAR FROM current_timestamp) FROM rdb$database;
SELECT LAST_DAY(OF WEEK FROM date '2017-11-01') FROM rdb$database;
```

## См. также
[FIRST_DAY](/first_day/), [EXTRACT](/extract/), [Математические операции с датой](/matematicheskie_operacii_s_datoj/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
