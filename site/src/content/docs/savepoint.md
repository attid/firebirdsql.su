---
title: "SAVEPOINT"
old_id: savepoint
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# SAVEPOINT

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
SAVEPOINT sp_name
```

| Параметр | Описание |
|---|---|
| `sp_name` | Имя точки сохранения. Должно быть уникальным в рамках транзакции. |

## Описание
Оператор `SAVEPOINT` создаёт совместимую с SQL:99 точку сохранения, к которой можно позже откатить работу с базой данных, не отменяя всё выполненное с момента старта транзакции. Механизм точек сохранения также известен как «вложенные транзакции» (nested transactions).

Если точка сохранения с указанным именем уже существует в рамках текущей транзакции, старая удаляется и создаётся новая с тем же именем.

Для отката изменений к точке сохранения используется оператор [ROLLBACK TO SAVEPOINT](/rollback/).

[NOTE]
====
Внутренний механизм точек сохранения может использовать большие объёмы памяти, особенно при многократном обновлении одних и тех же записей в одной транзакции. Если точка сохранения больше не нужна, но и транзакцию завершать пока не планируется, её можно удалить оператором `RELEASE SAVEPOINT sp_name`, освободив ресурсы.
====

## Пример
```sql
CREATE TABLE TEST (ID INTEGER);
COMMIT;

INSERT INTO TEST VALUES (1);
COMMIT;

INSERT INTO TEST VALUES (2);
SAVEPOINT Y;
DELETE FROM TEST;
SELECT * FROM TEST;      -- вернёт пустой набор

ROLLBACK TO SAVEPOINT Y;
SELECT * FROM TEST;      -- снова видна запись 2
```

## См. также
[ROLLBACK](/rollback/), [COMMIT](/commit/), [SET TRANSACTION](/set_transaction/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
