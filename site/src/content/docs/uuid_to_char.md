---
title: "UUID_TO_CHAR()"
old_id: uuid_to_char
section: glossary
type: term
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# UUID_TO_CHAR()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
  UUID_TO_CHAR( CHAR(16) )
```

## Описание

Встроенная функция UUID_TO_CHAR( ) преобразует переданное в качестве параметра восьмеричное представление UUID в виде 16 символов, удобное для хранения, в 32-х символьное ASCII представление UUID XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.

## Пример
```sql
  SELECT UUID_TO_CHAR( GEN_UUID() ) 
  FROM   RDB$DATABASE;
```

## См. также
[GEN_UUID()](/gen_uuid/), [CHAR_TO_UUID()](/char_to_uuid/), [Встроенные функции](/vstroennye_funkcii/)

## Источник
Firebird 2.5 Realise Notes  http://firebirdsql.org/devel/doc/rlsnotes/html/rlsnotes25.html
