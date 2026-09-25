---
title: "COMMENT"
old_id: comment
section: glossary
type: term
firebird:
  since: "2.0"
  until: 
  deprecated: false
---

# COMMENT

## Формат
```
COMMENT ON
{ DATABASE IS {'<текст>' | NULL}
| <базовый тип> <имя> IS {'<текст>' | NULL}
| COLUMN <таблица>.<столбец> IS
{'<текст>' | NULL}
| PARAMETER <процедура>.<параметр> IS
{'<текст>' | NULL} };
<базовый тип> ::=
{ DOMAIN
| TABLE
| VIEW
| PROCEDURE
| TRIGGER
| EXTERNAL FUNCTION
| FILTER
| EXCEPTION
| GENERATOR
| SEQUENCE
| INDEX
| ROLE
| CHARACTER SET
| COLLATION
}
```

## Описание

Оператор COMMENT позволяет создавать примечания, комментарии, для объектов базы данных. Если текст примечания задать в виде двух подряд идущих апострофов '', то это равносильно заданию NULL, то есть удалению существующего примечания.

## Пример
```sql
  COMMENT ON TABLE EMPLOYEE IS '"Employee" table'
```
