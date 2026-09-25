---
title: "EXTRACT"
old_id: extract
section: glossary
type: term
firebird:
  since: "0.9"
  until: 
  deprecated: false
---

# EXTRACT

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| Да | Да | Да | Да | Да | Да | Да | Да | Да | Да | ? |

## Формат
EXTRACT (part FROM value)

где 

value должно быть следующего типа : [DATE](/tipy_dannyx/), [TIME](/tipy_dannyx/), [TIMESTAMP](/tipy_dannyx/). 

## Описание
Встроенная функция. Позволяет извлекать дату и время. Извлекаемая часть должна присутствовать в значении. Например, не стоит извлекать год из данных, где хранится время.
EXTRACT (YEAR FROM aTime)
выдаст ошибку.

Значения, которые можно извлекать, представлены в следующей таблице

| Служебное слово | Тип данных | Значение |
|---|---|---|
| YEAR | [SMALLINT](/tipy_dannyx/) | Год, 1-9999 |
| MONTH | [SMALLINT](/tipy_dannyx/) | Месяц, 1-12 |
| DAY | [SMALLINT](/tipy_dannyx/) | День, 1-31 |
| HOUR | [SMALLINT](/tipy_dannyx/) | Час, 0-23 |
| MINUTE | [SMALLINT](/tipy_dannyx/) | Минут, 0-59 |
| SECOND | [NUMERIC(9,4)](/tipy_dannyx/) | Секунд, 0.0000-59.9999 |
| MILLISECOND | [NUMERIC(9,1)](/tipy_dannyx/) | Миллисекунд, 0.0–999.9 (начиная с версии 2.1.2) |
| WEEK | [SMALLINT](/tipy_dannyx/) | Номер недели года, 1–53 (начиная с версии 2.1) |
| WEEKDAY | [SMALLINT](/tipy_dannyx/) | День недели, 0-6 (начиная с Воскресенья) |
| YEARDAY | [SMALLINT](/tipy_dannyx/) | День года, 0-365 |

## Пример
процедура, возвращающая дату и время в текстовом виде в формате '00.00.0000 00:00'
```sql
CREATE OR ALTER PROCEDURE BDATE_TIME(
    DT TIMESTAMP)
RETURNS (
    RESULT VARCHAR(16))
AS
begin
  --извлекаем день 
  select l.result||'.' from lpad(extract(day from :dt),2,'0') l into result;

  --извлекаем месяц
  select :result||l.result||'.' from lpad(extract(month from :dt),2,'0') l into result;

  --извлекаем год 
  select :result||l.result||' ' from lpad(extract(year from :dt),4,'0') l into result;

  --извлекаем час 
  select :result||l.result||':' from lpad(extract(hour from :dt),2,'0') l into result;

  --извлекаем минута 
  select :result||l.result from lpad(extract(minute from :dt),2,'0') l into result;

  --result = '00.00.0000 00:00';

  suspend;

end
```

два варианта получания номера квартала из даты
```sql
SELECT CAST(EXTRACT(MONTH FROM CURRENT_TIMESTAMP)/3 + 0.3 AS INTEGER) FROM RDB$DATABASE
SELECT (EXTRACT(MONTH FROM CURRENT_TIMESTAMP)-1)/3+1 FROM RDB$DATABASE
```

Получение номера недели в году, источник [Date functions](http://www.volny.cz/iprenosil/interbase/ip_ib_code_timestamp.htm)

```sql
CREATE PROCEDURE YearWeek (D DATE)
  RETURNS (WEEK_NO INTEGER) AS
BEGIN
  D = D - EXTRACT(WEEKDAY FROM D-1) + 3;  /* move to thursday */
  WEEK_NO = (EXTRACT(YEARDAY FROM D) - EXTRACT(WEEKDAY FROM D-1) + 7) / 7e0;
  SUSPEND;
END
```
## См. также
[Математические операции с датой и временем](/matematicheskie_operacii_s_datoj/), [ADDMILLISECOND()](/addmillisecond/), [ADDSECOND()](/addsecond/), [ADDMINUTE()](/addminute/), [ADDDAY()](/addday/), [ADDWEEK](/addweek/), [ADDMONTH()](/addmonth/), [ADDYEAR()](/addyear/)

## Источник
ib60releasenotes.pdf
