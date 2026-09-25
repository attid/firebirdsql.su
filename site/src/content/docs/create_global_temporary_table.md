---
title: "CREATE GLOBAL TEMPORARY TABLE"
old_id: create_global_temporary_table
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# CREATE GLOBAL TEMPORARY TABLE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/)

## Формат
Global Temporary Tables (GTTs)

Global temporary tables have persistent metadata, but their contents are transaction-bound (the default) or connection-bound. Every transaction or connection has its own private instance of a GTT, isolated from all the others. Instances are only created if and when the GTT is referenced, and destroyed upon transaction end or disconnection. To modify or remove a GTT's metadata, ALTER TABLE and DROP TABLE can be used.

```sql
CREATE GLOBAL TEMPORARY TABLE name
   (column_def [, column_def | table_constraint ...])
   [ON COMMIT {DELETE | PRESERVE} ROWS]
```
## Описание
/*пока запощу оригинал - но это времмено, скоро постараюсь перевести на русский язык*/

```sql
ON COMMIT DELETE ROWS
```
создает временную таблицу в которой записи хранятся до следующего COMMIT'a. (После COMMIT'а табличка становится чистой)
```sql
ON COMMIT PRESERVE ROWS
```
создает временную таблицу в которой записи хранятся до потери соединения. (После RECONNECT'a табличка становится чистой) 

```sql
An EXTERNAL [FILE]
```
clause is not allowed on a global temporary table. 

Restrictions: GTTs can be “dressed up” with all the features and paraphernalia of ordinary tables (keys, references, indices, triggers…) but there are a few restrictions: 

GTTs and regular tables cannot reference one another.

A connection-bound (“PRESERVE ROWS”) GTT cannot reference a transaction-bound (“DELETE ROWS”) GTT. 

Domain constraints cannot reference any GTT.

The destruction of a GTT instance at the end of its life cycle does not cause any before/after delete triggers to fire.

## Пример
```sql
create global temporary table MyConnGTT (
  id int not null primary key,
  txt varchar(32),
  ts timestamp default current_timestamp
)
on commit preserve rows;

commit;

create global temporary table MyTxGTT (
  id int not null primary key,
  parent_id int not null references MyConnGTT(id),
  txt varchar(32),
  ts timestamp default current_timestamp
);

commit;
```

## Замечание
В существующей базе данных не всегда легко отличить обычную табличку от GTT, или "GTT со временем жизни транзакция" от "GTT со временем жизни коннект", что бы найти отличия в таблиц, используйте этот запрос:
```sql
select t.rdb$type_name
  from rdb$relations r
  join rdb$types t on r.rdb$relation_type = t.rdb$type
  where t.rdb$field_name = 'RDB$RELATION_TYPE'
  and r.rdb$relation_name = 'TABLENAME'
```

Или, для просмотра всех Ваших зависимостей:
```sql
select r.rdb$relation_name, t.rdb$type_name
  from rdb$relations r
  join rdb$types t on r.rdb$relation_type = t.rdb$type
  where t.rdb$field_name = 'RDB$RELATION_TYPE'
  and coalesce (r.rdb$system_flag, 0) = 0
```
## См. также

## Источник
http://www.firebirdsql.org/refdocs/langrefupd21-ddl-table.html
