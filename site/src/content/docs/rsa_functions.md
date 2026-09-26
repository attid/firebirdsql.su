---
title: "RSA-функции: RSA_PRIVATE, RSA_PUBLIC, RSA_ENCRYPT, RSA_DECRYPT"
old_id: rsa_functions
section: glossary
type: term
date: "2026-09-24"
firebird:
  since: "4.0"
  until: 
  deprecated: false
---

# RSA-функции

## Версии сервера
| 2.5 | 3.0 | 4.0 | 5.0 | 6.0 |
|---|---|---|---|---|
| − | − | Да | Да | Да |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/), [PSQL](/raznovidnosti_jazyka_sql/)

## Формат
```
RSA_PRIVATE (size)
RSA_PUBLIC (private-key)
RSA_ENCRYPT (<data> KEY <public_key> [LPARAM <tag>] [HASH <hash>])
RSA_DECRYPT (<data> KEY <private_key> [LPARAM <tag>] [HASH <hash>])

<hash> ::= { MD5 | SHA1 | SHA256 | SHA512 }
```

## Описание
Семейство функций RSA реализует в Firebird криптографию с открытым ключом: генерацию ключевой пары, извлечение открытого ключа из закрытого и асимметричное шифрование/дешифрование данных.

### RSA_PRIVATE

```
RSA_PRIVATE (size)
```

Генерирует закрытый ключ заданной длины (`size` — размер ключа в байтах) в формате PKCS#1, результат — `VARBINARY`.

### RSA_PUBLIC

```
RSA_PUBLIC (private-key)
```

Извлекает из закрытого ключа соответствующий открытый ключ (тоже PKCS#1, `VARBINARY`).

### RSA_ENCRYPT

```
RSA_ENCRYPT (<data> KEY <public_key> [LPARAM <tag>] [HASH <hash>])
```

Дополняет данные по схеме OAEP и шифрует их открытым ключом. Необязательный `HASH` задаёт алгоритм хеширования для OAEP.

### RSA_DECRYPT

```
RSA_DECRYPT (<data> KEY <private_key> [LPARAM <tag>] [HASH <hash>])
```

Выполняет обратную операцию закрытым ключом; параметры `LPARAM` и `HASH` должны совпадать с использованными при шифровании.

Поскольку RSA пригоден для шифрования лишь коротких данных, обычно им шифруют симметричные ключи, которые затем используются в блочных шифрах ([ENCRYPT](/encrypt/)/[DECRYPT](/decrypt/)) для самого сообщения. Ключи и промежуточные данные удобно хранить в контекстных переменных сессии (`RDB$SET_CONTEXT` / `RDB$GET_CONTEXT`).

## Пример
Полный цикл: генерация пары ключей, шифрование сообщения открытым ключом, расшифровка закрытым. Ключи и данные хранятся в контекстных переменных сессии.

```sql
-- Генерируем закрытый ключ длиной 256 байт
select rdb$set_context('USER_SESSION', 'private_key', rsa_private(256))
from rdb$database;

-- Извлекаем из него открытый ключ
select rdb$set_context('USER_SESSION', 'public_key',
    rsa_public(rdb$get_context('USER_SESSION', 'private_key')))
from rdb$database;

-- Шифруем сообщение открытым ключом
select rdb$set_context('USER_SESSION', 'msg',
    rsa_encrypt('Some message' key rdb$get_context('USER_SESSION', 'public_key')))
from rdb$database;

-- Расшифровываем сообщение закрытым ключом
select rsa_decrypt(rdb$get_context('USER_SESSION', 'msg')
    key rdb$get_context('USER_SESSION', 'private_key'))
from rdb$database;
```

## См. также
[ENCRYPT](/encrypt/), [DECRYPT](/decrypt/), [CRYPT_HASH](/crypt_hash/), [RDB$SET_CONTEXT](/rdb_set_context/)

## Источник
Руководство по языку SQL СУБД Firebird 5.0 (sim1984 / ibase.ru, Public Documentation License)
