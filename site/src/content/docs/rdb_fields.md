---
title: "RDB$FIELDS"
old_id: rdb_fields
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$FIELDS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
rdb fields

## Описание
Информация о доменах базы данных
| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$FIELD_NAME | CHAR(31) | Имя поля, должно быть уникальное для таблицы |
| RDB$QUERY_NAME | CHAR(31) |  |
| RDB$VALIDATION_BLR | BLOB |  |
| RDB$VALIDATION_SOURCE | BLOB |  |
| RDB$COMPUTED_BLR | BLOB |  |
| RDB$COMPUTED_SOURCE | BLOB | Содержит выражение для вычисления значения поля |
| RDB$DEFAULT_VALUE | BLOB |  |
| RDB$DEFAULT_SOURCE | BLOB | Содержит значение по умолчанию для этого поля |
| RDB$FIELD_LENGTH | SMALLINT | Длина поля |
| RDB$FIELD_SCALE | SMALLINT | Масштаб числовых типов данных |
| RDB$FIELD_TYPE | SMALLINT | Тип данных |
| RDB$FIELD_SUB_TYPE | SMALLINT | Подтип данных |
| RDB$MISSING_VALUE | BLOB |  |
| RDB$MISSING_SOURCE | BLOB |  |
| RDB$DESCRIPTION | BLOB |  |
| RDB$SYSTEM_FLAG | SMALLINT |  |
| RDB$QUERY_HEADER | BLOB |  |
| RDB$SEGMENT_LENGTH | SMALLINT |  |
| RDB$EDIT_STRING | VARCHAR(127) |  |
| RDB$EXTERNAL_LENGTH | SMALLINT |  |
| RDB$EXTERNAL_SCALE | SMALLINT |  |
| RDB$EXTERNAL_TYPE | SMALLINT |  |
| RDB$DIMENSIONS | SMALLINT |  |
| RDB$NULL_FLAG | SMALLINT |  |
| RDB$CHARACTER_LENGTH | SMALLINT |  |
| RDB$COLLATION_ID | SMALLINT |  |
| RDB$CHARACTER_SET_ID | SMALLINT |  |
| RDB$FIELD_PRECISION | SMALLINT |  |

# Типы данных
| Код | Тип | Начиная с | Диалект |
|---|---|---|---|
| 7 | SHORT | - | 1-3 |
| 8 | LONG | - | 1-3 |
| 9 | QUAD | - |  |
| 10 | FLOAT | - | 1-3 |
| 12 | DATE | - | 1-3 |
| 13 | TIME | - | 3 |
| 14 | TEXT | - | 1-3 |
| 16 | INT64 | - | 3 |
| 23 | BOOLEAN | 3.0 | 3 |
| 27 | DOUBLE | - | 1-3 |
| 35 | TIMESTAMP | - | 3 |
| 37 | VARYING | - | 1-3 |
| 40 | CSTRING | - | 1-3 |
| 45 | BLOB_ID | - |  |
| 261 | BLOB | - | 1-3 |

# Подтипы данных
| Код | Подтип |
|---|---|
| 0 | BINARY |
| 1 | TEXT |
| 2 | BLR |
| 3 | ACL |
| 4 | RANGES |
| 5 | SUMMARY |
| 6 | FORMAT |
| 7 | TRANSACTION_DESCRIPTION |
| 8 | EXTERNAL_FILE_DESCRIPTION |
## Пример
старый и данные устаревшие, поэтому вы получите не то, что запросили
```sql
select
cast(
  'CREATE DOMAIN '||trim(RDB$FIELD_NAME)||' as '||

    case RDB$FIELD_TYPE
        when 7 then 'SMALLINT'
        when 8 then 'INTEGER'
        when 12 then 'DATE'
        when 13 then 'TIME'
        when 14 then 'CHAR('||rdb$field_length||')'
        when 16 then
          iif(rdb$field_sub_type = 0,'BIGINT', 'NUMERIC('||RDB$FIELD_PRECISION||','||(-1*rdb$field_scale)||')')
        when 35 then 'TIMESTAMP'
        when 37 then 'VARCHAR('||rdb$field_length||')'
        when 261 then 'BLOB SUB_TYPE '||rdb$field_sub_type||' SEGMENT SIZE '||rdb$segment_length
        else cast(RDB$FIELD_TYPE as varchar(10))
    end
    ||trim(iif(RDB$NULL_FLAG = 1,' NOT NULL ',' ')
      ||coalesce(' '||RDB$DEFAULT_SOURCE,'')
      ||coalesce(' '||rdb$validation_SOURCE,''))
    ||';'
as varchar(1000))
from RDB$FIELDS where (not (RDB$FIELD_NAME starting with 'RDB$')) and RDB$SYSTEM_FLAG = 0
order by RDB$FIELD_NAME
```

## См. также
[Системные таблицы](/sistemnye_tablicy/)

[Таблицы мониторинга](/tablicy_monitoringa/)
## Источник
%Firebird%\doc\
