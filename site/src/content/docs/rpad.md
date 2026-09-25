---
title: "RPAD()"
old_id: rpad
section: glossary
type: term
firebird:
  since: "1.5"
  until: 
  deprecated: false
---

# RPAD()

## Версии сервера
|  | 0.9 | 1.0 | 1.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|
| Как UDF | - | - | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
RPAD( <string>, <number> [, <string> ] )

## Описание
Возвращает подстроку заданной длины, дополненной справа заданным символом

## Пример
```sql
  select RPAD('ABC', 5) as RS, RPAD('ABC', 5,'_') as R_ from rdb$database
```
результат
| RS | R_ |
|---|---|
| ABC | ABC__ |
## См. также
[LPAD](/lpad/), [TRIM](/trim/)

## Источник
%Firebird%\doc\
