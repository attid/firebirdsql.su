---
title: "EXCEPTION"
old_id: exception
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# EXCEPTION

## Версии сервера
Firebird 1.5   Firebird 2.0 

## Формат
EXCEPTION [исключение [сообщение]];

## Описание
Возбуждение пользовательского исключения или повторный вызов исключения.

⚠️ В версии 1.5 максимальная длина сообщения составляет 78 байт. Начиная с версии 2.0 - 1021 байт.

## Пример
для примера можно изучить процедуру SHIP_ORDER базы employee.

создание исключения (полный синтаксис см. [CREATE EXCEPTION](/create_exception/))
CREATE EXCEPTION ORDER_ALREADY_SHIPPED 'Order status is "shipped."';

вызов по условию
IF (ord_stat = 'shipped') THEN
BEGIN
EXCEPTION order_already_shipped;
END

вызов по условию с заменой сообщения
IF (ord_stat = 'shipped') THEN
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
[CREATE EXCEPTION](/create_exception/), [DROP EXCEPTION](/drop_exception/),  [ALTER EXCEPTION](/alter_exception/),  RECREATE EXCEPTION, [GDSCODE](/gdscode/), SQLCODE, [GDSCODES](/gdscodes/)

## Источник
%Firebird%\doc\sql.extensions\README.exception_handling 

https://www.firebirdsql.org/file/documentation/reference_manuals/Firebird_Language_Reference_RUS.pdf

https://www.firebirdsql.org/file/documentation/reference_manuals/reference_material/Firebird-2.5-LangRef-Update.pdf
