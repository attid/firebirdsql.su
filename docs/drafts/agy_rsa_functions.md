# RSA_PRIVATE / RSA_PUBLIC / RSA_ENCRYPT / RSA_DECRYPT (семейство функций RSA)

## Доступно в
DSQL, PSQL

## Формат
```
RSA_PRIVATE (size)

RSA_PUBLIC (private-key)

RSA_ENCRYPT (<data> KEY <public_key> [LPARAM <tag>] [HASH <hash>])

RSA_DECRYPT (<data> KEY <private_key> [LPARAM <tag>] [HASH <hash>])

<hash> ::= { MD5 | SHA1 | SHA256 | SHA512 }
```

## Описание
Семейство криптографических функций RSA предназначено для генерации пар асимметричных ключей, а также шифрования и расшифровки данных с использованием схемы заполнения OAEP.

### RSA_PRIVATE
Генерирует и возвращает закрытый RSA-ключ заданной длины `size` (в байтах) в формате PKCS#1. Возвращаемый тип данных — `VARBINARY`.

### RSA_PUBLIC
Возвращает открытый RSA-ключ в формате PKCS#1 для заданного закрытого ключа `private-key`. Возвращаемый тип данных — `VARBINARY`.

### RSA_ENCRYPT
Выполняет дополнение данных `data` (строки или BLOB) по стандарту OAEP и шифрует их открытым ключом `public_key`. Параметр `HASH` определяет алгоритм хеширования (по умолчанию `SHA256`). Дополнительный параметр `LPARAM` (`tag`, по умолчанию `NULL`) позволяет передать системный тег для идентификации источника кодирования. Возвращает `VARBINARY`. Обычно применяется для шифрования коротких симметричных ключей блочных шифров.

### RSA_DECRYPT
Расшифровывает зашифрованные данные `data` закрытым ключом `private_key` и удаляет OAEP-дополнение. Значение системного тега `LPARAM` должно строго совпадать с тегом, переданным в `RSA_ENCRYPT`, иначе операция расшифровки не будет выполнена. Параметр `HASH` (по умолчанию `SHA256`) задаёт используемый алгоритм хеширования. Возвращаемый тип данных — `VARCHAR`.

## Пример
```sql
-- Генерация пары ключей, шифрование открытым ключом и расшифровка закрытым
EXECUTE BLOCK
RETURNS (
    decrypted_msg VARCHAR(100)
)
AS
DECLARE VARIABLE priv_key VARBINARY(2048);
DECLARE VARIABLE pub_key  VARBINARY(2048);
DECLARE VARIABLE enc_data VARBINARY(2048);
BEGIN
    -- Генерация закрытого ключа (256 байт) и извлечение открытого
    priv_key = RSA_PRIVATE(256);
    pub_key  = RSA_PUBLIC(:priv_key);

    -- Шифрование сообщения открытым ключом с использованием системного тега
    enc_data = RSA_ENCRYPT('Секретное сообщение' KEY :pub_key LPARAM 'SysTag' HASH SHA256);

    -- Расшифровка закрытым ключом с указанием того же тега и хеша
    decrypted_msg = RSA_DECRYPT(:enc_data KEY :priv_key LPARAM 'SysTag' HASH SHA256);

    SUSPEND;
END;
```
