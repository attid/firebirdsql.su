---
title: "DISTINCT"
old_id: distinct
section: glossary
type: term
firebird:
  since: "2.0"
  until: 
  deprecated: false
---

# DISTINCT

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | + | + | + | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/) [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
DISTINCT  используется в конструкции [SELECT](/select/) и как самостоятельный оператор 

*переменная* IS [NOT] DISTINCT FROM *переменная2*

FIXME
## Описание

сравнивает 2 значения невзирая на NULL

если на поле существует индекс то он может быть использован при NOT DISTINCT

FIXME

## Пример
Блок 
```sql
execute block
returns (s varchar(100))
as
begin
  if (null = null) then
  begin
    s = 'null = null';
    suspend;
  end

  if (null <> null) then
  begin
    s = 'null <> null';
    suspend;
  end

  if (null = 12) then
  begin
    s = 'null = 12';
    suspend;
  end

  if (null <> 12) then
  begin
    s = 'null <> 12';
    suspend;
  end

  if (12 <> 12) then
  begin
    s = '12 <> 12';
    suspend;
  end

  if (12 = 12) then
  begin
    s = '12 = 12';
    suspend;
  end

  if (null is distinct from null) then
  begin
    s = 'null is distinct from null';
    suspend;
  end

  if (null is not distinct from null) then
  begin
    s = 'null is not distinct from null';
    suspend;
  end

  if (null is distinct from 12) then
  begin
    s = 'null is distinct from 12';
    suspend;
  end

  if (12 is distinct from null) then
  begin
    s = '12 is distinct from null';
    suspend;
  end

  if (12 is distinct from 12) then
  begin
    s = '12 is distinct from 12';
    suspend;
  end

  if (12 is not distinct from 12) then
  begin
    s = '12 is not distinct from 12';
    suspend;
  end

  if (12 is distinct from 13) then
  begin
    s = '12 is distinct from 13';
    suspend;
  end

end;
```
результат
```
12 = 12
null is not distinct from null
null is distinct from 12
12 is distinct from null
12 is not distinct from 12
12 is distinct from 13
```

```sql
SELECT * FROM T1 JOIN T2 ON T1.NAME IS NOT DISTINCT FROM T2.NAME;
```
```sql
SELECT * FROM T WHERE T.MARK IS DISTINCT FROM 'test'
```

## См. также
[COALESCE](/coalesce/) [nullif](/nullif/)

## Источник
README.distinct.txt
