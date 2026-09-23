---
title: "BIN_OR()"
old_id: bin_or
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# BIN_OR()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
BIN_OR( <number> [, <number> …])

## Описание
Возвращает побитовое ИЛИ между всеми аргументами.

⚠️ Количество аргументов может быть и нулевым, в результате будет возвращен 0

## Пример
```sql
  SELECT BIN_OR(flags1, flags2) FROM x;
```

## См. также
[BIN_AND()](/bin_and/), [BIN_SHL()](/bin_shl/), [BIN_SHR()](/bin_shr/), [BIN_XOR()](/bin_xor/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
