---
title: "NULLIF"
old_id: nullif
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# NULLIF

## Версии сервера
Firebird 1.5, Firebird 2.0 

## Доступно в
DSQL  ESQL  ISQL  PSQL

## Формат
NULLIF (значение1, значение2)

## Описание
Встроенная функция.
Возвращает значение первого аргумента, если он не эквивалентен второму, иначе возвратит NULL.

## Пример
```sql
SELECT
  NULLIF(1,1) A,
  NULLIF(1,2) B,
  NULLIF(NULL, NULL) C,
  NULLIF(1, NULL) D,
  NULLIF(NULL, 1) E
FROM
  RDB$DATABASE
```

Вернет
| A | B | C | D | E |
|---|---|---|---|---|
| NULL | 1 | NULL | 1 | NULL |

## См. также
[CASE](/case/) [COALESCE](/coalesce/) [DECODE](/decode/) [IIF](/iif/)
