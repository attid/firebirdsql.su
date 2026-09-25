---
title: "DROP PROCEDURE"
old_id: drop_procedure
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# DROP PROCEDURE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Формат
```
DROP PROCEDURE name;
```

| Аргумент | Описание |
|---|---|
| name | Имя существующей процедуры. |

## Описание
DROP PROCEDURE удаляет из базы данных существующую процедуру.

## Пример
Следующая инструкция удаляет процедуру TEST_PROCEDURE.
```
DROP PROCEDURE TEST_PROCEDURE;
```

## См. также
[CREATE PROCEDURE](/create_procedure/)

## Источник
langref.pdf
