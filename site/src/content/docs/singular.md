---
title: "SINGULAR"
old_id: singular
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# SINGULAR

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
[NOT] SINGULAR (SELECT * FROM *<tablelist>* WHERE *<search_condition>*)

## Описание
SINGULAR проверяет что запрос возвращает одну запись, и в этом случае возвращает TRUE 

оператор SELECT должен использоваться с возвратом всех колонок (*) 

## Пример
```sql
select e.full_name
from employee e
where singular (select * from project p
                 where p.team_leader = e.emp_no)
```
пример возвращает работников, которые являются лидерами в одном и только одном проекте. 

## См. также
[EXISTS()](/exists/), [ALL](/select/)

## Источник
EmbedSQL.pdf
