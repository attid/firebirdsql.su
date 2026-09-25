---
title: "ASIN()"
old_id: asin
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ASIN()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ASIN( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) в интервале от -1..+1 |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) арккосинус числа в радианах |

## Описание
Функция ASIN возвращает(в радинах) арксинус числа, переданного в качестве параметра < аргумент >, значение которого должно находиться в интервале -1..1.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ASIN
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_asin" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ASIN
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "asin" MODULE_NAME SYSTEM;
```

## Пример
Допустим, существует таблица WND_PARAMS с доменами ID [INTEGER](/tipy_dannyx/), DIAG  [DOUBLE PRECISION](/tipy_dannyx/) - диагональ прямоугольника и  SIN_DIAG [DOUBLE PRECISION](/tipy_dannyx/), который хранит отношение высоты прямоугольника к его диагонали (математически - синус угла наклона диагонали к ширине). 

Требуется выбрать из таблицы все записи, указав высоту прямоугольника.

1) [DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/)
```sql
SELECT W.ID, (W.DIAG * ASIN(W.SIN_DIAG)) AS HEIGHT
FROM   WND W
```

2) [PSQL](/raznovidnosti_jazyka_sql/)
```sql
SET TERM !!!;

CREATE OR ALTER PROCEDURE WND_HEIGHTS RETURNS (
   W_ID     INTEGER
  ,W_HEIGHT DOUBLE PRECISION
)AS
  DECLARE VARIABLE P_DIAG     DOUBLE PRECISION;
  DECLARE VARIABLE P_SIN_DIAG DOUBLE PRECISION;
BEGIN
  FOR
    SELECT W.ID, W.DIAG, W.COS_DIAG
    FROM   WND W
    INTO   :W_ID, :P_DIAG, :P_SIN_DIAG
  DO
  BEGIN
    W_HEIGHT = :W_DIAG * ASIN(:P_SIN_DIAG);
    SUSPEND;
  END
END !!!

SET TERM ; !!!
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
