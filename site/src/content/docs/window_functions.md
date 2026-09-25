---
title: "Оконные функции"
old_id: window_functions
section: groups
type: article
date: "2026-09-24"
firebird:
  since: "3.0"
  until: 
  deprecated: false
---

# Оконные функции

Оконные функции (их ещё называют аналитическими) — это, по сути, агрегатные функции, которые не уменьшают степень детализации выборки. Обычная агрегация с `GROUP BY` «схлопывает» строки группы в одну: на входе сто строк продаж, на выходе — по одной строке на регион. Оконная функция считает то же самое агрегатное значение, но строки никуда не деваются: рядом с каждой исходной строкой выводится, например, сумма по её группе, её место в рейтинге или значение из соседней строки.

Появлялись они в Firebird в два этапа. В Firebird 3.0 механизм `OVER` получили агрегатные функции — обычные `SUM`, `COUNT`, `AVG` и компания научились работать «в оконном режиме». А в Firebird 4.0 добавились собственно оконные функции: ранжирующие (`RANK`, `DENSE_RANK`, `ROW_NUMBER` и другие) и навигационные (`LAG`, `LEAD`, `FIRST_VALUE` и другие).

Синтаксически отличие простое: после имени функции всегда следует `OVER(...)`. Оконные функции могут находиться только в списке `SELECT` и в предложении `ORDER BY`.

## Синтаксис OVER

```
<window_function> ::=
    <aggregate_function> OVER <window_name_or_spec>
  | <window_function_name> ([<expr> [, <expr> ...]]) OVER <window_name_or_spec>

<window_name_or_spec> ::=
  <window_specification> | window_name

<window_specification> ::=
  ( [window_name] [<window partition>] [<window order>] [<window frame>] )

<window partition> ::= PARTITION BY <expr> [, <expr> ...]

<window order> ::=
  ORDER BY <expr> [<direction>] [<nulls placement>]
        [, <expr> [<direction>] [<nulls placement>] ...]

<window frame> ::=
  {RANGE | ROWS} <window frame extent>

<window frame extent> ::=
  <window frame start> | <window frame between>

<window frame start> ::=
  UNBOUNDED PRECEDING | <expr> PRECEDING | CURRENT ROW

<window frame between> ::=
  BETWEEN {UNBOUNDED PRECEDING | <expr> PRECEDING | <expr> FOLLOWING | CURRENT ROW}
      AND {UNBOUNDED FOLLOWING | <expr> PRECEDING | <expr> FOLLOWING | CURRENT ROW}
```

Пустые скобки `OVER()` тоже допустимы — тогда окном считается весь набор строк.

## Разбиение на секции (PARTITION BY)

`PARTITION BY` делит набор строк на секции — группы строк с одинаковыми значениями выражений разбивки. Оконная функция вычисляется независимо внутри каждой секции: на её границе накопленные суммы обнуляются, нумерация начинается заново.

```sql
SELECT
    REGION,
    CITY,
    POPULATION,
    SUM(POPULATION) OVER (PARTITION BY REGION) AS REGION_TOTAL
FROM CITIES;
```

Здесь в каждой строке города выводится суммарное население его региона — без всякого `GROUP BY` и без потери строк. Если `PARTITION BY` не указан, весь результат запроса считается одной секцией.

## Сортировка (ORDER BY) внутри окна

`ORDER BY` внутри `OVER` задаёт порядок строк в секции. Он нужен в двух случаях:

- для ранжирующих и навигационных функций порядок определяет сам смысл вычисления — кто первый, кто следующий, кто предыдущий;
- для агрегатов сортировка включает нарастающий итог: меняется рамка окна по умолчанию (об этом ниже).

```sql
SELECT
    EMP_NO,
    LAST_NAME,
    SALARY,
    RANK() OVER (ORDER BY SALARY DESC) AS SALARY_RANK
FROM EMPLOYEE;
```

Сортировка внутри окна не зависит от итогового `ORDER BY` запроса: первый определяет, как считается функция, второй — в каком порядке вы увидите строки. Для каждого ключа сортировки можно указать направление `ASC`/`DESC` и размещение `NULL`: `NULLS FIRST` или `NULLS LAST`.

## Рамка окна

Рамка окна — это набор строк внутри секции, который реально участвует в вычислении для текущей строки. Рамка задаётся только вместе с `ORDER BY` внутри `OVER` и описывается единицей (`ROWS` или `RANGE`) и границами: `UNBOUNDED PRECEDING`, `<expr> PRECEDING`, `CURRENT ROW`, `<expr> FOLLOWING`, `UNBOUNDED FOLLOWING`.

Разница между единицами:

- `ROWS` — рамка отсчитывает физические строки: «текущая строка и две предыдущие»;
- `RANGE` — рамка ограничивается логически, по диапазону значений ключа сортировки относительно значения текущей строки.

Если рамка не указана, действует умолчание:

- без `ORDER BY` — рамка охватывает все строки секции;
- с `ORDER BY` — `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, то есть все строки от начала секции до текущей, плюс следующие строки, равные ей по ключу сортировки. Именно это умолчание превращает `SUM(...) OVER (ORDER BY ...)` в нарастающий итог.

Пример со скользящей суммой по трём строкам:

```sql
SELECT
    SALE_DATE,
    AMOUNT,
    SUM(AMOUNT) OVER (
        ORDER BY SALE_DATE
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS MOVING_SUM
FROM SALES;
```

## Именованные окна

Если одна и та же спецификация окна нужна нескольким функциям, её не обязательно повторять в каждом `OVER`. Предложение `WINDOW` в конце запроса (после `HAVING`, перед итоговым `ORDER BY`) позволяет дать окну имя и ссылаться на него:

```sql
SELECT
    REGION,
    CITY,
    POPULATION,
    SUM(POPULATION) OVER w AS REGION_TOTAL,
    RANK() OVER w AS POP_RANK
FROM CITIES
WINDOW w AS (PARTITION BY REGION ORDER BY POPULATION DESC)
ORDER BY REGION, POP_RANK;
```

## Список функций

Две группы: обычные агрегатные функции, умеющие работать с `OVER` (с Firebird 3.0), и собственно оконные функции (с Firebird 4.0) — ранжирующие и навигационные.

| Функция | Группа | Что делает |
|---|---|---|
| `SUM`, `COUNT`, `AVG`, `MIN`, `MAX` и другие агрегатные | Агрегатные с `OVER` | Считают агрегат по секции или рамке окна, не схлопывая строки |
| `RANK()` | Ранжирующая | Ранг строки с учётом равенства значений; после равных рангов — пропуск номеров (1, 2, 2, 4) |
| `DENSE_RANK()` | Ранжирующая | То же, но без пропусков (1, 2, 2, 3) |
| `PERCENT_RANK()` | Ранжирующая | Относительный ранг строки в секции от 0 до 1 |
| `CUME_DIST()` | Ранжирующая | Накопленное распределение: доля строк секции, не превосходящих текущую |
| `NTILE(n)` | Ранжирующая | Делит секцию на `n` примерно равных групп и возвращает номер группы |
| `ROW_NUMBER()` | Ранжирующая | Порядковый номер строки в секции, без учёта равенства значений |
| `FIRST_VALUE(expr)` | Навигационная | Значение выражения из первой строки рамки окна |
| `LAST_VALUE(expr)` | Навигационная | Значение выражения из последней строки рамки окна |
| `LAG(expr)` | Навигационная | Значение выражения из предыдущей строки секции |
| `LEAD(expr)` | Навигационная | Значение выражения из следующей строки секции |
| `NTH_VALUE(expr, n)` | Навигационная | Значение выражения из n-й строки рамки окна |

## Пример

Представим таблицу продаж менеджеров `SALES(SELLER, SALE_MONTH, AMOUNT)`. Одним запросом посмотрим на каждую продажу сразу в нескольких разрезах: нарастающий итог менеджера, дельта к предыдущему месяцу, место продажи в личном рейтинге и доля в общем обороте месяца.

```sql
SELECT
    SELLER,
    SALE_MONTH,
    AMOUNT,

    -- нарастающий итог по менеджеру
    SUM(AMOUNT) OVER (
        PARTITION BY SELLER
        ORDER BY SALE_MONTH
    ) AS RUNNING_TOTAL,

    -- сколько было в прошлом месяце у этого же менеджера
    AMOUNT - LAG(AMOUNT) OVER (
        PARTITION BY SELLER
        ORDER BY SALE_MONTH
    ) AS DIFF_PREV_MONTH,

    -- место этой продажи среди всех продаж менеджера
    DENSE_RANK() OVER (
        PARTITION BY SELLER
        ORDER BY AMOUNT DESC
    ) AS PERSONAL_RANK,

    -- доля продажи в общем обороте месяца
    ROUND(
        100.0 * AMOUNT / SUM(AMOUNT) OVER (PARTITION BY SALE_MONTH),
        2
    ) AS PCT_OF_MONTH
FROM SALES
ORDER BY SELLER, SALE_MONTH;
```

Обратите внимание: `GROUP BY` здесь нет вообще, а строки результата совпадают по числу со строками исходной таблицы. Каждая оконная функция живёт в своей «системе координат»: нарастающий итог и `LAG` движутся по календарю внутри менеджера, ранг сортирует те же строки по сумме, а доля считается по совсем другой секции — по месяцу. Попробуйте переписать это на классических агрегатах и самосоединениях — и разница в выразительности станет очевидной.

## См. также
[Встроенные функции](/vstroennye_funkcii/), [Встроенные функции по группам](/vstroennye_funkcii_po_gruppam/), [SELECT](/select/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
