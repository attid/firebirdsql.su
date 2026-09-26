# DECRYPT

## Доступно в
DSQL, PSQL

## Формат
```text
DECRYPT (_encrypted_input_
  [USING <algorithm>] [MODE <mode>]
  KEY _key_
  [IV _iv_] [<ctr_type>] [CTR_LENGTH _ctr_length_]
  [COUNTER _initial_counter_] )

<algorithm> ::= <block_cipher> | <stream_cipher>

<block_cipher> ::=
    AES | ANUBIS | BLOWFISH | KHAZAD | RC5
  | RC6 | SAFER+ | TWOFISH | XTEA

<stream_cipher> ::= CHACHA20 | RC4 | SOBER128

<mode> ::= CBC | CFB | CTR | ECB | OFB

<ctr_type> ::= CTR_BIG_ENDIAN | CTR_LITTLE_ENDIAN
```

## Описание
Функция `DECRYPT` расшифровывает (дешифрует) данные с использованием симметричного алгоритма шифрования. В качестве входного значения (`encrypted_input`) функция принимает зашифрованный `BLOB` или двоичную строку и возвращает расшифрованный результат типа `BLOB` или `VARBINARY`. Размеры передаваемых строк должны строго соответствовать требованиям выбранного алгоритма и режима.

Основные параметры:
- `USING <algorithm>` — алгоритм шифрования. Поддерживаются блочные (`AES`, `ANUBIS`, `BLOWFISH`, `KHAZAD`, `RC5`, `RC6`, `SAFER+`, `TWOFISH`, `XTEA`) и потоковые (`CHACHA20`, `RC4`, `SOBER128`) алгоритмы.
- `MODE <mode>` — режим шифрования (`CBC`, `CFB`, `CTR`, `ECB`, `OFB`). Обязателен для блочных шифров.
- `KEY` — ключ дешифрования (обязательный параметр).
- `IV` — вектор инициализации. Должен быть указан для всех блочных алгоритмов, кроме `ECB`, а также для всех потоковых, кроме `RC4`.
- `<ctr_type>` (`CTR_BIG_ENDIAN` или `CTR_LITTLE_ENDIAN`) — порядок байтов счётчика. Применяется только в режиме `CTR` (по умолчанию `CTR_LITTLE_ENDIAN`).
- `CTR_LENGTH` — длина счётчика в байтах в режиме `CTR` (по умолчанию равна длине вектора `IV`).
- `COUNTER` — начальное значение счётчика, применимо только для `CHACHA20` (по умолчанию равно `0`).

## Пример
```sql
SELECT DECRYPT(x'0154090759DF' USING SOBER128 KEY 'AbcdAbcdAbcdAbcd'
               IV '01234567')
FROM rdb$database;

SELECT DECRYPT(secret_field USING AES MODE OFB KEY '0123456701234567'
               IV init_vector)
FROM secure_table;
```
