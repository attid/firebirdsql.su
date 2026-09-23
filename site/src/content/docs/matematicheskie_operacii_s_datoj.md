---
title: "Математические операции с датой и временем"
old_id: matematicheskie_operacii_s_datoj
section: sql
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# Математические операции с датой и временем

Иногда возникает необходимость проводить с датой какие-либо операции что мы и попытаемся изложить.

Для начала определимся, что у нас есть и что мы с этим можем сделать.

Операции можно проводить со следующими типами данных: [DATE](/tipy_dannyx/), [TIME](/tipy_dannyx/), [TIMESTAMP](/tipy_dannyx/)

Операции которые могут нам понадобиться: это добавить(убавить) и найти разницу.

С добавлением к [TIMESTAMP](/tipy_dannyx/) проще всего заниматься используя родные UDF fbudf [ADDMILLISECOND()](/addmillisecond/), [ADDSECOND()](/addsecond/), [ADDMINUTE()](/addminute/), [ADDDAY()](/addday/), [ADDWEEK](/addweek/), [ADDMONTH()](/addmonth/), [ADDYEAR()](/addyear/)

С версии 2.1 доступна функция [dateadd](/dateadd/).

Если не хочется использовать UDF и не важна погрешность, то можно прибавлять все ручками 

для [TIMESTAMP](/tipy_dannyx/) 1 (единица) это один день, соответственно 0.00001157407 это одна секунда

для [DATE](/tipy_dannyx/) 1 (единица) это один день

для [TIME](/tipy_dannyx/) 1 (единица) это одна секунда, 3600 это час  

к примеру хотим добавить 30 секунд к [TIMESTAMP](/tipy_dannyx/)

```sql
SELECT current_timestamp, current_timestamp + (0.00001157407*30) FROM RDB$DATABASE 
```

30 секунд к [TIME](/tipy_dannyx/)

```sql
select current_time, current_time + 30  from rdb$database
```

добавляем к дате 5 дней

```sql
select current_date , current_date + 5 from rdb$database
```

получить кол-во секунд с полночи можно так

```sql
select current_time - cast('0:00' as time) from rdb$database
``` 

сколько прошло времени между 18:00 и 15:30  в часах и минутах (мы тут никогда не получим результат больше суток "25:15" потому что невозможно)

```sql
select cast('0:00' as time)+(cast('18:00' as time)-cast('15:30' as time)) from rdb$database
```

тоже самое но с [TIMESTAMP](/tipy_dannyx/) сравнивается только время, дата не учитывается никак

```sql
select cast('0:00' as time)+(cast('01.01.2001 18:00' as timestamp)-cast('02.02.2007 15:30' as timestamp))*24*60*60 from rdb$database
```

зато дату можно можно прибывать к другому [TIMESTAMP](/tipy_dannyx/)

```sql
select cast('03.03.2003' as timestamp) + (cast('05.02.2001 18:00' as timestamp)-cast('02.02.2001 15:30' as timestamp)) from rdb$database
```

также мы можем [TIME](/tipy_dannyx/) прибавит к [TIMESTAMP](/tipy_dannyx/)

```sql
select current_timestamp+(cast('2:00' as time)-cast('0:00' as time))/(60*60*24) from rdb$database
```

[TIME](/tipy_dannyx/) и [DATE](/tipy_dannyx/) складываются без шаманства

```sql
select current_date + current_time from rdb$database
```

получить разницу больше суток в часах можно при помощи следующей процедуры

```sql
create or alter procedure get_my_time (beg timestamp, ends timestamp)
returns (_time varchar(20))
as
   declare variable interval double precision;
   declare variable hours int;
   declare variable mins int;
   declare variable sec int;
begin
   interval = beg - ends;
   if (interval < 0) then interval = -interval;
   interval = interval*24;
   if (cast(interval as int) > interval) then hours = interval - 1; else hours = interval;
   interval = (interval - hours)*60;
   if (cast(interval as int) > interval) then mins = interval - 1; else mins = interval;
   sec = (interval - mins)*60;
   if (sec = 60) then sec = 59; /* милисекунды могут сделать бяку, потому так */

   _time = hours || ':' || case when mins>10 then mins else '0' || mins end || ':' || case when sec>10 then sec else '0' || sec end;
   suspend;
end
```
