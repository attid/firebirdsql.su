---
title: "CLOSE"
old_id: close
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# CLOSE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
CLOSE cursor_name;
```

## Описание
Оператор `CLOSE` закрывает открытый курсор. Применим только к курсорам, объявленным оператором `DECLARE ... CURSOR`.

Явное закрытие не строго обязательно: оставшиеся открытыми курсоры автоматически закрываются после завершения выполнения кода триггера, хранимой процедуры, функции или анонимного PSQL-блока, в пределах которого они были открыты. Тем не менее явный `CLOSE` делает код понятнее и освобождает курсор сразу, как только работа с набором данных завершена.

Типичный жизненный цикл курсора в PSQL: объявление через `DECLARE ... CURSOR`, открытие оператором `OPEN`, чтение строк оператором `FETCH` и закрытие оператором `CLOSE`.

## Пример
```sql
SET TERM ^;
CREATE OR ALTER PROCEDURE list_customers
RETURNS (cust_name VARCHAR(50))
AS
  DECLARE c CURSOR FOR (SELECT name FROM customers ORDER BY name);
BEGIN
  OPEN c;
  WHILE (1 = 1) DO
  BEGIN
    FETCH c INTO :cust_name;
    IF (ROW_COUNT = 0) THEN LEAVE;
    SUSPEND;
  END
  CLOSE c;
END^
SET TERM ;^
```

## См. также
[OPEN](/open/), [FETCH](/fetch/), [DECLARE CURSOR](/declare_cursor/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
