---
title: "LEFT()"
old_id: left
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# LEFT()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
left(<строка>, <длина>)

## Описание
Возвращает левую (начальную) часть строки <строка>, длиной <длина>

## Пример
```sql
  SELECT left(firstname,1) FROM employee e
```
Возвращает первую букву имени (инициал)
## См. также
[POSITION()](/position/), [substring()](/substring/)

## Источник
%Firebird%\doc\
