---
title: "BASE64_DECODE"
old_id: base64_decode
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# BASE64_DECODE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
BASE64_DECODE(base64_data)
```

## Описание
`BASE64_DECODE` декодирует строку с данными в кодировке Base64 и возвращает декодированное значение как `VARBINARY` или `BLOB` — в зависимости от типа входного аргумента.

Параметр `base64_data` — данные в Base64, дополненные знаком `=` до длины, кратной 4. Функция требует корректного выравнивания входа:

- если длина *типа* `base64_data` не кратна 4 — ошибка возникает при подготовке запроса;
- если длина *значения* не кратна 4 — ошибка при выполнении.

Когда входной аргумент не является `BLOB`, длина результирующего типа вычисляется как `type_length * 3 / 4`, где `type_length` — максимальная длина типа входа в байтах.

## Пример
```sql
select cast(base64_decode('VGVzdCBiYXNlNjQ=') as varchar(12))
from rdb$database;
```

```
CAST
============
Test base64
```

## См. также
[BASE64_ENCODE](/base64_encode/), [HEX_ENCODE](/hex_encode/), [Встроенные функции по группам](/vstroennye_funkcii_po_gruppam/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
