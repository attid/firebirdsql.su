---
title: "ASCII_VAL()"
old_id: ascii_val
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# ASCII_VAL()

## Версии сервера
|  | 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|
| Как UDF | Да | Да | Да | Да | Да | Да | - | - | - |
| Как встроенная функция | - | - | - | - | - | - | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),   [ISQL](/raznovidnosti_jazyka_sql/),   [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ASCII_VAL( < аргумент > )
```
| Аргумент | Описание |
|---|---|
| < аргумент > | [CHAR(1)](/tipy_dannyx/) одиночный символ |
| Возвращает | [INTEGER](/tipy_dannyx/) - код символа в таблице символов кодировки. |

## Описание
Функция ASCII_VAL возвращает код символа в таблице символов, переданного в качестве параметра < аргумент >.

⚠️ В Firebird версии младше 2.1 для того, чтобы пользоваться этой функцией, ее небходимо подключить к базе данных как UDF.

## Объявление
1. В Firebird версии младше 2.1 функция объявляется как UDF в внешнем модуле "ib_udf".
```sql
DECLARE EXTERNAL FUNCTION ASCII_VAL
  CHAR(1)
RETURNS
  INTEGER BY VALUE
ENTRY_POINT "IB_UDF_ascii_val" MODULE_NAME "ib_udf";
```

2. В Firebird версии 2.1 и старше является встроенной функцией при соглашении объявления ее как:
```sql
DECLARE EXTERNAL FUNCTION ASCII_VAL
  CHAR(1)
RETURNS
  INTEGER BY VALUE
ENTRY_POINT "ascii_val" MODULE_NAME SYSTEM;
```

## Пример
Допустим, существует таблица CUSTOMERS с доменами ID [INTEGER](/tipy_dannyx/) и NAME [VARCHAR(80)](/tipy_dannyx/).

Требуется выбрать из таблицы все записи, упорядочив их по алфавиту, учтя при этом ошибки ввода данных, когда оператор ввода мог ошибиться и не может визуально заметить свою ошибку (например, отличить латинский символ "C" и русский символ "С", ввиду расположения их на клавиатуре).

[PSQL](/raznovidnosti_jazyka_sql/)
```sql
SET TERM !!!;

CREATE OR ALTER PROCEDURE CUST_ORDER_LIST RETURNS (
   ORDER_ID  INTEGER
  ,CUST_NAME VARCHAR(80)
)AS
BEGIN
  FOR
    SELECT C.NAME
    FROM   CUSTOMERS C
    INTO   :CUST_NAME
  DO
    BEGIN
    ORDER_ID = ASCII_VAL( SUBSTRING(:CUST_NAME FROM 1 FOR 1) );
    SUSPEND;
    END
END !!!

SET TERM ; !!!
```

И далее мы вибираем упорядоченные записи :
```sql
SELECT PR.ORDER_ID, PR CUT_NAME 
FROM   CUST_ORDER_LIST PR
ORDER BY PR.ORDER_ID
```

## См. также
[SUBSTRING()](/substring/), UDF, [Встроенные функции](/vstroennye_funkcii/)

## Источник
langref.pdf
