---
title: "having"
old_id: having
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# having

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

having

## Описание

Так же, как и предложение WHERE ограничивает строки в наборе данных, теми которые удовлетворяют условию поиска, с той разницей, что предложение HAVING накладывает ограничения на агрегированные строки сгруппированного набора. Предложение HAVING не является обязательным и может быть использовано только в сочетании с предложением GROUP BY

## Пример

Какие продавцы сумели в 1998-м году обслужить больше пяти городов в одной стране?
```sql
SELECT DISTINCT EmployeeID
FROM Orders
WHERE Year (Orderdate) = 1998
GROUP BY EmployeeID, ShipCountry
HAVING	Count (DISTINCT Shipcity) > 5
```
