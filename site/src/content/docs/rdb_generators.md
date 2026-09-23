---
title: "RDB$GENERATORS"
old_id: rdb_generators
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# RDB$GENERATORS

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Доступно в
FIXME[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
| Имя столбца | Тип | Описание |
|---|---|---|
| RDB$GENERATOR_NAME | CHAR(31) | Название генератора, указывается в CREATE, ALTER, DROP, GEN_ID |
| RDB$GENERATOR_ID | SMALLINT | Уникальный идентификатор |
| RDB$SYSTEM_FLAG | SMALLINT |  |
| RDB$DESCRIPTION | BLOB subtype TEXT | Описание<br> ⚠️Только в версии 2.0 и выше |

## Описание
⚠️ Приведенная в этом разделе информация предназначена только для общего ознакомления. Общее правило таково: вы не должны обращаться к системным таблицам напрямую. Не пытайтесь создавать или изменять генераторы путем изменения таблицы RDB$GENERATORS. (Хотя оператор [SELECT](/select/) и не наделает бед.)

## Пример
```sql
  SELECT * FROM RDB$GENERATORS G
```

## См. также

## Источник
http://www.firebirdsql.org/manual/ru/generatorguide-basics-ru.html
