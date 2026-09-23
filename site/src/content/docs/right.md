---
title: "RIGHT()"
old_id: right
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RIGHT()

## Версии сервера
| 0.9 | 1.0 | 1.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|
| - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
right(<строка>, <длина>)

## Описание
Возвращает правую (конечную) часть строки <строка>, длиной <длина>

## Пример
```sql
  SELECT right('ABCDEFG',1) FROM rdb$database
```
Возвращает последнюю букву строки (G)
## См. также
[POSITION()](/position/), [substring()](/substring/), [left()](/left/), [char_length()](/char_length/)

## Источник
%Firebird%\doc\
