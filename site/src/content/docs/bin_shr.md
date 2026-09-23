---
title: "BIN_SHR()"
old_id: bin_shr
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# BIN_SHR()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
BIN_SHR( <number1>, <number2> )

## Описание
Возвращает результатом побитовый сдвиг первого аргумента в вправо на величину второго аргумента
(аналогично инструкции number1 >> number2 языка C)

## Пример
```sql
  SELECT BIN_SHR(flags1, 1) FROM X;
```

## См. также
[BIN_AND()](/bin_and/), [BIN_OR()](/bin_or/), [BIN_SHL()](/bin_shl/), [BIN_XOR()](/bin_xor/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html
