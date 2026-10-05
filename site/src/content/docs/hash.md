---
title: "HASH()"
old_id: hash
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# HASH()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
HASH( <string> )
```
| Аргумент | Описание |
|---|---|
| <string> | Столбец или выражение, которое приводится к строковому типу данных. |
| Результат | [BIGINT](/tipy_dannyx/) |
## Описание
Возвращает хэш от указанной строки, используя алгоритм ELF HASH.

[Встроенная функция](/vstroennye_funkcii/). Является не зарезервированным ключевым словом.

## Пример
```sql
  SELECT E.FULL_NAME, HASH(E.FULL_NAME) AS HASH FROM EMPLOYEE E
```

## См. также
[Встроенные функции](/vstroennye_funkcii/)

## Источник
http://www.firebirdsql.org/rlsnotesh/rlsnotes210.html#rnfb210-appx-A
