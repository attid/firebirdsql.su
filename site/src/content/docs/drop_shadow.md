---
title: "DROP SHADOW"
old_id: drop_shadow
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# DROP SHADOW

## Формат
```
DROP SHADOW <номер оперативной копии>
```

## Описание
Оператор DROP SHADOW удаляет указанную оперативную копии из базы данных, с которой в настоящий момент существует соединение.
Номер оперативной копии — положительное число, идентифицирующее набор файлов ранее созданной оперативной копии. При удалении оперативной копии удаляются все связанные с ней файлы и прекращается процесс дублирования данных в этой оперативной копии. Оперативная копия может быть удалена ее создателем, пользователем SYSDBA, пользователем операционной системы root (Linux), trusted user (Windows).

## Пример
```sql
  DROP SHADOW 666
```

## См. также
[CREATE DATABASE](/create_database/), [ALTER DATABASE](/alter_database/), [DROP DATABASE](/drop_database/), [CREATE SHADOW](/create_shadow/)
