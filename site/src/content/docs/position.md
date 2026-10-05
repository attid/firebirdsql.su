---
title: "POSITION()"
old_id: position
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# POSITION()
## Версии сервера
| 1.0 | 1.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|
| - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)
## Формат
POSITION (string_exp1 IN string_exp2)

POSITION( <string>, <string> [, <number>] )
## Описание
Firebird 2.1
Возвращает позицию первого вхождения string_exp1 в string_exp2 начиная со смещения (или с начала если опущено).
Если строка не найдена, то функция возвращает 0.
## Пример
```sql
POSITION('ll' IN 'hello') = 3

POSITION('la' IN 'hello') = 0

POSITION('test', 'test for test') = 1

POSITION('test', 'test for test', 3) = 10
```

## См. также
[SUBSTRING()](/substring/)

## Источник
%Firebird%\doc\
