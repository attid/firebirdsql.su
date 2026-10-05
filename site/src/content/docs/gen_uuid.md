---
title: "GEN_UUID()"
old_id: gen_uuid
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# GEN_UUID()

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | + | + | + |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```sql
gen_uuid()
```

## Описание
[Встроенная функция](/vstroennye_funkcii/).\
Возвращает универсальный уникальный идентификатор ([UUID](http://ru.wikipedia.org/wiki/UUID)).\
[Тип](/tipy_dannyx/) возвращаемого результата: CHAR(16) CHARACTER SET OCTETS.\
Вызывается без аргументов.

⚠️ GEN_UUID() позволяет заполнять значения [UNIQUE](/constraint/) или [PRIMARY KEY](/constraint/) в распределённых базах, когда не удаётся использовать [GEN_ID()](/gen_id/) для формирования искуственных ключей. 

## Пример
```sql
  INSERT INTO RECORDS (id) VALUE (gen_uuid());
```

## См. также
[GEN_ID()](/gen_id/), [UUID_TO_CHAR()](/uuid_to_char/), [CHAR_TO_UUID()](/char_to_uuid/)
## Источник
%Firebird%\doc\sql.extensions\README.builtin_functions.txt \
http://www.firebirdsql.org/refdocs/langrefupd21-intfunc-gen_uuid.html
