---
title: "CREATE INDEX"
old_id: create_index
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# CREATE INDEX

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| + | + | + | + | + | + | + | + | + | + | + |

## Формат
```
CREATE [UNIQUE] [ASC[ENDING] | DESC[ENDING]]
INDEX <имя индекса> ON <таблица>
 { (<столбец> [, <столбец> ...]) | COMPUTED BY (выражение) };
```

## Описание
Индекс создается для одной конкретной таблицы. Имя индекса должно быть уникальным среди имен всех индексов базы данных. Индекс может быть уникальным (ключевое слово UNIQUE). Это означает, что в индексе не может быть двух разных строк с одинаковыми значениями столбцов. Столбцы, входящие в состав уникального индекса, не могут также иметь пустого значения NULL.
Ключевое слово ASCENDING (сокращенно ASC) означает, что записи индекса упорядочиваются по возрастанию значений столбцов, входящих в состав индекса. Этот вариант по умолчанию.
Ключевое слово DESCENDING (сокращение DESC) указывает, что записи индекса упорядочиваются по уменьшению значений столбцов индекса.
В состав индекса не могут входить столбцы, имеющие тип данных BLOB, а также столбцы любого типа данных, являющиеся массивами.
Для одной таблицы можно создать не более 256 индексов.

## Примеры
Если для таблицы PEOPLE требуются и возрастающий, и убывающий индексы по столбцу, хранящему фамилии людей LAST_NAME, то нужно создать два индекса, выполнив следующие операторы:

```sql
CREATE ASCENDING INDEX IDX_ASC_PEOPLE ON PEOPLE (LAST_NAME);
CREATE DESCENDING INDEX IDX_DESC_PEOPLE ON PEOPLE (LAST_NAME);
```

Вместо одного или нескольких полей в индексе можно использовать выражение. Выражение будет проиндексировано в запросах, если оно находится в предложении WHERE, ORDER BY или GROUP BY. 
Индексирование нескольких выражений не поддерживается:
```sql
CREATE INDEX IDX_UPNAME ON PERSONS COMPUTED BY (UPPER(NAME));
COMMIT;

-- следующие запросы будут использовать этот индекс idx_upname:
SELECT * FROM PERSONS ORDER BY UPPER(NAME);
SELECT * FROM PERSONS WHERE UPPER(NAME) STARTING WITH 'ВЛАД';
DELETE FROM PERSONS WHERE UPPER(NAME) = 'БОГДАН';
DELETE FROM PERSONS WHERE UPPER(NAME) = 'БОГДАН' AND AGE > 65;
```

```sql
CREATE DESCENDING INDEX IDX_DESC_EVENTS_YT 
    ON MYEVENTS COMPUTED BY (EXTRACT(YEAR FROM STARTDATE) || TOWN);
COMMIT;

-- следующий запрос будет использовать этот индекс idx_desc_events_yt:
SELECT * FROM MYEVENTS
  ORDER BY EXTRACT(YEAR FROM STARTDATE) || TOWN DESC;
```
## См. также
[INDEX](/index/), DROP INDEX, [ALTER INDEX](/alter_index/)
