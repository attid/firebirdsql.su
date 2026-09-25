---
title: "SIN()"
old_id: sin
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# SIN()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
SIN( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) синус числа в радианах |

## Описание
Функция SIN возвращает (в радинах) синус угла, переданного в качестве параметра < аргумент > (в радианах).

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION SIN
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_sin" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION SIN
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "sin" MODULE_NAME SYSTEM;
```

## Пример
```sql
SELECT SIN(1.234) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [ASIN()](/asin/), [COS()](/cos/), [ACOS()](/acos/), [SINH()](/sinh/), [COSH()](/cosh/)

http://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%B3%D0%BE%D0%BD%D0%BE%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8

## Источник
langref.pdf
