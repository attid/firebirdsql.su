---
title: "MON$DATABASE"
old_id: mon_database
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# MON$DATABASE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
CREATE TABLE MON$DATABASE (
    MON$DATABASE_NAME       VARCHAR(253),
    MON$PAGE_SIZE           SMALLINT,
    MON$ODS_MAJOR           SMALLINT,
    MON$ODS_MINOR           SMALLINT,
    MON$OLDEST_TRANSACTION  INTEGER,
    MON$OLDEST_ACTIVE       INTEGER,
    MON$OLDEST_SNAPSHOT     INTEGER,
    MON$NEXT_TRANSACTION    INTEGER,
    MON$PAGE_BUFFERS        INTEGER,
    MON$SQL_DIALECT         SMALLINT,
    MON$SHUTDOWN_MODE       SMALLINT,
    MON$SWEEP_INTERVAL      INTEGER,
    MON$READ_ONLY           SMALLINT,
    MON$FORCED_WRITES       SMALLINT,
    MON$RESERVE_SPACE       SMALLINT,
    MON$CREATION_DATE       TIMESTAMP,
    MON$PAGES               BIGINT,
    MON$STAT_ID             INTEGER,
    MON$BACKUP_STATE        SMALLINT
);
```

## Описание

| MON$DATABASE (база данных) | имеет одну запись (например, как RDB$DATABASE), хранящую служебную информацию о текущей базе данных. |
|---|---|
| MON$DATABASE_NAME | физическое имя файла базы данных в файловой системе. Полезно, когда подключение к БД делается по псевдониму (алиасу). |
| MON$PAGE_SIZE | размер страницы базы данных (1024, 2048, 4096, 8192, 16384) |
| MON$ODS_MAJOR | старшая версия ODS базы данных, например 11 |
| MON$ODS_MINOR | младшая версия ODS базы данных, например 1 |
| MON$OLDEST_TRANSACTION | (OIT number) |
| MON$OLDEST_ACTIVE | (OAT number) |
| MON$OLDEST_SNAPSHOT | (OST number) |
| MON$NEXT_TRANSACTION | ID следующей транзакции (значение "генератора транзакций") |
| MON$PAGE_BUFFERS | количество страниц, расположенных в кэше |
| MON$SQL_DIALECT | диалект языка SQL |
| MON$SHUTDOWN_MODE | текущий режим остановки |
| MON$SWEEP_INTERVAL | интервал перед сборкой мусора |
| MON$READ_ONLY | признак доступности базы данных только для чтения |
| MON$FORCED_WRITES | признак синхронной записи |
| MON$RESERVE_SPACE | признак резервирования места на страницах БД для версий записей, созданных в результате обновлений/удалений |
| MON$CREATION_DATE | дата создания (восстановления из бэкапа) файла базы данных |
| MON$PAGES | суммарное количество страниц базы данных |
| MON$BACKUP_STATE | текущее физическое состояние бэкапа |
| MON$STAT_ID | ссылка на MON$IO_STATS |

Текущий режим остановки MON$SHUTDOWN_MODE принимает значения:
|  |  |
|---|---|
| 0 | online |
| 1 | multi-user shutdown |
| 2 | single-user shutdown |
| 3 | full shutdown |

Режим MON$BACKUP_STATE принимает значения:
|  |  |
|---|---|
| 0 | normal |
| 1 | stalled |
| 2 | merge |

Эти значения могут быть получены при помощи выполнения следующего запроса:
```sql
SELECT T.RDB$TYPE, T.RDB$TYPE_NAME 
FROM   RDB$TYPES T 
WHERE (T.RDB$FIELD_NAME ='MON$SHUTDOWN_MODE')
```

## Пример

## См. также
[Таблицы мониторинга](/tablicy_monitoringa/), MON$ATTACHMENTS, MON$CALL_STACK, MON$CONTEXT, MON$DATABASE, MON$IO_STATS, MON$RECORD_STATS, MON$STATEMENTS,  MON$TRANSACTIONS

## Источник
($firebird)/doc/README.monitoring_tables.txt
