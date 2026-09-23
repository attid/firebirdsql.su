---
title: "CURRENT_TRANSACTION"
old_id: current_transaction
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CURRENT_TRANSACTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [ESQL](/raznovidnosti_jazyka_sql/), [ISQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
CURRENT_TRANSACTION

## Описание
Контекстная переменная возвращает идентификатор текущей транзакции, в рамках которой выполняется оператор. Идентификатор транзакции является значением столбца MON$TRANSACTION_ID одной из записей (соответствующей текущей транзакции) таблицы MON$TRANSACTIONS.

## Пример
```sql
SELECT CURRENT_TRANSACTION FROM RDB$DATABASE
```

## Аналог
То же самое значение может быть получено при выполнении оператора
```sql
SELECT RDB$GET_CONTEXT('SYSTEM','TRANSACTION_ID') FROM RDB$DATABASE
```

## Смотри также
MON$TRANSACTIONS, RDB$GET_CONTEXT(), RDB$SET_CONTEXT(), [CURRENT_CONNECTION](/current_connection/), [CURRENT_USER](/current_user/), [CURRENT_ROLE](/current_role/)

## Источник
