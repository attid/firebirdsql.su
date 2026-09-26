kimi version 2.0.2
• The user wants a reference page. This is a writing task — just produce the markdown. Should I write to a file? The user says "напиши справочную страницу" — I'll output the page. No file path specified; probably just output in the reply. I'll write it as markdown in the final message.

• # RSA_PRIVATE / RSA_PUBLIC / RSA_ENCRYPT / RSA_DECRYPT (семейство функций RSA)

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```sql
  RSA_PRIVATE (size)

  RSA_PUBLIC (private-key)

  RSA_ENCRYPT (<data> KEY <public_key> [LPARAM <tag>] [HASH <hash>])

  RSA_DECRYPT (<data> KEY <private_key> [LPARAM <tag>] [HASH <hash>])

  <hash> ::= { MD5 | SHA1 | SHA256 | SHA512 }
  ```

  ## Описание

  Семейство функций RSA реализует в Firebird криптографию с открытым ключом: генерацию ключевой пары, извлечение открытого ключа из закрытого, а также асимметричное шифрование и дешифрование данных.

  `RSA_PRIVATE` генерирует закрытый ключ заданной длины, `RSA_PUBLIC` извлекает из него соответствующий открытый ключ; оба ключа представляются в формате PKCS#1 как строки `VARBINARY`. `RSA_ENCRYPT` дополняет данные по схеме OAEP и шифрует их открытым ключом, `RSA_DECRYPT` выполняет обратную операцию закрытым ключом. Поскольку RSA пригоден для шифрования лишь коротких данных, обычно с его помощью шифруют симметричные ключи, которые затем используются в блочных шифрах для шифрования самого сообщения.

  Ключи и промежуточные данные удобно хранить в контекстных переменных сессии (`RDB$SET_CONTEXT` / `RDB$GET_CONTEXT`), что позволяет выстроить полный цикл «ключи → шифрование → дешифрование» в пределах одного соединения.

  ### RSA_PRIVATE

  ```sql
  RSA_PRIVATE (size)
  ```

  **Параметры:**

  - `size` — размер ключа в байтах.

  **Тип возвращаемого результата:** `VARBINARY`

  Функция `RSA_PRIVATE` возвращает RSA закрытый ключ заданной длины (в байтах) в формате PKCS#1 как строку `VARBINARY`.

  ### RSA_PUBLIC

  ```sql
  RSA_PUBLIC (private-key)
  ```

  **Параметры:**

  - `private-key` — RSA закрытый ключ.

  **Тип возвращаемого результата:** `VARBINARY`

  Функция `RSA_PUBLIC` возвращает RSA открытый ключ для заданного RSA закрытого ключа. Оба ключа должны быть в формате PKCS#1.

  ### RSA_ENCRYPT

  ```sql
  RSA_ENCRYPT (<data> KEY <public_key> [LPARAM <tag>] [HASH <hash>])

  <hash> ::= { MD5 | SHA1 | SHA256 | SHA512 }
  ```

  **Параметры:**

  - `data` — данные (строка или BLOB) для шифрования.
  - `public_key` — открытый RSA ключ, который возвращает функция `RSA_PUBLIC`.
  - `tag` — дополнительный системный тег, который можно применять для определения того, какая система закодировала сообщение. Значение по умолчанию — `NULL`.
  - `hash` — алгоритм хеширования. По умолчанию SHA256.

  **Тип возвращаемого результата:** `VARBINARY`

  Дополняет данные, используя заполнение OAEP, и шифрует их открытым ключом RSA. Обычно используется для шифрования коротких симметричных ключей, которые затем применяются в блочных шифрах для шифрования сообщения.

  ### RSA_DECRYPT

  ```sql
  RSA_DECRYPT (<data> KEY <private_key> [LPARAM <tag>] [HASH <hash>])

  <hash> ::= { MD5 | SHA1 | SHA256 | SHA512 }
  ```

  **Параметры:**

  - `data` — данные (строка или BLOB) для дешифрования.
  - `private_key` — закрытый RSA ключ, который возвращает функция `RSA_PRIVATE`.
  - `tag` — дополнительный системный тег. Должен совпадать со значением, передававшимся в `RSA_ENCRYPT`; если теги не совпадают, функция не расшифровывает пакет. Значение по умолчанию — `NULL`.
  - `hash` — алгоритм хеширования. По умолчанию SHA256.

  **Тип возвращаемого результата:** `VARCHAR`

  Расшифровывает данные закрытым ключом RSA и удаляет OAEP-дополнение.

  ## Пример

  Полный цикл: генерация пары ключей, шифрование сообщения открытым ключом и его расшифровка закрытым ключом. Ключи и зашифрованные данные сохраняются в контекстных переменных сессии.

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

To resume this session: kimi -r session_7b43d36f-cf57-42f2-b7fa-775d7e1bdf72
