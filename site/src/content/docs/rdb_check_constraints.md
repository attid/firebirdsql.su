---
title: "RDB$CHECK_CONSTRAINTS"
old_id: rdb_check_constraints
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# RDB$CHECK_CONSTRAINTS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
CREATE TABLE RDB$CHECK_CONSTRAINTS (
    RDB$CONSTRAINT_NAME  CHAR(31) CHARACTER SET UNICODE_FSS,
    RDB$TRIGGER_NAME     CHAR(31) CHARACTER SET UNICODE_FSS
);

CREATE INDEX RDB$INDEX_14 ON RDB$CHECK_CONSTRAINTS (RDB$CONSTRAINT_NAME);
CREATE INDEX RDB$INDEX_40 ON RDB$CHECK_CONSTRAINTS (RDB$TRIGGER_NAME);
```

## Описание
Системная таблица RDB$CНECK_CONSТRAINТS содержит перекрестные ссылки имен и триггеров для ограничений [СНЕСК](/constraint/) и [NOT NULL](/constraint/) 

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$CONSTRAINT_NAМE | СНАR(З1) | Имя ограничения ссылочной целостности |
| RDB$TRIGGER_NAМE | СНАR(З1) | Для ограничения [СНЕСК](/constraint/) это имя триггера, который поддерживает данное ограничение. Для ограничения [NOT NULL](/constraint/) это имя столбца, к которому применяется ограничение - имя таблицы может быть найдено через имя oграничения |

## Пример

## См. также
[Системные таблицы](/sistemnye_tablicy/)

## Источник
