---
title: "NEXT VALUE FOR"
old_id: next_value_for
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# NEXT VALUE FOR

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | + | + | + | + | + | + |

## Формат
```
NEXT VALUE FOR <sequence_name>
```
| Аргумент | Описание |
|---|---|
| sequence_name | Имя существующей последовательности (генератора). |
## Описание
Функция работает аналогично gen_id(<sequence_name>, 1): увеличивает значение последовательности <sequence_name> на 1 и возвращает его.

## Пример
```sql
  SELECT NEXT VALUE FOR <sequence_name> FROM RDB$DATABASE
```

PSQL:
```sql
  <variable> = NEXT VALUE FOR <sequence_name>;
```

## См. также
[GEN_ID](/gen_id/)
