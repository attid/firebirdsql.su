---
title: "BIN_SHL()"
old_id: bin_shl
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# BIN_SHL()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
BIN_SHL( <number>, <number> )

## Описание
Возвращает результатом побитовый сдвиг первого аргумента в лево на величину второго аргумента

## Пример
```sql
  SELECT BIN_SHL(flags1, 1) FROM X;
```

## См. также
[BIN_AND()](/bin_and/), [BIN_OR()](/bin_or/), [BIN_SHR()](/bin_shr/), [BIN_XOR()](/bin_xor/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
