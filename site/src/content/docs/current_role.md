---
title: "CURRENT_ROLE"
old_id: current_role
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CURRENT_ROLE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/), [ISQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
CURRENT_ROLE

## Описание
Контекстная переменная возвращает имя роли, с которой подключился текущий пользователь.

## Пример
```sql
SELECT CURRENT_ROLE FROM RDB$DATABASE
```

## Аналог
То же самое значение может быть получено при выполнении оператора
```sql
SELECT RDB$GET_CONTEXT('SYSTEM','CURRENT_ROLE') FROM RDB$DATABASE
```

## Смотри также
RDB$GET_CONTEXT(), RDB$SET_CONTEXT(), [CURRENT_CONNECTION](/current_connection/), [CURRENT_USER](/current_user/)

## Источник
55
