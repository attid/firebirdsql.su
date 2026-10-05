---
title: "CREATE EXCEPTION"
old_id: create_exception
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# CREATE EXCEPTION

## Версии сервера
Firebird v0.9       Firebird v1.0       Firebird v1.5       Firebird v2.0 

## Формат
{CREATE [OR ALTER] | RECREATE} EXCEPTION *name* **'message'**;

## Описание
Создает исключение определяемое пользователем с именем *name* и с текстом **'message'** для дальнейшего вызова этого исключения в хранимых процедурах и триггерах.
Доступно в DSQL и в ISQL.

## Пример
для примера можно изучить процедуру SHIP_ORDER базы employee.

создание исключения
CREATE EXCEPTION ORDER_ALREADY_SHIPPED 'Order status is "shipped."';

вызов по условию
IF(ord_stat = 'shipped')THEN
BEGIN
EXCEPTION order_already_shipped;
END

вызов по условию с заменой сообщения
IF(ord_stat = 'shipped')THEN
BEGIN
EXCEPTION order_already_shipped 'Order status is "'||ord_stat||'"';
END

подмена стандартного исключения
CREATE EXCEPTION COUNTRY_EXIST '';
CREATE PROCEDURE ADD_COUNTRY  
as
begin
insert into country (country, currency)
values ('Canada', 'CdnDlr');
when sqlcode -803 do exception COUNTRY_EXIST 'Такая страна уже добавлена!';
end

## См. также
[EXCEPTION](/exception/),  [DROP EXCEPTION](/drop_exception/),  [ALTER EXCEPTION](/alter_exception/),  RECREATE EXCEPTION

## Источник
%Firebird%\doc\sql.extensions\README.exception_handling
