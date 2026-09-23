---
title: "RDB$TRANSACTIONS"
old_id: rdb_transactions
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$TRANSACTIONS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
CREATE TABLE RDB$TRANSACTIONS (
    RDB$TRANSACTION_ID           INTEGER,
    RDB$TRANSACTION_STATE        SMALLINT,
    RDB$TIMESTAMP                TIMESTAMP,
    RDB$TRANSACTION_DESCRIPTION  BLOB SUB_TYPE 7 SEGMENT SIZE 80
);

CREATE UNIQUE INDEX RDB$INDEX_32 ON RDB$TRANSACTIONS (RDB$TRANSACTION_ID)
```

## Описание
Системная таблица RDB$TRANSACTIONS отслеживает транзакции <u>с несколькими</u> базами данных.

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$TRANSACTION_ID | INTEGER | Уникальный идентификатор отслеживаемой транзакции |
| RDB$TRANSACTION_STATE | SMALLINT | Состояние транзакции: (0)-зависшая, (1) - подтвержденная [COMMIT](/commit/), (2) - отмененная ROLLBACK |
| RDB$TIMESTAMP | TIMESTAMP | Зарезервировано для будующих версий. |
| RDB$TRANSACTION_DESCRIPTION | BLOB | Описывает подгoтовленную транзакцию к нескольким базам данных, доступна в случае потери соединения, которое не может быть восстановлено |

## Пример

## См. также
[Системные таблицы](/sistemnye_tablicy/)

## Источник
