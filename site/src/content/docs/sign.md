---
title: "SIGN()"
old_id: sign
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# SIGN()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
SIGN( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) |
| Возвращает | [INTEGER](/tipy_dannyx/) знак числа |

Результаты, возвращаемые функцией:
| Результат | Значение |
|---|---|
| -1 | Аргумент меньше нуля |
| 0 | Аргумент равен нулю |
| 1 | Аргумент больше нуля |

## Описание
Функция SIGN возвращает знак числа, переданного в качестве параметра < аргумент >.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION SIGN
  DOUBLE PRECISION
RETURNS
  INTEGER BY VALUE
ENTRY_POINT "IB_UDF_sign" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION SIGN
  DOUBLE PRECISION
RETURNS
  INTEGER BY VALUE
ENTRY_POINT "sign" MODULE_NAME SYSTEM;
```

## Пример
```sql
SELECT SIGN(-1.234), SIGN(0.000), SIGN(1.234) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [TRUNC()](/trunc/), [ROUND()](/round/)

## Источник
langref.pdf
