---
title: "ABS()"
old_id: abs
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ABS()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ABS( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) |

## Описание
Функция ABS возвращает абсолютное значение числа, переданного в качестве параметра < аргумент >.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ABS
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_abs" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ABS
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_abs" MODULE_NAME SYSTEM;
```

## Пример
Допустим, существует таблица CUSTOMERS с доменами ID [INTEGER](/tipy_dannyx/) и AMOUNT [DOUBLE PRECISION](/tipy_dannyx/), который может быть отрицательным.

Требуется выбрать из таблицы все записи, указав абсолютное значение домена AMOUNT.

1) [DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/)
```sql
SELECT ABS(C.AMOUNT)
FROM   CUSTOMERS C
```

2) [PSQL](/raznovidnosti_jazyka_sql/)
```sql
SET TERM !!!;

CREATE OR ALTER PROCEDURE CUST_AMOUNT RETURNS (
   CUST_ID INTEGER
  ,AMOUNT  DOUBLE PRECISION
)AS
BEGIN
  FOR
    SELECT C.ID, C.AMOUNT
    FROM   CUSTOMERS C
    INTO   :CUST_ID, :AMOUNT
  DO
    BEGIN
    AMOUNT = ABS(:AMOUNT);
    SUSPEND;
    END
END !!!

SET TERM ; !!!
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
