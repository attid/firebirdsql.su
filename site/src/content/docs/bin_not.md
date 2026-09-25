---
title: "BIN_NOT()"
old_id: bin_not
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# BIN_NOT()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | - |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
bin_not(<number>)

## Описание
Возвращает побитовое NOT.

## Пример
```sql
  SELECT bin_not(4) FROM employee e
```

## См. также
[BIN_OR()](/bin_or/), [BIN_SHL()](/bin_shl/), [BIN_SHR()](/bin_shr/), [BIN_XOR()](/bin_xor/)

## Источник
http://pnv82.blogspot.ru/2011/05/firebird-25.html
http://ibexpert.net/ibe/index.php?n=Doc.NewInFirebird25
