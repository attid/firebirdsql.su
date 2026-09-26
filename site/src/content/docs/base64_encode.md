---
title: "BASE64_ENCODE"
old_id: base64_encode
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# BASE64_ENCODE

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
BASE64_ENCODE(binary_data)
```

| Параметр | Описание |
|---|---|
| `binary_data` | Двоичные данные для кодирования |

## Описание
Функция `BASE64_ENCODE` кодирует двоичные данные по алгоритму base64 и возвращает результат в текстовом виде. Тип результата зависит от входного аргумента: для не-BLOB аргументов — `VARCHAR CHARACTER SET ASCII`, для `BLOB` — `BLOB SUB_TYPE TEXT CHARACTER SET ASCII`. Набор символов ASCII гарантирует, что закодированная строка состоит только из переносимых символов, безопасных для хранения и передачи текстовыми протоколами.

Возвращаемое значение при необходимости дополняется знаками `=`, чтобы длина была кратна четырём, как требует стандарт base64.

Когда входной аргумент не является `BLOB`, длина результирующего типа вычисляется по формуле `type_length * 4 / 3` с округлением вверх до числа, кратного четырём, где `type_length` — максимальная длина входного типа в байтах: каждые 3 байта исходных данных превращаются в 4 символа.

Типичные применения — передача двоичных данных (хешей, изображений, сериализованных структур) через текстовые каналы: JSON, XML, почту, HTTP-заголовки. Обратное преобразование выполняет `BASE64_DECODE`; шестнадцатеричный аналог — `HEX_ENCODE`.

## Пример
```sql
select base64_encode('Test base64')
from rdb$database;
```

```
BASE64_ENCODE
================
VGVzdCBiYXNlNjQ=
```

Кодирование хеша для текстового отчёта:

```sql
select base64_encode(hash_value) as hash_b64
from file_hashes
where file_id = 42;
```

## См. также
[BASE64_DECODE](/base64_decode/), [CRYPT_HASH](/crypt_hash/), [Встроенные функции по группам](/vstroennye_funkcii_po_gruppam/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
