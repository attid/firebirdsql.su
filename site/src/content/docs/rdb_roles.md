---
title: "RDB$ROLES"
old_id: rdb_roles
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$ROLES

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
CREATE TABLE RDB$ROLES (
    RDB$ROLE_NAME    CHAR(31) CHARACTER SET UNICODE_FSS,
    RDB$OWNER_NAME   CHAR(31) CHARACTER SET UNICODE_FSS,
    RDB$DESCRIPTION  BLOB SUB_TYPE 1 SEGMENT SIZE 80 CHARACTER SET UNICODE_FSS,
    RDB$SYSTEM_FLAG  SMALLINT
);

CREATE UNIQUE INDEX RDB$INDEX_39 ON RDB$ROLES (RDB$ROLE_NAME);
```

## Описание
Системная таблица RDB$ROLES содержит информацию о ролях доступа к базе данных. 

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$ROLE_NAME | СНАR(З1) | Имя роли |
| RDB$OWNER_NAME | СНАR(З1) | Имя пользователя-владельца роли |
| RDB$DESCRIPTION | BLOB | Поле для хранения пользовательской документации |
| RDB$SYSTEM_FLAG | SMALLINT | Указывает, является ли роль системной (1), или создана пользователем (не равно 1) |

## Пример
Следующий пример выводит набор данных, содержащий имена всех ролей доступа к базе данных.
```sql
SELECT R1.RDB$ROLE_NAME AS ROLENAME 
FROM   RDB$ROLES R1
```

## См. также
[Системные таблицы](/sistemnye_tablicy/),  [CREATE ROLE](/create_role/), [DROP ROLE](/drop_role/), [GRANT](/grant/), [REVOKE](/revoke/)

## Источник
