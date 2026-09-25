---
title: "DROP EXCEPTION"
old_id: drop_exception
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# DROP EXCEPTION

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
DROP EXCEPTION <наименование>;

## Описание
Оператор, удаляющий исключение <наименование> в текущей БД.

Удалить исключение может либо его владелец либо SYSDBA, при условии что его нет в зависимостях других обьектов

## Пример
```sql
  DROP EXCEPTION UNKNOWN_EMP_ID
```

## См. также
[CREATE EXCEPTION](/create_exception/), [EXCEPTION](/exception/),  [ALTER EXCEPTION](/alter_exception/),  RECREATE EXCEPTION

## Источник
