---
title: "CREATE DOMAIN"
old_id: create_domain
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# CREATE DOMAIN

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
CREATE DOMAIN domain [AS] *<datetype>*\
[DEFAULT {literal | NULL | USER}]\
[NOT NULL] [CHECK (*<dom_search_condition>*)]\
[COLLATE collation];

<datatype> = {SMALLINT|INTEGER|FLOAT|DOUBLE PRECISION}[*<array_dim>*]\
|  |  |  |  |
|---|---|---|---|
| {DATE | TIME | TIMESTAMP}[*<array_dim>*]<br> |  |
| {DECIMAL | NUMERIC} [(precision [, scale])] [*<array_dim>*]<br> |  |  |
| {CHAR | CHARACTER | CHARACTER VARYING | VARCHAR} [(int)] [*<array_dim>*] [CHARACTER SET charname]<br> |
| {NCHAR | NATIONAL CHARACTER | NATIONAL CHAR} [VARYING] [(int)] [*<array_dim>*]<br> |  |
| BLOB [SUB_TYPE {int | subtype_name}] [SEGMENT SIZE int] [CHARACTER SET charname]<br> |  |  |
| BLOB [(seglen [, subtype])]<br> |  |  |  |

<array_dim> = **[**[x:]y [, [x:]y …]**]**
подробнее смотреть [tipy_dannyx](/tipy_dannyx/)
<dom_search_condition> = {\
VALUE <operator> value\
|  |
|---|
| VALUE [NOT] BETWEEN value AND value<br> |
| VALUE [NOT] LIKE value [ESCAPE value]<br> |
| VALUE [NOT] IN (value [, value …])<br> |
| VALUE IS [NOT] NULL<br> |
| VALUE [NOT] CONTAINING value<br> |
| VALUE [NOT] STARTING [WITH] value<br> |
| (*<dom_search_condition>*)<br> |
| NOT *<dom_search_condition>*<br> |
| *<dom_search_condition>* OR *<dom_search_condition>*<br> |
| *<dom_search_condition>* AND *<dom_search_condition>*<br> |
}
<operator> = `{= | < | > | <= | >= | !< | !> | <> | !=}`
## Описание
Оператор, создающий домен <наименование> в текущей БД с заданым <тип данных>.

Создать домен может любой, подключившийся к БД.

FIXME Домены используются при создании таблиц, а начиная с Firibird 2.1 также в процедурах и триггерах.

## Пример
CREATE DOMAIN PONUMBER AS CHAR(8) CHARACTER SET NONE CHECK (VALUE STARTING WITH 'V') COLLATE NONE;

CREATE DOMAIN EMPNO AS SMALLINT;

## См. также
[DROP DOMAIN](/drop_domain/),  [ALTER DOMAIN](/alter_domain/)

## Источник
docs
