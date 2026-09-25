---
title: "BIN_AND()"
old_id: bin_and
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# BIN_AND()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
BIN_AND( <number> [, <number> …])

## Описание
Возвращает побитовое И между всеми аргументами.

⚠️ Количество аргументов может быть и нулевым, в результате будет возвращен 0

## Пример
```sql
  SELECT bin_and(flags, 1) FROM x;
```

## См. также
[BIN_OR()](/bin_or/), [BIN_SHL()](/bin_shl/), [BIN_SHR()](/bin_shr/), [BIN_XOR()](/bin_xor/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
