---
title: "TRIM"
old_id: trim
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# TRIM

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
TRIM ([ [ *<trim specification>* ] [ *<trim character>* ] FROM ] *<value expression>* )

| *<trim specification>* |  |
|---|---|
| LEADING | c начала строки |
| TRAILING | с конца строки |
| BOTH | с обих сторон строки |

## Описание
Обрезает заданые символы слева\справа или с обоих концов строки

если *<trim specification>* не заданна, используется по умолчанию BOTH

если *<trim character>* не заданна, используется по умолчанию ' '(пробел).

ключевое слово FROM используется тогда, и только тогда, когда в выражении присутствует <trim specification> и\или <trim character>

<value expression> - выражение, символы которого нужно обрезать

## Пример
```sql
select rdb$relation_name, trim(leading 'RDB$' from rdb$relation_name)
  from rdb$relations
 where rdb$relation_name starting with 'RDB$'
```
```sql
select trim(rdb$relation_name) || ' is a system table'
from rdb$relations
where rdb$system_flag = 1
```

## Смотри также
[LOWER()](/lower/), [UPPER()](/upper/), [CHAR_LENGTH()](/char_length/)

## Источник
Firebird_2_0\doc\sql.extensions\README.trim.txt
