---
title: "CURRENT_CONNECTION"
old_id: current_connection
section: glossary
type: term
firebird:
  since: "1.5.3"
  until: 
  deprecated: false
---

# CURRENT_CONNECTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/), [ISQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
CURRENT_CONNECTION

## Описание
Контекстная переменная возвращает идентификатор текущего подключения к базе данных. Идентификатор подключения является значением столбца MON$ATTACHMENT_ID одной из записей (соответствующей текущему подключению) таблицы MON$ATTACHMENTS.

## Пример
```sql
SELECT CURRENT_CONNECTION FROM RDB$DATABASE
```

## Аналог
То же самое значение может быть получено при выполнении оператора
```sql
SELECT RDB$GET_CONTEXT('SYSTEM','SESSION_ID') FROM RDB$DATABASE
```

## Смотри также
MON$ATTACHMENTS, RDB$GET_CONTEXT(), RDB$SET_CONTEXT(), [CURRENT_TRANSACTION](/current_transaction/), [CURRENT_USER](/current_user/), [CURRENT_ROLE](/current_role/)

## Источник
2.0 Release Notes
