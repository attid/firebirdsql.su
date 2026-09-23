---
title: "RDB$DATABASE"
old_id: rdb_database
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$DATABASE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | - |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

## Описание

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$DESCRIPTION | BLOB(80) |  |
| RDB$RELATION_ID | SMALLINT |  |
| RDB$SECURITY_CLASS | CHAR(31) |  |
| RDB$CHARACTER_SET_NAME | CHAR(31) | Кодировка базы данных, например UTF8 |

## Пример
```sql
  SELECT * FROM RDB$DATABASE
```

## См. также

## Источник
%Firebird%\doc\
