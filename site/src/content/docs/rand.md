---
title: "RAND()"
old_id: rand
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# RAND()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
RAND()
```
| Аргумент | Описание |
|---|---|
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) |

## Описание
Функция RAND() возвращает псевдослучайное число, равномерно распределенное в интервале от [0..1].

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее необходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION RAND
RETURNS 
  DOUBLE PRECISION BY VALUE
ENTRY_POINT 'IB_UDF_rand' MODULE_NAME 'ib_udf';
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION RAND
RETURNS 
  DOUBLE PRECISION BY VALUE
ENTRY_POINT 'IB_UDF_rand' MODULE_NAME 'SYSTEM';
```

## Пример
1) Псевдослучайное число в интервале [0..1]
```sql
SELECT RAND() FROM RDB$DATABASE
```

2) Псевдослучайное число в интервале [1..100]
```sql
SELECT TRUNC(RAND() * 100) FROM RDB$DATABASE
```

3) Псевдослучайное число в интервале [1..123456]
```sql
SELECT TRUNC(RAND() * 123456) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [TRUNC()](/trunc/)

## Источник
langref.pdf
