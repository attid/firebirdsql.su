# CREATE PACKAGE

## Доступно в
DSQL

## Формат
```sql
CREATE PACKAGE package_name
[<rights clause>]                            
AS
BEGIN
  [<package_item> ...]
END

<rights clause> ::=
  SQL SECURITY {DEFINER | INVOKER}  

<package_item> ::=
    <function_decl>; 
  | <procedure_decl>;
                            
<function_decl> ::=
  FUNCTION func_name [(<in_params>)]
  RETURNS <type> [NOT NULL] [COLLATE collation] 
  [DETERMINISTIC]   
                            
<procedure_decl> ::=
  PROCEDURE proc_name [(<in_params>)]
  [RETURNS (<out_params>)]                           

<in_params> ::= <inparam> [, <inparam> ...]

<inparam> ::= <param_decl> [{= | DEFAULT} <value>]  
                                                        
<value> ::=  {literal | NULL | context_var}

<out_params> ::= <outparam> [, <outparam> ...]

<outparam>  ::=  <param_decl> 
                    
<param_decl> ::= paramname <type> [NOT NULL] [COLLATE collation]

<type> ::= <datatype> | [TYPE OF] domain_name | TYPE OF COLUMN rel.col
                    
<datatype> ::= 
    <scalar_datatype> | <blob_datatype>
```

## Описание
Оператор `CREATE PACKAGE` предназначен для создания заголовка пакета, определяющего его открытый интерфейс. Имя пакета должно быть уникальным среди всех пакетов базы данных и может содержать до 63 символов.

Необязательное предложение `SQL SECURITY` задает контекст привилегий выполнения для всех процедур и функций пакета: `INVOKER` (по умолчанию) выполняет подпрограммы с правами вызывающего пользователя, а `DEFINER` — с правами владельца пакета, дополненными привилегиями, выданными самому пакету через `GRANT`. Переопределять привилегии выполнения для отдельных процедур или функций внутри пакета запрещено.

В отличие от отдельных хранимых процедур и функций, существующих в глобальном пространстве имен базы данных, пакет позволяет логически объединять связанные подпрограммы. Процедуры и функции, объявленные в заголовке пакета, доступны извне через составное имя вида `package_name.proc_name` или `package_name.func_name`. Механизм пакетов разделяет заголовок и тело (`CREATE PACKAGE BODY`): подпрограммы, определенные только в теле и не объявленные в заголовке, остаются приватными и недоступны снаружи. Кроме того, если имя подпрограммы пакета совпадает с именем глобальной процедуры или функции, внутри пакета всегда вызывается локальная подпрограмма пакета, а не глобальная.

## Пример
```sql
CREATE PACKAGE APP_SECURITY
  SQL SECURITY DEFINER
AS
BEGIN
  FUNCTION CHECK_USER_ACCESS(
    USER_NAME VARCHAR(63) NOT NULL,
    ROLE_NAME VARCHAR(63) DEFAULT 'GUEST'
  ) RETURNS BOOLEAN DETERMINISTIC;

  PROCEDURE LOG_EVENT(
    EVENT_TYPE VARCHAR(32) NOT NULL,
    DETAILS BLOB SUB_TYPE TEXT
  );

  PROCEDURE GET_USER_ROLES(
    USER_NAME VARCHAR(63) NOT NULL
  ) RETURNS (
    ROLE_ID INTEGER,
    ROLE_NAME VARCHAR(63)
  );
END
```
