# FIRST_DAY

## Доступно в
DSQL, PSQL

## Формат
```
FIRST_DAY(OF <period> FROM date_or_timestamp)

<period> ::= YEAR | QUARTER | MONTH | WEEK
```

## Описание
Скалярная функция `FIRST_DAY` предназначена для вычисления начальной даты заданного временного интервала (`YEAR`, `QUARTER`, `MONTH` или `WEEK`) для переданной даты или временной метки.

Входной параметр `date_or_timestamp` принимает выражение типа `DATE` либо `TIMESTAMP [WITH | WITHOUT] TIME ZONE`. Возвращаемый результат имеет тот же тип данных, что и переданный аргумент (`DATE` или `TIMESTAMP [WITH | WITHOUT] TIME ZONE`). Функция определяет дату первого дня года, квартала, месяца или недели, в которую попадает переданное значение.

Ключевые особенности работы функции:
- Если в качестве аргумента передаётся выражение типа `TIMESTAMP` (с указанием часового пояса или без него), возвращаемое значение полностью сохраняет исходную временную часть.
- Первым днём недели при вычислении периода `WEEK` считается воскресенье, что согласуется с поведением функции `EXTRACT` при извлечении части `WEEKDAY`.

## Пример
```sql
-- Получение первого дня текущего месяца и первого дня года с сохранением времени
SELECT 
    FIRST_DAY(OF MONTH FROM CURRENT_DATE) AS first_month_day,
    FIRST_DAY(OF YEAR FROM CURRENT_TIMESTAMP) AS first_year_day
FROM RDB$DATABASE;

-- Определение первого дня недели (воскресенья) для заданной даты
SELECT FIRST_DAY(OF WEEK FROM DATE '2017-11-01') AS first_week_day
FROM RDB$DATABASE;
```
