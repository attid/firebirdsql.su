---
title: "reverse"
old_id: reverse
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# reverse

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
REVERSE( <value> )

## Описание
Возвращает перевернутую строку 

## Пример
```sql
    create index people_email on people computed by (reverse(email));
    select * from people where reverse(email) starting with reverse('.br');
```

## См. также

## Источник
%Firebird%\doc\

## Примечание
Удобно для построения индексов для использования совместно с STARTING WITH
