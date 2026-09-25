---
title: "CREATE PACKAGE"
old_id: create_package
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "3.0"
  until: 
  deprecated: false
---

# CREATE PACKAGE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
CREATE PACKAGE package_name
  [SQL SECURITY {INVOKER | DEFINER}]
AS
BEGIN
  [<package_item declarations>]
  [<module function declarations>]
END

CREATE PACKAGE BODY package_name
AS
BEGIN
  [<package_item declarations>]
  [<module function implementations>]
  [<module procedure implementations>]
END
```

## Описание
Оператор `CREATE PACKAGE` создаёт заголовок пакета, определяющий его открытый интерфейс. Имя пакета должно быть уникальным среди всех пакетов базы данных и может содержать до 63 символов.

Необязательное предложение `SQL SECURITY` задаёт контекст привилегий выполнения для всех процедур и функций пакета: `INVOKER` (по умолчанию) выполняет подпрограммы с правами вызывающего пользователя, а `DEFINER` — с правами владельца пакета, дополненными привилегиями, выданными самому пакету через [GRANT](/grant/). Переопределять контекст для отдельных подпрограмм внутри пакета запрещено.

В отличие от отдельных хранимых процедур и функций, существующих в глобальном пространстве имён базы данных, пакет позволяет логически объединять связанные подпрограммы. Процедуры и функции, объявленные в заголовке пакета, доступны извне через составное имя вида `package_name.proc_name` / `package_name.func_name`. Механизм пакетов разделяет заголовок и тело (`CREATE PACKAGE BODY`): подпрограммы, определённые только в теле и не объявленные в заголовке, остаются приватными и недоступными снаружи. Если имя подпрограммы пакета совпадает с именем глобальной процедуры или функции, внутри пакета всегда вызывается локальная подпрограмма пакета.

Тело пакета создаётся оператором `CREATE PACKAGE BODY`; заголовок и тело компилируются вместе, поэтому изменение тела требует прав на изменение и заголовка.

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
END
```

## См. также
[CREATE FUNCTION](/create_function/), [CREATE PROCEDURE](/create_procedure/), [GRANT](/grant/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
