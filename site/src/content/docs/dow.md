---
title: "DOW()"
old_id: dow
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# DOW()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
DOW( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | [TIMESTAMP](/tipy_dannyx/) значение даты, для которой нужно вернуть день недели |
| Возвращает | [VARCHAR](/tipy_dannyx/) имя дня недели для даты, переданной в качестве параметра |

## Описание
Функция DOW возвращает текстовое имя дня недели для даты, переданной в качестве параметра < аргумент >.

Для того, чтобы воспользоваться функцией, необходимо подключить ее к базе данных, как UDF

⚠️ подобный функционал можно получить встроенным оператором [EXTRACT](/extract/)(WEEKDAY FROM value)

## Объявление
```sql
DECLARE EXTERNAL FUNCTION DOW
    TIMESTAMP,
    VARCHAR(15)
RETURNS PARAMETER 2
ENTRY_POINT 'DOW' MODULE_NAME 'fbudf';
```

## Пример
```sql
SELECT DOW(CURRENT_TIMESTAMP) AS DD FROM RDB$DATABASE
```

## См. также
UDF, [Встроенные функции](/vstroennye_funkcii/), [EXTRACT](/extract/)

## Источник
