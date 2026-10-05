---
title: "LPAD()"
old_id: lpad
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# LPAD()

## Версии сервера
|  | 0.9 | 1.0 | 1.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|
| Как UDF | - | - | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
LPAD( <string>, <number> [, <string> ] )

## Описание
Возвращает подстроку заданной длины, дополненной слева заданным символом

## Пример
```sql
  select lpad('ABC', 5) as LS, lpad('ABC', 5,'_') as L_ from rdb$database
```
результат
| LS | L_ |
|---|---|
| ABC | __ABC |
## См. также
[RPAD](/rpad/), [TRIM](/trim/)

## Источник
%Firebird%\doc\
