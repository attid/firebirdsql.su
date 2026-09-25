# CREATE FUNCTION

## Доступно в
DSQL

## Формат
```sql
CREATE FUNCTION funcname [(<inparam> [, <inparam> ...])]
  RETURNS <type> [NOT NULL] [COLLATE collation]
  [DETERMINISTIC]
  <routine-body>
  
<inparam> ::= <param_decl> [{= | DEFAULT} <value>]  
                    
<value> ::= {<literal> | NULL | <context_var>}
                    
<param_decl> ::= paramname <type> [NOT NULL] [COLLATE collation]
                    
<type> ::=
    <datatype>
  | [TYPE OF] domain
  | TYPE OF COLUMN rel.col
                    
<routine-body> ::=
    <psql-routine-spec>
  | <external-routine-spec>
                    
<psql-routine-spec> ::=
  [<rights-clause>] <psql-routine-body>

<rights-clause> ::=
  SQL SECURITY {DEFINER | INVOKER}                    

<external-routine-spec> ::= 
  EXTERNAL NAME '<module-name>!<routine-name>[!<misc-info>]' ENGINE <engine>
  [AS <extbody>]
```

## Описание
Оператор `CREATE FUNCTION` предназначен для создания новой хранимой функции в базе данных.

Хранимая функция состоит из заголовка и тела. Заголовок определяет уникальное имя функции (до 63 символов), список входных параметров и обязательное предложение `RETURNS`, задающее тип возвращаемого скалярного значения. Входные параметры передаются по значению и могут содержать ограничения `NOT NULL`, параметры сортировки `COLLATE` и значения по умолчанию (`DEFAULT`). Необязательное ключевое слово `DETERMINISTIC` сообщает оптимизатору, что результат функции зависит только от входных аргументов. Предложение `SQL SECURITY` позволяет настроить контекст безопасности (`DEFINER` или `INVOKER`).

Тело функции может быть написано на языке PSQL (блок `BEGIN ... END`, содержащий объявления переменных, курсоров, подпрограмм и исполняемые операторы) либо реализовано как внешняя подпрограмма (UDR) с указанием модуля и движка (`ENGINE`).

В отличие от хранимых процедур, которые могут возвращать множество параметров или наборы строк, функция возвращает ровно одно скалярное значение и может вызываться непосредственно внутри SQL-выражений (в блоках `SELECT`, `WHERE`, `ORDER BY` и др.). В отличие от устаревших внешних функций (UDF), функции на PSQL компилируются и хранятся внутри базы данных, полностью безопасны, поддерживают типизацию через домены и столбцы (`TYPE OF`), а также контекст прав пользователя.

## Пример
```sql
SET TERM ^ ;

CREATE FUNCTION FN_CALC_DISCOUNT (
    SUM_TOTAL TYPE OF COLUMN INVOICES.AMOUNT,
    DISCOUNT_PERCENT NUMERIC(5, 2) DEFAULT 0.00 NOT NULL
)
RETURNS NUMERIC(15, 2)
DETERMINISTIC
SQL SECURITY DEFINER
AS
BEGIN
    IF (SUM_TOTAL IS NULL OR SUM_TOTAL <= 0) THEN
        RETURN 0.00;
        
    RETURN ROUND(SUM_TOTAL * (1.00 - DISCOUNT_PERCENT / 100.00), 2);
END^

SET TERM ; ^
```
