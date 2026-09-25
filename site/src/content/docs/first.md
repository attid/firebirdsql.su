---
title: "FIRST"
old_id: first
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# FIRST

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | + | + | + | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
FIRST (m) SКlP (n) 

## Описание
Необязательные ключевые слова FIRST (m) и/или SКIP (п), если присутствуют, предшествуют всем друrим спецификациям. Они задают режим выбора первых m строк в упорядоченном наборе и игнорирования первых n строк в упорядоченном наборе, 
соответственно. 

## Пример
```sql
  SELECT FIRST 5 SKIP 10 * FROM employee e
```

## См. также
[SELECT](/select/)

## Источник
Борри Х. Firebird:Руководство разработчика баз данных
