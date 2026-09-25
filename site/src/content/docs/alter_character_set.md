---
title: "ALTER CHARACTER SET"
old_id: alter_character_set
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# ALTER CHARACTER SET
Оператор DDL, который изменяет свойство "CHARACTER SET".

## Версии сервера
| 2.5 | 3.0 |
|---|---|
| + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
ALTER CHARACTER SET <charset_name>
  SET DEFAULT COLLATION <collation_name>;
```  

## Описание
Позволяет изменить сопоставление набора символов. 

Заданное по умолчанию сопоставление используется, когда столбцы таблицы созданы с данной кодировкой (явной или неявной через кодировку по умолчанию базы данных) без определенного сопоставления. Строковые константы также используют заданное по умолчанию сопоставление кодировки подключения.
## Пример
```sql
CREATE DATABASE 'peoples.fdb'
    DEFAULT CHARACTER SET WIN1252;
 
ALTER CHARACTER SET WIN1252
    SET DEFAULT COLLATION WIN_PTBR;
 
CREATE TABLE PEOPLES (
    ID INTEGER,
    NAME VARCHAR(50)    -- will use the database default character set and the WIN1252 default collation
);
 
INSERT INTO PEOPLES VALUES (1, 'adriano');
INSERT INTO PEOPLES VALUES (2, 'ADRIANO');
 
-- will retrieve both records as WIN_PTBR is case insensitive
SELECT * FROM PEOPLES WHERE NAME LIKE 'A%';
```

## См. также

## Источник
http://wiki.firebirdsql.org/wiki/index.php?page=ALTER+CHARACTER+SET
