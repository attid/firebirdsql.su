---
title: "DROP DOMAIN"
old_id: drop_domain
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# DROP DOMAIN

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | ? | ? |

## Формат
DROP DOMAIN <наименование>;

## Описание
Оператор, удаляющий домен <наименование> в текущей БД.

Удалить домен может либо её владелец либо SYSDBA при условии что его нет в зависимостях других обьектов

## Пример
DROP DOMAIN PHONENUMBER

## См. также
[CREATE DOMAIN](/create_domain/),  [ALTER DOMAIN](/alter_domain/)

## Источник
