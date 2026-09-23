---
title: "DROP TRIGGER"
old_id: drop_trigger
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DROP TRIGGER

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
```
DROP TRIGGER name;
```

| Аргумент | Описание |
|---|---|
| name | Имя существующего триггера. |

## Описание
DROP TRIGGER удаляет определенный пользователем триггер из базы данных. Определенные системой триггеры, такие как созданные для CHECK ограничения, не могут быть удалены инструкцией DROP TRIGGER. Используйте ALERT TABLE, чтобы удалить предложение CHECK, которое определяет триггер.

Триггеры, используемые для активных транзакций, не могут быть удалены, пока транзакция не завершена.

Триггер может быть удален его создателем и пользователем SYSDBA.

⚠️ Чтобы сделать триггер временно не активным, используйте инструкцию [ALTER TRIGGER](/alter_trigger/) и определите INACTIVE в заголовке.

## Пример
Следующая инструкция удаляет триггер:
```
DROP TRIGGER POST_NEW_ORDER;
```
## См. также
[CREATE TRIGGER](/create_trigger/),  [ALTER TRIGGER](/alter_trigger/),  RDB$TRIGGERS, [CREATE PROCEDURE](/create_procedure/),  [ALTER PROCEDURE](/alter_procedure/)

## Источник
langref.pdf
