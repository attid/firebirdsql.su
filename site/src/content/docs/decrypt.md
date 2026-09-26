---
title: "DECRYPT"
old_id: decrypt
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# DECRYPT

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
DECRYPT (input
  [USING <algorithm>] [MODE <mode>]
  KEY key
  [IV iv] [<ctr_type>] [CTR_LENGTH ctr_length]
  [COUNTER initial_counter] )
```

Алгоритмы, режимы и параметры — те же, что у [ENCRYPT](/encrypt/).

## Описание
Функция `DECRYPT` расшифровывает данные, зашифрованные симметричным шифром. На вход подаётся зашифрованный `BLOB` или двоичная строка; результат возвращается как `BLOB` или `VARBINARY`.

Алгоритм задаётся предложением `USING` (блочные: `AES`, `ANUBIS`, `BLOWFISH`, `KHAZAD`, `RC5`, `RC6`, `SAFER+`, `TWOFISH`, `XTEA`; потоковые: `CHACHA20`, `RC4`, `SOBER128`), ключ — предложением `KEY`.

Для блочных алгоритмов обязателен режим `MODE`. Вектор инициализации `IV` нужен всем блочным алгоритмам, кроме `ECB`, и всем потоковым, кроме `RC4`. Предложения `CTR_TYPE`/`CTR_LENGTH` (порядок байтов и длина счётчика) допустимы только в режиме `CTR`; `COUNTER` — только для `CHACHA20`.

Все параметры дешифрования обязаны совпадать с использованными при шифровании функцией `ENCRYPT`, иначе данные будут восстановлены некорректно.

## Пример
```sql
select decrypt(x'0154090759DF' using sober128 key 'AbcdAbcdAbcdAbcd'
               iv '01234567')
from rdb$database;

select decrypt(secret_field using aes mode ofb key '0123456701234567'
               iv init_vector)
from secure_table;
```

## См. также
[ENCRYPT](/encrypt/), [CRYPT_HASH](/crypt_hash/), [RSA_FUNCTIONS](/rsa_functions/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
