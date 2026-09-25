---
title: "UPDATE OR INSERT"
old_id: update_or_insert
section: glossary
type: term
firebird:
  since: "2.1"
  until: 
  deprecated: false
---

# UPDATE OR INSERT
Модификация или вставка записи

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | Да | Да | Да |
## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/)  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

UPDATE OR INSERT INTO <table or view> [(<column_list>)]
VALUES (<value_list>)
[MATCHING (<column_list>)]
[RETURNING <column_list> [INTO <variable_list>]]

## Описание
В таблице проводится поиск по полям перечисленным в MATCHING.

Если записи нашлись - заменяем их. Иначе вставляем новые.

Если MATCHING не указан, то используется PRIMARY_KEY

Для успешного :?:выполнения необходимы права как на INSERT так и на UPDATE таблицы

Для успешного ⚠️ выполнения [returning](/returning/) запрос должен работать с одной записью
a
## Пример
Задача: Установить правильную валюту для страны "Украина". Если этой страны нет, то завести :-)
```sql
update or insert into country (country, currency)
values ('Ukraine','hryvnia')
matching (country)
```
Выполняем скрипт пару раз и замечаем:

первое выполнение "1 record(s) was(were) inserted into COUNTRY" - произошла вставка

последующие       "1 record(s) was(were) updated in COUNTRY"    - апдейт 

Ну и если учесть, что поле в MATCHING у нас совпадает с ключем таблицы, то можно смело сие предложение (matching) удалять

## См. также
[insert](/insert/) [returning](/returning/) into [update](/update/) 

## Источник
Firebird_v2.1.0.ReleaseNotes.pdf
