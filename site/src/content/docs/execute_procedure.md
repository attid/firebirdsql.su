---
title: "EXECUTE PROCEDURE"
old_id: execute_procedure
section: glossary
type: term
firebird:
  since: "1.0"
  until: 
  deprecated: false
---

# EXECUTE PROCEDURE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| ? | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
EXECUTE PROCEDURE name [param [, param …]]
[RETURNING_VALUES param [, param …]]

## Описание
Позволяет вызвать процедуру которая не возращает параметры или возращает их единожды

## Пример
```sql
create procedure set_context(User_ID varchar(40), Trn_ID integer) as
begin
  RDB$SET_CONTEXT('USER_TRANSACTION', 'Trn_ID', Trn_ID);
  RDB$SET_CONTEXT('USER_TRANSACTION', 'User_ID', User_ID);
end;
```
```sql
execute procedure set_context('skidder', 1);
```
## См. также
[ALTER PROCEDURE](/alter_procedure/), [CREATE PROCEDURE](/create_procedure/), [DROP PROCEDURE](/drop_procedure/),\
RDB$GET_CONTEXT, RDB$SET_CONTEXT

## Источник
LANGREF.PDF
