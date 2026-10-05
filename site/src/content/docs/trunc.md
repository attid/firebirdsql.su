---
title: "TRUNC()"
old_id: trunc
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# TRUNC()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
TRUNC( < аргумент > , < знаков > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | [Числовое выражение](/tipy_dannyx/) |
| < знаков > | [INTEGER](/tipy_dannyx/) |
| Возвращает | [INTEGER, BIGINT или DOUBLE](/tipy_dannyx/) |

## Описание
Функция TRUNC() возвращает результат округления числа < аргумент > до < знаков > знаков после запятой *в меньшую по модулю сторону*. Если число < знаков > отрицательное, то округление идет до < знаков > знаков перед запятой.

⚠️ Чтобы пользоваться этой функцией в Firebird версии младше 2.1, её небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "fbudf".
```sql
DECLARE EXTERNAL FUNCTION TRUNC
    INTEGER BY DESCRIPTOR,
    INTEGER BY DESCRIPTOR
RETURNS PARAMETER 2
ENTRY_POINT 'fbtruncate' MODULE_NAME 'fbudf';
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION TRUNC
    INTEGER BY DESCRIPTOR,
    INTEGER BY DESCRIPTOR
RETURNS PARAMETER 2
ENTRY_POINT 'fbtruncate' MODULE_NAME 'SYSTEM';
```

## Пример
```sql
SELECT TRUNC(1111.23456, 2), TRUNC(1.23456, 0), TRUNC(1111.23456, -2) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [ROUND()](/round/)

## Источник
langref.pdf
