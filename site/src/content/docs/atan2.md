---
title: "ATAN2()"
old_id: atan2
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# ATAN2()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ATAN2( < аргумент1 >,  < аргумент2 >)
```
| Аргумент | Описание |
|---|---|
| < аргумент1 > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) |
| < аргумент2 > | Любой тип данных, приводимый к [DOUBLE PRECISION](/tipy_dannyx/) |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) арктангенс частного от деления < аргумент1 > / < аргумент2 >. Результат находится в промежутке от -Pi до Pi |

## Описание
Функция ATAN2 возвращает арктангенс частного, получаемого при делении переданных в качестве параметра < аргумент1 > на < аргумент2 >.

С точки зрения тригонометрии функция ATAN2 возвращает величину угла прямоугольного треугольника в радианах, для которого <аргумент1> - длинна противолежащего катета, а <аргумент2> - длинна прилежащего катета.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее необходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ATAN2
  DOUBLE PRECISION,
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "IB_UDF_atan2" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ATAN2
  DOUBLE PRECISION,
  DOUBLE PRECISION
RETURNS
  DOUBLE PRECISION BY VALUE
ENTRY_POINT "atan2" MODULE_NAME SYSTEM;
```

## Пример
```sql
SELECT W.ID, ATAN2(W.H1, W.H2) AS ARCTG
FROM   WND W
```

## См. также
UDF,  [ATAN()](/atan/),  [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
