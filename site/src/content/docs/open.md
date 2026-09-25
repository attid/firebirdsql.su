---
title: "OPEN"
old_id: open
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# OPEN

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| Да | Да | Да | Да | Да |

## Доступно в
[PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
OPEN cursor_name;
```

## Описание
Оператор `OPEN` открывает ранее объявленный курсор, выполняет объявленный в нём оператор `SELECT` и получает записи из результирующего набора. `OPEN` применим только к курсорам, объявленным оператором `DECLARE ... CURSOR`.

Если в `SELECT` курсора есть параметры, они должны быть объявлены как локальные переменные или входные (выходные) параметры до объявления курсора. При открытии курсора параметру присваивается текущее значение переменной. Это важно при повторном открытии курсора внутри цикла: каждый `OPEN` заново вычисляет результирующий набор с учётом актуальных на момент открытия значений.

После открытия курсор устанавливается перед первой записью набора. Последовательная выборка выполняется оператором `FETCH`, а по завершении работы курсор закрывается оператором `CLOSE` для освобождения ресурсов.

## Пример
```sql
SET TERM ^;
CREATE OR ALTER PROCEDURE GET_RELATIONS_NAMES
RETURNS (
  RNAME CHAR(31)
)
AS
  DECLARE C CURSOR FOR (
    SELECT RDB$RELATION_NAME
    FROM RDB$RELATIONS);
BEGIN
  OPEN C;
  WHILE (1 = 1) DO
  BEGIN
    FETCH C INTO :RNAME;
    IF (ROW_COUNT = 0) THEN
      LEAVE;
    SUSPEND;
  END
  CLOSE C;
END^
SET TERM ;^
```

## См. также
[CLOSE](/close/), [FETCH](/fetch/), [DECLARE CURSOR](/declare_cursor/), [Разновидности языка SQL](/raznovidnosti_jazyka_sql/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
