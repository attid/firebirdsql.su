---
title: "EXISTS"
old_id: exists
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# EXISTS

## Версии сервера
Firebird 2.0 

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
[NOT] EXISTS (SELECT * FROM <tablelist> WHERE <search_condition>)

## Описание
оператор проверяет существует ли хоть одна запись в запросе 

внутрений запрос выполняется до получения первой записи запроса.

используется в основном в [поисковых условиях], но может так же использоваться в pl-sql c оператором if 

## Пример
```sql
select 1 from rdb$database
 where exists(select * 
                from sales s
               where s.cust_no = 1001)
```

## См. также
[SELECT](/select/), [IF](/if/), [SINGULAR](/singular/)

## Источник
EmbedSQL.pdf
