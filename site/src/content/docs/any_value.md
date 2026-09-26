---
title: "ANY_VALUE"
old_id: any_value
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "6.0"
  until: 
  deprecated: false
---

# ANY_VALUE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | − | − | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ANY_VALUE(expression)
```

## Описание
Агрегатная функция `ANY_VALUE` возвращает некоторое значение `expression` для группы строк. Функция недетерминирована: не гарантируется, какое именно значение из группы будет возвращено. Значения `NULL` игнорируются; `NULL` возвращается только если в группе нет ни одной записи с отличным от `NULL` значением.

Типичное применение — упрощение запросов с `GROUP BY`, когда в список выборки нужно включить столбцы, значения которых одинаковы внутри группы (например, зависящие от столбца группировки — первичного ключа). Стандарт SQL требует, чтобы все неагрегатные выражения из списка `SELECT` присутствовали в `GROUP BY`; оборачивание такого выражения в `ANY_VALUE` избавляет от группировки по дополнительным столбцам.

Раньше в тех же целях применялись `MIN` или `MAX`, однако `ANY_VALUE` дешевле: `MIN`/`MAX` требуют сравнения значений, тогда как `ANY_VALUE` просто возвращает первое попавшееся значение группы.

Функция появилась в Firebird 6.0 — версия в разработке, доступна в снапшот-сборках.

## Пример
`ANY_VALUE`, чтобы не добавлять `FIRST_NAME` и `LAST_NAME` в `GROUP BY` (`EMP_NO` — первичный ключ, сам обеспечивает уникальность сотрудника):

```sql
SELECT
  EMPLOYEE.EMP_NO,
  ANY_VALUE(EMPLOYEE.FIRST_NAME) AS FIRST_NAME,
  ANY_VALUE(EMPLOYEE.LAST_NAME) AS LAST_NAME,
  SUM(SALES.TOTAL_VALUE) AS TOTAL_SUM,
  COUNT(*) AS CNT
FROM
  SALES
  JOIN EMPLOYEE ON EMPLOYEE.EMP_NO = SALES.SALES_REP
GROUP BY 1;
```

Эквивалентный запрос без `ANY_VALUE` требует группировки по всем неагрегатным столбцам.

## См. также
[COALESCE](/coalesce/), [Встроенные функции по группам](/vstroennye_funkcii_po_gruppam/)

## Источник
Руководство по языку SQL СУБД Firebird 6.0 (sim1984 / ibase.ru, Public Documentation License)
