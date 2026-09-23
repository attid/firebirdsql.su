---
title: "RDB$RELATION_FIELDS"
old_id: rdb_relation_fields
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$RELATION_FIELDS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| ? | ? | ? | ? | ? | ? | ? | ? | ? | + | + |

## Описание
Системная таблица RDB$RELATION_FIELDS хранит определения столбцов.

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$FIELD_NAME | CHAR(31) | Имя столбца, уникальное в таблице или представлении |
| RDB$RELATION_NAME | CHAR(31) | Имя таблицы или представления |
| RDB$FIELD_SOURCE | CHAR(31) | Имя, сгенерированное системой (SQL&nnn) для этого столбца, связанное с RDB$FIELDS. Если столбец основан на домене, то два связанных столбца RDB$FIELD_SOURCE хранят имя домена. |
| … | … | … |

## Пример
```sql
  SELECT * FROM employee e
```

## См. также

## Источник
%Firebird%\doc\
