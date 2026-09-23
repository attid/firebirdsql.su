---
title: "LIKE"
old_id: like
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# LIKE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | + | + | + | + | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
<переменая> [NOT] LIKE <значение> [ESCAPE символ]
```

## Описание
Это регистро зависимый оператор для поиска строк, (не)содержащих заданную строку.

Может использоваться как в SQL так и в DSQL

для задания маски имеет 2 спец символа это 

**%** (знак процента) для обозначения любой последовательности символов (как * в поиске файлов)

**_** (знак подчеркивания) для обозначения одного символа (как ? в поиске файлов)

**ESCAPE** позволяет задать экранирующий символ 

## Пример
Найти людей в фамилии которых две последовательно идущих буквы "e"
```sql
select * from employee e where e.last_name like '%ee%'  
```
Найти людей в фамилии которых вторая буква "e"
```sql
select * from employee e where e.last_name like '_e%'
```
Найти людей в фамилии которых нет буквы "e"
```sql
select * from employee e where not e.last_name like '%e%'
```
Найти объекты содержащие в названии знак подчеркивания "_"
```sql
select rdb$relation_name from rdb$relations where rdb$relation_name like '%\_%' escape '\'
```

## См. также
[CONTAINING](/containing/),  STARTING WITH

## Источник
EmbedSQL.pdf 

SQL92
