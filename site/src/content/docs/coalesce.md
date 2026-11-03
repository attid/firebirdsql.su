---
title: "COALESCE в Firebird: синтаксис и примеры"
old_id: coalesce
section: glossary
type: term
updated: "2026-11-03"
firebird:
  since: "1.5"
  until: 
  deprecated: false
---

# COALESCE в Firebird

`COALESCE()` возвращает первый из своих аргументов, который не равен `NULL`
(а если не-NULL аргументов нет — сам `NULL`). Это самый короткий способ
подставить значение по умолчанию вместо NULL в запросе или в PSQL.

## Формат

COALESCE ( значение1, значение2[, значение3 [, ...]] )

## Описание

Встроенная функция, появилась в Firebird 1.5. Возвращает первое не-NULL
значение из списка аргументов; типы аргументов должны быть совместимы.

`COALESCE(V1, V2)` — упрощённая форма [CASE](/case/):

```sql
CASE WHEN V1 IS NOT NULL THEN V1 ELSE V2 END
```

`COALESCE(V1, V2, ..., Vn)` разворачивается рекурсивно:

```sql
CASE WHEN V1 IS NOT NULL THEN V1
     ELSE COALESCE(V2, ..., Vn) END
```

## Примеры

Подставить текст вместо отсутствующего адреса:

```sql
select c.customer, coalesce(c.address_line2, 'не задан')
from customer c
```

Склейка строк с NULL-полями — типичный источник «пропавших» значений:

```sql
select coalesce(lastname, '') || ' ' || coalesce(firstname, '')
from people
```

Если все аргументы NULL, результат тоже NULL:

```sql
select coalesce(null, null, null) from rdb$database;
-- NULL
```

## См. также

[IF](/if/), [CASE](/case/), [IIF](/iif/), [NULL](/null/), [NULLIF](/nullif/)
