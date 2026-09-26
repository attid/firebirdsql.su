---
title: "FIRST_DAY"
old_id: first_day
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# FIRST_DAY

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
FIRST_DAY(OF <period> FROM date_or_timestamp)

<period> ::= YEAR | QUARTER | MONTH | WEEK
```

| Параметр | Описание |
|---|---|
| `date_or_timestamp` | Выражение типа `DATE` или `TIMESTAMP [WITH \| WITHOUT] TIME ZONE` |

Тип результата: `DATE` или `TIMESTAMP` соответствующей разновидности.

## Описание
Функция `FIRST_DAY` возвращает первый день периода — года, квартала, месяца или недели, — которому принадлежит заданная дата или отметка времени. Период задаётся ключевым словом после `OF`: `YEAR`, `QUARTER`, `MONTH` или `WEEK`.

Тип результата совпадает с типом аргумента: для `DATE` возвращается `DATE`, для `TIMESTAMP` — `TIMESTAMP` соответствующей разновидности (с часовым поясом или без). Если аргумент — `TIMESTAMP`, возвращаемое значение сохраняет временную часть: сдвигается только дата.

При вычислении первого дня недели (`WEEK`) первым днём считается **воскресенье**, в соответствии с тем, что возвращает `EXTRACT` с частью `WEEKDAY`. В локалях, где неделя начинается с понедельника, результат может отличаться от ожидаемого.

Функция удобна для группировки и агрегирования по календарным периодам, построения отчётов и вычисления границ интервалов. Обратная операция — `LAST_DAY`.

## Пример
```sql
-- Первый день текущего месяца
SELECT FIRST_DAY(OF MONTH FROM current_date) FROM rdb$database;

-- Первый день недели (воскресенье) для заданной даты
SELECT FIRST_DAY(OF WEEK FROM date '2017-11-01') FROM rdb$database;

-- Первый день квартала с сохранением времени
SELECT FIRST_DAY(OF QUARTER FROM timestamp '2026-09-24 14:30:00') FROM rdb$database;
```

## См. также
[LAST_DAY](/last_day/), [EXTRACT](/extract/), [Математические операции с датой](/matematicheskie_operacii_s_datoj/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
