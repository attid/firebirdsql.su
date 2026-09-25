---
title: "between"
old_id: interval
section: glossary
type: term
firebird:
  since: "2.0.4"
  until: 
  deprecated: false
---

# between

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
<between_predicate> ::=
     <psql_expr> BETWEEN <psql_expr> AND <psql_expr>
   | <psql_expr> NOT BETWEEN <psql_expr> AND <psql_expr>
```
## Описание
Используйте BETWEEN, чтобы проверить, находится ли значение в определенном диапазоне, включая пределы диапазона..

## Пример
В диапазоне
```sql
SELECT * FROM `tbl` t WHERE t.id BETWEEN 1 and 100
```

аналог 
```sql
select * from 'tbl' t where t.id >= 1 and t.id ⇐ 100
```

Вне диапазона
```sql
SELECT * FROM `tbl` t WHERE t.id NOT BETWEEN 1 and 100
```

аналог 
```sql
select * from 'tbl' t where NOT (t.id >= 1 and t.id ⇐ 100)
```
## См. также
[dateadd](/dateadd/)

## Источник
http://www.janus-software.com/fbmanual/manual.php?book=psql&topic=80
