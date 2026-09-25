---
title: "replace()"
old_id: replace
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# replace()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
REPLACE( <где ищем>, <что меняем>, <на что меняем> )

## Описание
Встроенная функция.
REPLACE(searched, find, replacement) 
Заменяет все вхождения подстроки "find" в строке "searched" на подстроку "replacement".
## Пример
```sql
select replace('I love beer with lemon', 'beer', 'tea') from rdb$database
```
вернет строку "I love tea with lemon"
## См. также
[LEFT()](/left/),  [RIGHT()](/right/),  [OVERLAY()](/overlay/),  [POSITION()](/position/),  [CHAR_LENGTH()](/char_length/), [SUBSTRING()](/substring/)

## Источник
%Firebird%\doc\
