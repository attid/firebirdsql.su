---
title: "RDB$TRIGGERS"
old_id: rdb_triggers
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$TRIGGERS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
CREATE TABLE RDB$TRIGGERS (
    RDB$TRIGGER_NAME      CHAR(31) CHARACTER SET UNICODE_FSS,
    RDB$RELATION_NAME     CHAR(31) CHARACTER SET UNICODE_FSS,
    RDB$TRIGGER_SEQUENCE  SMALLINT,
    RDB$TRIGGER_TYPE      SMALLINT,
    RDB$TRIGGER_SOURCE    BLOB SUB_TYPE 1 SEGMENT SIZE 80 CHARACTER SET UNICODE_FSS,
    RDB$TRIGGER_BLR       BLOB SUB_TYPE 2 SEGMENT SIZE 80,
    RDB$DESCRIPTION       BLOB SUB_TYPE 1 SEGMENT SIZE 80 CHARACTER SET UNICODE_FSS,
    RDB$TRIGGER_INACTIVE  SMALLINT,
    RDB$SYSTEM_FLAG       SMALLINT,
    RDB$FLAGS             SMALLINT,
    RDB$VALID_BLR         SMALLINT,
    RDB$DEBUG_INFO        BLOB SUB_TYPE 9 SEGMENT SIZE 80
);

CREATE INDEX RDB$INDEX_38 ON RDB$TRIGGERS (RDB$RELATION_NAME);
CREATE UNIQUE INDEX RDB$INDEX_8 ON RDB$TRIGGERS (RDB$TRIGGER_NAME);
```

## Описание
Системная таблица RDB$TRIGGERS содержит информацию о всех триггерах в базе данных. 

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$TRIGGER_NAME | CHAR(31) | Имя триггера. Должно быть уникально. |
| RDB$RELATION_NAME | CHAR(31) | Имя просмотра или таблицы, для которой используется триггер. |
| RDB$TRIGGER_SEQUENCE | SMALLINT | Последовательность выполнения триггера в рамках его действия. По-умолчанию - ноль. |
| RDB$TRIGGER_TYPE | SMALLINT | Тип триггера - определяет событие, при котором произойдет выполнение триггера. См. ниже. |
| RDB$TRIGGER_SOURCE | BLOB | Хранит [PSQL](/raznovidnosti_jazyka_sql/) -исходный код триггера. |
| RDB$TRIGGER_BLR | BLOB | Хранит скомпилированное сервером тело триггера в двоичном виде. |
| RDB$DESCRIPTION | BLOB | Служит для хранения пользовательской документации о триггере. |
| RDB$TRIGGER_INACTIVE | SMALLINT | Признак, является ли триггер в настоящее время неактивным ("1" - триггер "отключен", "0" - триггер активен). |
| RDB$SYSTEM_FLAG | SMALLINT | Признак того, что триггер определен системой (1) или пользователем (не равно 1) |
| RDB$FLAGS | SMALLINT | Для внутреннего использования |
| RDB$VALID_BLR | SMALLINT | *Не документировано* |
| RDB$DEBUG_INFO | BLOB | *Не документировано* |

Определены следующие типы триггеров по событию:
|  |  |  |
|---|---|---|
| 1 | BEFORE INSERT | Триггер выполняется перед вставкой записи в таблицу или просмотр. |
| 2 | AFTER INSERT | Триггер выполняется после вставки записи в таблицу или просмотр. |
| 3 | BEFORE UPDATE | Триггер выполняется перед изменением записи в таблице или просмотре. |
| 4 | AFTER UPDATE | Триггер выполняется после изменения записи в таблице или просмотре. |
| 5 | BEFORE DELETE | Триггер выполняется перед удалением записи из таблицы или просмотра. |
| 6 | AFTER DELETE | Триггер выполняется после удаления записи из таблицы или просмотра. |
| 17 | BEFORE INSERT OR UPDATE | Триггер выполняется перед вставкой или изменением записи в таблице или просмотре. |
| 18 | AFTER INSERT OR UPDATE | Триггер выполняется после вставки или изменения записи в таблице или просмотре. |
| 25 | BEFORE INSERT OR DELETE | Триггер выполняется перед вставкой или удалением записи в таблице или просмотре. |
| 26 | AFTER INSERT OR DELETE | Триггер выполняется после вставки или удаления записи в таблице или просмотре. |
| 27 | BEFORE UPDATE OR DELETE | Триггер выполняется перед изменением или удалением записи в таблице или просмотре. |
| 28 | AFTER UPDATE OR DELETE | Триггер выполняется после изменения или удаления записи в таблице или просмотре. |
| 113 | BEFORE INSERT OR UPDATE OR DELETE | Триггер выполняется перед вставкой, изменением или удалением записи в таблице или просмотре. |
| 114 | AFTER INSERT OR UPDATE OR DELETE | Триггер выполняется после вставки, изменения или удаления записи в таблице или просмотре. |
| 8192 | ON CONNECT | Триггер выполняется после установления подключения к базе данных. |
| 8193 | ON DISCONNECT | Триггер выполняется перед отключением от базы данных. |
| 8194 | ON TRANSACTION START | Триггер выполняется после старта транзакции. |
| 8195 | ON TRANSACTION COMMIT | Триггер выполняется перед подтверждением [COMMIT](/commit/) транзакции. |
| 8196 | ON TRANSACTION ROLLBACK | Триггер выполняется перед отменой ROLLBACK транзакции. |

## Пример
Следующий пример выводит список всех триггеров для таблицы MY_TABLE
```sql
SELECT T.RDB$TRIGGER_NAME, T.RDB$TRIGGER_SEQUENCE,
    CASE T.RDB$TRIGGER_TYPE
      WHEN   1 THEN 'BEFORE INSERT'
      WHEN   2 THEN 'AFTER INSERT'
      WHEN   3 THEN 'BEFORE UPDATE'
      WHEN   4 THEN 'AFTER UPDATE'
      WHEN   5 THEN 'BEFORE DELETE'
      WHEN   6 THEN 'AFTER DELETE'
      WHEN  17 THEN 'BEFORE INSERT OR UPDATE'
      WHEN  18 THEN 'AFTER INSERT OR UPDATE'
      WHEN  25 THEN 'BEFORE INSERT OR DELETE'
      WHEN  26 THEN 'AFTER INSERT OR DELETE'
      WHEN  27 THEN 'BEFORE UPDATE OR DELETE'
      WHEN  28 THEN 'AFTER UPDATE OR DELETE'
      WHEN 113 THEN 'BEFORE INSERT OR UPDATE OR DELETE'
      WHEN 114 THEN 'AFTER INSERT OR UPDATE OR DELETE'
    END AS TRIGGER_TYPE
FROM  RDB$TRIGGERS T
WHERE (T.RDB$RELATION_NAME = 'MY_TABLE')
```

Следующий PSQL-блок вернет DSQL скрипт создания триггера, имя которого передано в качестве параметра TRIGGER_NAME.
```sql
EXECUTE BLOCK(
  A_TRIGGER_NAME VARCHAR(31) = ?TRIGGER_NAME
)RETURNS(
  DDLSQL BLOB SUB_TYPE 1 SEGMENT SIZE 80 CHARACTER SET UNICODE_FSS
)AS
  DECLARE VARIABLE P_TRIGGER_NAME   VARCHAR(31);
  DECLARE VARIABLE P_RELATION_NAME  VARCHAR(31);
  DECLARE VARIABLE P_TRIGGER_TYPE   VARCHAR(80);
  DECLARE VARIABLE P_TRIGGER_ACTIVE VARCHAR(8);
  DECLARE VARIABLE P_TRIGGER_POS    INTEGER;
  DECLARE VARIABLE P_TRIGGER_SRC    BLOB SUB_TYPE 1 SEGMENT SIZE 80
                                          CHARACTER SET UNICODE_FSS;
BEGIN
  DDLSQL = '';
  SELECT FIRST 1 TRIM(T.RDB$TRIGGER_NAME), TRIM(T.RDB$RELATION_NAME),
      T.RDB$TRIGGER_SEQUENCE, T.RDB$TRIGGER_SOURCE,
      CASE T.RDB$TRIGGER_INACTIVE
        WHEN 1 THEN 'INACTIVE'
        WHEN 0 THEN 'ACTIVE'
      END AS TRIG_ACTIVE,
      CASE T.RDB$TRIGGER_TYPE
        WHEN   1 THEN 'BEFORE INSERT'
        WHEN   2 THEN 'AFTER INSERT'
        WHEN   3 THEN 'BEFORE UPDATE'
        WHEN   4 THEN 'AFTER UPDATE'
        WHEN   5 THEN 'BEFORE DELETE'
        WHEN   6 THEN 'AFTER DELETE'
        WHEN  17 THEN 'BEFORE INSERT OR UPDATE'
        WHEN  18 THEN 'AFTER INSERT OR UPDATE'
        WHEN  25 THEN 'BEFORE INSERT OR DELETE'
        WHEN  26 THEN 'AFTER INSERT OR DELETE'
        WHEN  27 THEN 'BEFORE UPDATE OR DELETE'
        WHEN  28 THEN 'AFTER UPDATE OR DELETE'
        WHEN 113 THEN 'BEFORE INSERT OR UPDATE OR DELETE'
        WHEN 114 THEN 'AFTER INSERT OR UPDATE OR DELETE'
      END AS TRIGGER_TYPE
  FROM  RDB$TRIGGERS T
  WHERE (UPPER(TRIM(T.RDB$TRIGGER_NAME)) =  :A_TRIGGER_NAME)
  INTO  :P_TRIGGER_NAME, :P_RELATION_NAME, :P_TRIGGER_POS, :P_TRIGGER_SRC,
        :P_TRIGGER_ACTIVE, :P_TRIGGER_TYPE;

  DDLSQL = 'CREATE OR ALTER TRIGGER '||:P_TRIGGER_NAME||' FOR '||
    :P_RELATION_NAME||' '||ASCII_CHAR(13)||ASCII_CHAR(10)||
    :P_TRIGGER_ACTIVE||'  '||:P_TRIGGER_TYPE||' POSITION '||:P_TRIGGER_POS||
    ' '||ASCII_CHAR(13)||ASCII_CHAR(10)||:P_TRIGGER_SRC;

  SUSPEND;
END
```

## См. также
[Системные таблицы](/sistemnye_tablicy/), [CREATE TRIGGER](/create_trigger/), [DROP TRIGGER](/drop_trigger/), [ALTER TRIGGER](/alter_trigger/)

## Источник
