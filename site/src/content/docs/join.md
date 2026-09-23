---
title: "JOIN"
old_id: join
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# JOIN
Данная статья уточняет правило <joined table> из статьи [SELECT](/select/)

## Версии сервера
|  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  | **0.9** | **1.0** | **1.5.3** | **1.5.4** | **1.5.5** | **2.0** | **2.0.3** | **2.0.4** | **2.1** | **2.5** | **3.0** |
| **INNER, OUTER** | + | + | + | + | + | + | + | + | + | + | + |
| **CROSS** | - | - | - | - | - | + | + | + | + | + | + |
| **NATURAL, USING** | - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
<joined table> ::= 
  { <cross_join> | <qualified_join> | <named_columns_join> | <natural_join>}
```

```
<cross_join> ::= 
  <reference_expression_list> CROSS JOIN <reference_expression_list>
```

```
<qualified_join> ::=
  <reference_expression_list> <join type> JOIN <reference_expression_list>
    ON <join condition>
```

```
<named_columns_join> ::=
  <reference_expression_list> <join type> JOIN <reference_expression_list>
    USING ( <column list> )
```

```
<natural_join> ::=
  <reference_expression_list> NATURAL <join type> JOIN <table primary>
```

```
<join type> ::=
  [{INNER | {LEFT | RIGHT | FULL} [OUTER]}]
```

## Описание
Далее во всех примерах в качестве <reference_expression_list> будут использоваться следующие две таблицы:
```sql
CREATE TABLE A( A INT, B INT, C INT);
CREATE TABLE B( A INT, B INT, D INT);
```
A
| A | B | C |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 2 | 2 |
B
| A | B | D |
|---|---|---|
| 1 | 0 | 3 |
| 2 | 2 | 4 |

# <qualified_join>
"Обычное" соединение. Подразделяется на 4 типа (<join type>):
  1. Внутреннее (INNER JOIN)
  1. Внешнее Левое (LEFT OUTER JOIN)
  1. Внешнее Правое (RIGHT OUTER JOIN)
  1. Внешнее Полное (FULL OUTER JOIN)

Внутреннее
Из таблиц выделяются все возможные пары, для которых условие соединения <join condition> истинно
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A INNER JOIN B ON A.B <= B.B
```
Эквивалентно неявному соединению: 
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A, B 
WHERE A.B <= B.B
```
Результат:
| AA | AB | AC | BA | BB | BD |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | 2 | 4 |
| 2 | 2 | 2 | 2 | 2 | 4 |

Внешнее Левое
Из левой таблицы выбираются все записи. Из правой выбираются только те, которые удовлетворяют условию соединения <join condition>. Если для какой-либо записи левой таблицы не нашлась ни одна пара, то столбцы правой таблицы заменяются NULL-ами.
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A LEFT JOIN B ON A.B = B.B
```
Результат:
| AA | AB | AC | BA | BB | BD |
|---|---|---|---|---|---|
| 1 | 1 | 1 | NULL | NULL | NULL |
| 2 | 2 | 2 | 2 | 2 | 4 |

Внешнее Правое
Эквивалентно левому, если поменять таблицы местами.
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A RIGHT JOIN B ON A.B = B.B
```
Эквивалентно:
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM B LEFT JOIN A ON A.B = B.B
```
Результат:
| AA | AB | AC | BA | BB | BD |
|---|---|---|---|---|---|
| NULL | NULL | NULL | 1 | 0 | 3 |
| 2 | 2 | 2 | 2 | 2 | 4 |

Внешнее Полное
Представляет собой результат объединения левого и правого соединения
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A FULL JOIN B ON A.B = B.B
```
Результат:
| AA | AB | AC | BA | BB | BD |
|---|---|---|---|---|---|
| 1 | 1 | 1 | NULL | NULL | NULL |
| 2 | 2 | 2 | 2 | 2 | 4 |
| NULL | NULL | NULL | 1 | 0 | 3 |

# <cross_join>
Перекрестное соединение, или декартово произведение. Каждая строка левой таблицы соединяется с каждой строкой правой таблицы.

⚠️ Появилось начиная с версии 2.0. В более ранних версиях необходимо использовать INNER JOIN с <join condition> тождественно равным истине.
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A CROSS JOIN B
```
Эквивалентно неявному соединению:
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A, B
```
В ранних версиях:
```sql
SELECT A.A AS AA, A.B AS AB, A.C AS AC, B.A AS BA, B.B AS BB, B.D AS BD
FROM A INNER JOIN B ON 1 = 1
```

Результат:
| AA | AB | AC | BA | BB | BD |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 0 | 3 |
| 1 | 1 | 1 | 2 | 2 | 4 |
| 2 | 2 | 2 | 1 | 0 | 3 |
| 2 | 2 | 2 | 2 | 2 | 4 |

# <named_columns_join>
Является упрощенной записью [JOIN#<qualified_join>](/join/) для случая когда <join condition> содержит только сравнения на равенство и только одноименных столбцов. Часто встречается при соединению по [внешнему ключу](/constraint/).

⚠️ Появилось начиная с версии 2.1

⚠️ Столбцы, которые учавствуют в USING в результирующем наборе встречаются по одному разу.

Также как [JOIN#<qualified_join>](/join/) разделяется на 4 типа.
```sql
SELECT *
FROM A RIGHT JOIN B USING(A, B)
```
Эквивалентно:
```sql
SELECT COALESCE(A.A, B.A) AS A, COALESCE(A.B, B.B) AS B, A.C, B.D
FROM A RIGHT JOIN B ON A.A = B.A AND A.B = B.B
```

Результат:
| A | B | C | D |
|---|---|---|---|
| 1 | 0 | NULL | 3 |
| 2 | 2 | 2 | 4 |

# <natural_join>
Является упрощенной записью [JOIN#<named_columns_join>](/join/) для случая когда <column list> содержит все одноименные столбцы. Удобно при соединению по [внешнему ключу](/constraint/).

⚠️ Появилось начиная с версии 2.1

⚠️ В отличии от других СУБД в Firebird <natural_join> соединяет именно по **одноименным** столбцам, а не по [внешнему ключу](/constraint/).

```sql
SELECT *
FROM A NATURAL RIGHT JOIN B
```

Результат:
| A | B | C | D |
|---|---|---|---|
| 1 | 0 | NULL | 3 |
| 2 | 2 | 2 | 4 |

## См. также
[SELECT](/select/)

http://www.ibase.ru/devinfo/joins.htm
## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes20.html#dml-dsql-cross-join

http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html#rnfb210-joins-sntx
