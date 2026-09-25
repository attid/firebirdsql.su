---
title: "POWER()"
old_id: power
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# POWER()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
POWER( < аргумент > , < степень > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | [DOUBLE PRECISION](/tipy_dannyx/) |
| < степень > | [DOUBLE PRECISION](/tipy_dannyx/) |
| Возвращает | [DOUBLE PRECISION](/tipy_dannyx/) |

## Описание
Функция POWER() возвращает результат возведения числа < аргумент > в степень < степень >.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "fbudf".
```sql
DECLARE EXTERNAL FUNCTION POWER
    DOUBLE PRECISION BY DESCRIPTOR,
    DOUBLE PRECISION BY DESCRIPTOR,
    DOUBLE PRECISION BY DESCRIPTOR
RETURNS PARAMETER 3
ENTRY_POINT 'power' MODULE_NAME 'fbudf';
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION POWER
    DOUBLE PRECISION BY DESCRIPTOR,
    DOUBLE PRECISION BY DESCRIPTOR,
    DOUBLE PRECISION BY DESCRIPTOR
RETURNS PARAMETER 3
ENTRY_POINT 'power' MODULE_NAME 'SYSTEM';
```

## Пример
```sql
SELECT POWER(2, 0), POWER(2,1), POWER(2,2), POWER(2,3), POWER(2,4), POWER(2,5) FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
