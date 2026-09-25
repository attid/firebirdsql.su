---
title: "MERGE"
old_id: merge
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# MERGE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
  MERGE
   INTO <table or view> [ [AS] <correlation name> ]
   USING <table or view or derived table> [ [AS] <correlation name> ]
   ON <condition>
   [ merge when matched ]
   [ merge when not matched ]
```
merge when matched
```sql
  WHEN MATCHED THEN
   UPDATE SET <assignment list>
```
merge when not matched
```sql
  WHEN NOT MATCHED THEN
   INSERT [ <left paren> <column list> <right paren> ]
    VALUES <left paren> <value list> <right paren>
```

## Описание
MERGE читает данные из исходной (USING) таблицы и вставляет([INSERT](/insert/)) или обновляет ([UPDATE](/update/)) данные в целевой (INTO) таблице, в зависимости от условия.

Должна присутствовать хотя бы одна из двух секций **[merge when matched]**или**[merge when not matched]**, при чем не более одного раза каждая.

## Пример
```sql
MERGE
   INTO customers c
   USING (SELECT * FROM customers_delta WHERE id > 10) cd
   ON (c.id = cd.id)
   WHEN MATCHED THEN
    UPDATE SET
     name = cd.name
   WHEN NOT MATCHED THEN
    INSERT (id, name)
     VALUES (cd.id, cd.name)
```

Замечание:
Выполняется [правое внешнее соединение](/join/) между таблицами, указанными в INTO и USING, по условию <condition>. Если слева запись есть, то производится обновление, иначе вставка. Если справа так же нет записей, соответствующих условию, то вставка не производится.

## См. также
[SELECT](/select/), [JOIN](/join/), [INSERT](/insert/), [UPDATE](/update/)

## Источник
%Firebird%\doc\sql.extensions\README.merge.txt

%Firebird%\doc\Firebird_v2.1.1.ReleaseNotes.pdf
