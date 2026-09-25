---
title: "WITH [RECURSIVE]"
old_id: recursive
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# WITH [RECURSIVE]

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | ? |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
WITH [RECURSIVE]
 CTE_A [(a1, a2, …)]
 AS ( SELECT … ),
 CTE_B [(b1, b2, …)]
 AS ( SELECT … ),
...
SELECT ...
  FROM CTE_A, CTE_B, TAB1, TAB2 ...
 WHERE ...
```

## Описание
Общие табличные выражения (Common Table Expressions), сокращённо CTE, описаны как виртуальные таблицы или представления, определённые в преамбуле основного. Операторы DML запроса, которые участвуют в основном запросе. Основной запрос может ссылаться на любое CTE из определённых в преамбуле, как и при выборке данных из обычных таблиц или представлений. CTE могут быть рекурсивными, т.е. ссылающимися сами на себя, но не могут быть вложенными.
Лимит на глубину рекурсии установлен в 1024.

## Пример
Без рекурсии:
```sql
  WITH
  DEPT_YEAR_BUDGET AS (
    SELECT FISCAL_YEAR, DEPT_NO,
        SUM(PROJECTED_BUDGET) AS BUDGET
      FROM PROJ_DEPT_BUDGET
    GROUP BY FISCAL_YEAR, DEPT_NO
  )
SELECT D.DEPT_NO, D.DEPARTMENT,
  B_1993.BUDGET AS B_1993, B_1994.BUDGET AS B_1994,
       B_1995.BUDGET AS B_1995, B_1996.BUDGET AS B_1996
  FROM DEPARTMENT D
    LEFT JOIN DEPT_YEAR_BUDGET B_1993
      ON D.DEPT_NO = B_1993.DEPT_NO
      AND B_1993.FISCAL_YEAR = 1993
    LEFT JOIN DEPT_YEAR_BUDGET B_1994
      ON D.DEPT_NO = B_1994.DEPT_NO
      AND B_1994.FISCAL_YEAR = 1994
    LEFT JOIN DEPT_YEAR_BUDGET B_1995
      ON D.DEPT_NO = B_1995.DEPT_NO
      AND B_1995.FISCAL_YEAR = 1995
    LEFT JOIN DEPT_YEAR_BUDGET B_1996
      ON D.DEPT_NO = B_1996.DEPT_NO
      AND B_1996.FISCAL_YEAR = 1996
  WHERE EXISTS (
    SELECT * FROM PROJ_DEPT_BUDGET B
    WHERE D.DEPT_NO = B.DEPT_NO)          
```

с рекурсией:
```sql
WITH RECURSIVE
  DEPT_YEAR_BUDGET AS
  (
    SELECT FISCAL_YEAR, DEPT_NO,
        SUM(PROJECTED_BUDGET) AS BUDGET
      FROM PROJ_DEPT_BUDGET
    GROUP BY FISCAL_YEAR, DEPT_NO
  ),

  DEPT_TREE AS
  (
    SELECT DEPT_NO, HEAD_DEPT, DEPARTMENT,
        CAST('' AS VARCHAR(255)) AS INDENT
      FROM DEPARTMENT
     WHERE HEAD_DEPT IS NULL

    UNION ALL

    SELECT D.DEPT_NO, D.HEAD_DEPT, D.DEPARTMENT,
    H.INDENT || '  '
      FROM DEPARTMENT D
      JOIN DEPT_TREE H
        ON D.HEAD_DEPT = H.DEPT_NO
  )

  SELECT D.DEPT_NO,
 D.INDENT || D.DEPARTMENT AS DEPARTMENT,
 B_1993.BUDGET AS B_1993,
 B_1994.BUDGET AS B_1994,
 B_1995.BUDGET AS B_1995,
 B_1996.BUDGET AS B_1996

  FROM DEPT_TREE D
    LEFT JOIN DEPT_YEAR_BUDGET B_1993
      ON D.DEPT_NO = B_1993.DEPT_NO
      AND B_1993.FISCAL_YEAR = 1993
    LEFT JOIN DEPT_YEAR_BUDGET B_1994
      ON D.DEPT_NO = B_1994.DEPT_NO
      AND B_1994.FISCAL_YEAR = 1994
    LEFT JOIN DEPT_YEAR_BUDGET B_1995
      ON D.DEPT_NO = B_1995.DEPT_NO
      AND B_1995.FISCAL_YEAR = 1995
    LEFT JOIN DEPT_YEAR_BUDGET B_1996
      ON D.DEPT_NO = B_1996.DEPT_NO
      AND B_1996.FISCAL_YEAR = 1996
```

еще один пример с рекурсией: 
```sql
with recursive temp(n, f1, f2, f3, f4) as
(select 0, 1, 2, 3, 4
 from rdb$database
 union all
 select n+1, 1, 2, 3, 4
 from temp
 where n < 10)

Select * from temp
```
## См. также

## Источник
Firebird 2.1 Release Notes 14 April 2008 - Document v. 0210_53
