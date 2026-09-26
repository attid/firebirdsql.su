---
title: "ENCRYPT"
old_id: encrypt
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# ENCRYPT

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
ENCRYPT (input
  [USING <algorithm>] [MODE <mode>]
  KEY key
  [IV iv] [<ctr_type>] [CTR_LENGTH ctr_length]
  [COUNTER initial_counter] )

<algorithm> ::= <block_cipher> | <stream_cipher>

<block_cipher> ::=
    AES | ANUBIS | BLOWFISH | KHAZAD | RC5
  | RC6 | SAFER+ | TWOFISH | XTEA

<stream_cipher> ::= CHACHA20 | RC4 | SOBER128

<mode> ::= CBC | CFB | CTR | ECB | OFB

<ctr_type> ::= CTR_BIG_ENDIAN | CTR_LITTLE_ENDIAN
```

## Описание
Функция `ENCRYPT` шифрует данные симметричным шифром. Входные данные (`input`) — выражение строкового типа или `BLOB`. Алгоритм может быть блочным (`AES`, `ANUBIS`, `BLOWFISH`, `KHAZAD`, `RC5`, `RC6`, `SAFER+`, `TWOFISH`, `XTEA`) или потоковым (`CHACHA20`, `RC4`, `SOBER128`).

Режим шифрования `mode` (`CBC`, `CFB`, `CTR`, `ECB`, `OFB`) обязателен для блочных алгоритмов. Ключ задаётся параметром `KEY`. Вектор инициализации `IV` обязателен для всех блочных алгоритмов, кроме режима `ECB`, и для всех потоковых, кроме `RC4`.

Параметры `ctr_type` (порядок байтов счётчика, по умолчанию `CTR_LITTLE_ENDIAN`) и `ctr_length` (длина счётчика в байтах, по умолчанию — длина IV) допустимы только в режиме `CTR`. Начальное значение счётчика `COUNTER` допустимо только для `CHACHA20`, по умолчанию 0.

Функция возвращает `BLOB SUB_TYPE BINARY`, если вход — `BLOB`, и `VARBINARY` для остальных текстовых и двоичных типов.

Размеры `key` и `iv` должны соответствовать требованиям алгоритма и режима; как правило, размер `iv` совпадает с размером блока алгоритма. Для режимов `ECB` и `CBC` входные данные должны быть кратны размеру блока — при необходимости дополните их вручную (нулями или пробелами).

## Пример
Потоковое шифрование SOBER128 с ключом и IV:

```sql
SELECT ENCRYPT('Secret data'
  USING SOBER128
  KEY '0123456789ABCDEF76543210'
  IV '32109876')
FROM RDB$DATABASE;
```

Обратная операция — [DECRYPT](/decrypt/) с теми же ключом и IV.

## См. также
[DECRYPT](/decrypt/), [CRYPT_HASH](/crypt_hash/), [RSA_FUNCTIONS](/rsa_functions/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
