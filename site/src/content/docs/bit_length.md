---
title: "BIT_LENGTH()"
old_id: bit_length
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# BIT_LENGTH()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
BIT_LENGTH(<value>)

## Описание
Возвращает количество бит памяти, занимаемых строкой, переданной в качестве параметра <value>.

## Пример
```sql
select rdb$relation_name, bit_length(rdb$relation_name), bit_length(trim(rdb$relation_name))
from rdb$relations;
```

## Смотри также
[LOWER()](/lower/), [UPPER()](/upper/), [TRIM()](/trim/), [CHAR_LENGTH()](/char_length/)

## Источник
Firebird_2_0\doc\sql.extensions\README.length.txt
