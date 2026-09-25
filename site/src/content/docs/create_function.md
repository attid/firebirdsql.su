---
title: "CREATE FUNCTION"
old_id: create_function
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "3.0"
  until: 
  deprecated: false
---

# CREATE FUNCTION

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
CREATE FUNCTION name ( [ <inparam> ...] )
  RETURNS <ret_type>
  [DETERMINISTIC]
  [SQL SECURITY {INVOKER | DEFINER}]
  AS <module body>

<module body> ::=
    <psql routine body>
  | EXTERNAL NAME 'extname' ENGINE engine
```

## Описание
Оператор `CREATE FUNCTION` создаёт новую хранимую функцию — подпрограмму, которая принимает входные параметры и возвращает одиночное значение, поэтому её можно вызывать прямо в SQL-выражениях (в списке выбора `SELECT`, в условиях, в присваиваниях). В этом её главное отличие от хранимой процедуры: процедура выполняется оператором `EXECUTE PROCEDURE` и возвращает данные через выходные параметры, тогда как функция обязана вернуть значение через `RETURNS` и встраивается в выражения. От устаревших внешних функций (UDF, объявляемых через `DECLARE EXTERNAL FUNCTION`) хранимая функция отличается тем, что её тело пишется на PSQL и исполняется внутри сервера; тем же оператором можно создать и внешнюю функцию на базе UDR через предложение `EXTERNAL NAME ... ENGINE ...`.

Имя хранимой функции (до 63 символов) должно быть уникальным среди имён всех хранимых функций и внешних (UDF) функций; для подпрограмм достаточно уникальности в рамках охватывающего модуля. Желательно избегать совпадений с именами функций в PSQL-пакетах: из пакета нельзя вызвать одноимённую функцию глобального пространства имён — всегда будет вызвана функция пакета.

`CREATE FUNCTION` — составной оператор из заголовка и тела. Заголовок определяет имя, объявляет входные параметры и тип возвращаемого значения. Тело состоит из необязательных объявлений локальных переменных, подпрограмм и именованных курсоров и одного или нескольких блоков операторов, заключённых во внешний блок `BEGIN ... END`.

Входные параметры передаются по значению: их изменение внутри функции не влияет на аргументы вызывающей программы. Для параметра можно указать `NOT NULL`, порядок сортировки `COLLATE` и значение по умолчанию через `=` или `DEFAULT`. Тип параметра и возвращаемого значения задаётся типом данных SQL, доменом (`TYPE OF domain`) либо типом столбца таблицы или представления (`TYPE OF COLUMN rel.col`). Предложение `DETERMINISTIC` помечает функцию как детерминированную, а `SQL SECURITY` задаёт контекст прав доступа.

В `isql` и подобных редакторах из-за конфликта точек с запятой внутри тела с терминатором оператора используйте `SET TERM`.

## Пример
```sql
SET TERM ^ ;

CREATE FUNCTION FN_FULL_NAME (
    FIRST_NAME  TYPE OF COLUMN EMPLOYEE.FIRST_NAME,
    LAST_NAME   TYPE OF COLUMN EMPLOYEE.LAST_NAME
)
RETURNS VARCHAR(85) NOT NULL
AS
BEGIN
  RETURN LAST_NAME || ', ' || FIRST_NAME;
END^

SET TERM ; ^

-- Вызов функции в SQL-выражении
SELECT FN_FULL_NAME(FIRST_NAME, LAST_NAME) AS FULL_NAME
FROM EMPLOYEE;
```

## См. также
[CREATE PROCEDURE](/create_procedure/), [CREATE PACKAGE](/create_package/), [EXECUTE FUNCTION](/execute_statement/), [UDF](/udf/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
