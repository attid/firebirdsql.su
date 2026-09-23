---
title: "ROUND()"
old_id: round
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ROUND()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ROUND( < аргумент > , < знаков > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | [Числовое выражение](/tipy_dannyx/) |
| < знаков > | [INTEGER](/tipy_dannyx/) |
| Возвращает | [INTEGER, BIGINT или DOUBLE](/tipy_dannyx/) |
## Описание
Функция ROUND() возвращает результат округления числа < аргумент > до < знаков > знаков после запятой *в ближайшую сторону*. Если число < знаков > отрицательное, то округление идет до < знаков > знаков перед запятой.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ROUND
    INTEGER BY DESCRIPTOR,
    INTEGER BY DESCRIPTOR
RETURNS PARAMETER 2
ENTRY_POINT 'fbround' MODULE_NAME 'fbudf';
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ROUND
    INTEGER BY DESCRIPTOR,
    INTEGER BY DESCRIPTOR
RETURNS PARAMETER 2
ENTRY_POINT 'fbround' MODULE_NAME 'SYSTEM';
```

## Пример
```sql
SELECT ROUND(1111.23456, 2), ROUND(1.23456, 0), ROUND(1111.23456, -2) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [TRUNC()](/trunc/)

## Источник
langref.pdf
