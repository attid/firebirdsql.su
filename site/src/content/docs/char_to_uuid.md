---
title: "CHAR_TO_UUID()"
old_id: char_to_uuid
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# CHAR_TO_UUID()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
  CHAR_TO_UUID( CHAR(32) )
```

## Описание

Встроенная функция CHAR_TO_UUID() преобразует переданное в качестве параметра 32-х символьное ASCII представление UUID XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX в восьмеричное представление, оптимизированное для хранения.

## Пример
```sql
  SELECT CHAR_TO_UUID('93519227-8D50-4E47-81AA-8F6678C096A1') 
  FROM   RDB$DATABASE;
```

## См. также
[GEN_UUID()](/gen_uuid/), [UUID_TO_CHAR()](/uuid_to_char/), [Встроенные функции](/vstroennye_funkcii/)

## Источник
Firebird 2.5 Release Notes  http://firebirdsql.org/devel/doc/rlsnotes/html/rlsnotes25.html
