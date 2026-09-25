---
title: "ACOS()"
old_id: acos
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ACOS()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ACOS( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) в интервале от -1..+1 |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) арккосинус числа в радианах |

## Описание
Функция ACOS возвращает(в радинах) арккосинус числа, переданного в качестве параметра < аргумент >, значение которого должно находиться в интервале -1..1.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ACOS
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_acos" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ACOS
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "acos" MODULE_NAME SYSTEM;
```

## Пример
Допустим, существует таблица WND_PARAMS с доменами ID [INTEGER](/tipy_dannyx/), DIAG  [DOUBLE PRECISION](/tipy_dannyx/) - диагональ прямоугольника и  COS_DIAG [DOUBLE PRECISION](/tipy_dannyx/), который хранит отношение ширины прямоугольника к его диагонали (математически - косинус угла наклона диагонали). 

Требуется выбрать из таблицы все записи, указав ширину прямоугольника.

1) [DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/)
```sql
SELECT W.ID, (W.DIAG * ACOS(W.COS_DIAG)) AS WIDTH
FROM   WND W
```

2) [PSQL](/raznovidnosti_jazyka_sql/)
```sql
SET TERM !!!;

CREATE OR ALTER PROCEDURE WND_WIDTHS RETURNS (
   W_ID     INTEGER
  ,W_WIDTH  DOUBLE PRECISION
)AS
  DECLARE VARIABLE P_DIAG     DOUBLE PRECISION;
  DECLARE VARIABLE P_COS_DIAG DOUBLE PRECISION;
BEGIN
  FOR
    SELECT W.ID, W.DIAG, W.COS_DIAG
    FROM   WND W
    INTO   :W_ID, :P_DIAG, :P_COS_DIAG
  DO
  BEGIN
    W_WIDTH = :W_DIAG * ACOS(:P_COS_DIAG);
    SUSPEND;
  END
END !!!

SET TERM ; !!!
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
