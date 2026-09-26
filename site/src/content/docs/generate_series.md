---
title: "GENERATE_SERIES"
old_id: generate_series
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "6.0"
  until: 
  deprecated: false
---

# GENERATE_SERIES

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | − | − | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
<generate_series_function> ::=
    GENERATE_SERIES(<start>, <finish> [, <step>])
    [AS] <correlation name> [ ( <derived column name> ) ]
```

## Описание
Функция `GENERATE_SERIES` создаёт ряд чисел в заданном интервале. Интервал и шаг между значениями определяются пользователем.

Параметры:

- `start` — начальное значение интервала. Переменная, литерал или скалярное выражение типов `SMALLINT`, `INTEGER`, `BIGINT`, `INT128` или `NUMERIC/DECIMAL`;
- `finish` — конечное значение интервала. Генерация останавливается, когда последнее значение шага превышает (или становится меньше, при отрицательном `step`) значение `finish`;
- `step` — шаг между значениями. Может быть положительным и отрицательным, но не нулём. Необязателен, по умолчанию 1.

Функция возвращает набор данных со столбцом типа `BIGINT`, `INT128` или `NUMERIC(18, x)`/`NUMERIC(38, x)` — масштаб определяется максимальным из масштабов аргументов.

Правила:

- если `start < finish` и `step` отрицательный — возвращается пустой набор;
- если `start > finish` и `step` положительный — возвращается пустой набор;
- если `step` равен нулю — возникает ошибка.

Непосредственное указание `GENERATE_SERIES` в качестве столбца в `SELECT` запрещено: запрос `SELECT GENERATE_SERIES FROM GENERATE_SERIES(1, 3) AS S` вызовет ошибку «столбец GENERATE_SERIES не существует». При этом `SELECT * FROM GENERATE_SERIES(1, 3) AS S` отработает, и столбец будет называться `GENERATE_SERIES`.

Функция появилась в Firebird 6.0 — версия находится в разработке, доступна в снапшот-сборках.

## Пример
```sql
SELECT n
FROM GENERATE_SERIES(1, 3) AS S(n);
-- 1, 2, 3

SELECT n
FROM GENERATE_SERIES(3, 1, -1) AS S(n);
-- 3, 2, 1

-- Разбиение часа на минутные интервалы
SELECT
    DATEADD(n MINUTE TO timestamp '2025-01-01 12:00') AS start_time,
    DATEADD(n MINUTE TO timestamp '2025-01-01 12:00:59.9999') AS finish_time
FROM GENERATE_SERIES(0, 59) AS S(n);
```

## См. также
[Встроенные функции по группам](/vstroennye_funkcii_po_gruppam/), [Типы данных](/tipy_dannyx/)

## Источник
Руководство по языку SQL СУБД Firebird 6.0 (sim1984 / ibase.ru, Public Documentation License)
