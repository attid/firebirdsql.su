---
title: "CURRENT_USER"
old_id: current_user
section: glossary
type: term
firebird:
  since: "1.5.3"
  until: 
  deprecated: false
---

# CURRENT_USER

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/), [ISQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
CURRENT_USER

## Описание
Контекстная переменная возвращает имя текущего пользователя, от имени которого было выполнено текущее подключения к базе данных.

## Пример
```sql
SELECT CURRENT_USER FROM RDB$DATABASE
```

## Аналог
То же самое значение может быть получено при выполнении оператора
```sql
SELECT RDB$GET_CONTEXT('SYSTEM','CURRENT_USER') FROM RDB$DATABASE
```

## Смотри также
RDB$GET_CONTEXT(), RDB$SET_CONTEXT(), [CURRENT_CONNECTION](/current_connection/), [CURRENT_ROLE](/current_role/)

## Источник
