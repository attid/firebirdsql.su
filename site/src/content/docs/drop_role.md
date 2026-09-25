---
title: "DROP ROLE"
old_id: drop_role
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# DROP ROLE

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | Да |

## Формат
```
DROP ROLE name;
```

| Аргумент | Описание |
|---|---|
| name | Имя существующей роли. |

## Описание
DROP ROLE удаляет из базы данных существующую роль доступа.

## Пример
Следующая инструкция удаляет роль.
```
DROP ROLE "Managers";
```

## См. также
[CREATE ROLE](/create_role/),  [GRANT](/grant/),  [REVOKE](/revoke/)

## Источник
langref.pdf
