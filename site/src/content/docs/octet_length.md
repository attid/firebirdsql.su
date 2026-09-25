---
title: "OCTET_LENGTH()"
old_id: octet_length
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# OCTET_LENGTH()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
OCTET_LENGTH(<value>)

## Описание
Возвращает количество байт памяти (не путать с количеством бит, для этого сущестсвует [BIT_LENGTH()](/bit_length/)), занимаемых строкой, переданной в качестве параметра <value>.

⚠️ Внимание ! Не во всех кодировках количество байт, занимаемых строкой, равно количеству символов !

## Пример
```sql
SELECT RDB$RELATION_NAME, OCTET_LENGTH(RDB$RELATION_NAME), OCTET_LENGTH(TRIM(RDB$RELATION_NAME))
FROM   RDB$RELATIONS;
```

## Смотри также
[LOWER()](/lower/), [UPPER()](/upper/), [TRIM()](/trim/), [CHAR_LENGTH()](/char_length/), [BIT_LENGTH()](/bit_length/)

## Источник
Firebird_2_0\doc\sql.extensions\README.length.txt
