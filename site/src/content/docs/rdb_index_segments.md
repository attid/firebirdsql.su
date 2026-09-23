---
title: "RDB$INDEX_SEGMENTS"
old_id: rdb_index_segments
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$INDEX_SEGMENTS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Описание

Системная таблица RDB$INDEX_SEGMENTS хранит сегменты и позиции составных индексов.

| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$INDEX_NAME | CHAR(31) | Имя индекса |
| RDB$FIELD_NAME | CHAR(31) | Имя ключевого столбца в индексе |
| RDB$FIELD_POSITION | SMALLINT | Позиция столбца в индексе |

## Источник
%Firebird%\doc\
