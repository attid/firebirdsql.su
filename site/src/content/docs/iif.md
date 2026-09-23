---
title: "IIF()"
old_id: iif
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# IIF()
## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| ? | ? | ? | ? | ? | + | + | + | + | + | + |
## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)
## Формат
```sql
IIF(<поисковое условие>, <значение1>, <значение2>)
```
## Описание
[Встроенная функция](/vstroennye_funkcii/).\
Если <поисковое условие> верно то возвращается <значение1> иначе <значение2>.

IIF - упрощенная форма [CASE](/case/), к примеру
```sql
IIF(SC, V1, V2)
```
можно заменить на
```sql
CASE WHEN SC THEN V1 ELSE V2 END
``` 
## Пример
```sql
  SELECT e.full_name, IIF(e.hire_date > current_date, 'Работает', 'Уволен') FROM employee e
```
## См. также
[IF](/if/), [CASE](/case/), [COALESCE](/coalesce/)
## Источник
%Firebird%\doc\sql.extensions\README.iif.txt \
http://www.firebirdsql.org/refdocs/langrefupd20-iif.html
