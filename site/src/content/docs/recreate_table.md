---
title: "RECREATE TABLE"
old_id: recreate_table
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# RECREATE TABLE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
RECREATE [GLOBAL TEMPORARY] TABLE tablename
  [EXTERNAL [FILE] 'filespec']
  (<col_def> [, <col_def> | <tconstraint> ...])
  [ON COMMIT {DELETE | PRESERVE} ROWS]
  [SQL SECURITY {DEFINER | INVOKER}]
```

## Описание
Оператор `RECREATE TABLE` создаёт новую таблицу или пересоздаёт существующую. Если таблица с таким именем уже есть, сервер попытается удалить её и создать новую. Фактически это последовательность `DROP TABLE` + `CREATE TABLE` одним оператором: не нужно заранее проверять существование объекта. Удобно в установочных и обновляющих скриптах, когда структуру надо гарантированно привести к эталонному виду.

Оператор не выполнится, если у существующей таблицы есть зависимости (ограничения, представления, триггеры, PSQL-модули, ссылающиеся на неё): удаление старой будет отвергнуто и новая создана не будет.

В отличие от `ALTER TABLE`, изменяющего существующую структуру по частям, `RECREATE TABLE` пересоздаёт таблицу целиком по определению из оператора, а все данные старой таблицы безвозвратно уничтожаются. Для таблиц с ценными данными используйте `ALTER TABLE` (либо предваряйте оператор резервной копией через [gbak](/gbak/)).

По синтаксису повторяет `CREATE TABLE`, включая определения столбцов и ограничений, внешние таблицы (`EXTERNAL FILE`), глобальные временные таблицы (`GLOBAL TEMPORARY`) и контекст безопасности (`SQL SECURITY`).

## Пример
```sql
RECREATE TABLE EMPLOYEES
(
  ID          INTEGER NOT NULL,
  LAST_NAME   VARCHAR(50) NOT NULL,
  FIRST_NAME  VARCHAR(50) NOT NULL,
  HIRED       DATE DEFAULT CURRENT_DATE,
  CONSTRAINT PK_EMPLOYEES PRIMARY KEY (ID)
);
```

## См. также
[CREATE TABLE](/create_table/), [ALTER TABLE](/alter_table/), [DROP TABLE](/drop_table/), [gbak](/gbak/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
