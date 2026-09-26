kimi version 2.0.2
• Just write the page.

• # ENCRYPT

  ## Доступно в

  DSQL, PSQL

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

  Функция `ENCRYPT` шифрует данные с использованием симметричного шифра. В качестве входных данных (`input`) принимается выражение строкового типа или `BLOB`. Алгоритм (`algorithm`) может быть как блочным (`AES`, `ANUBIS`, `BLOWFISH`, `KHAZAD`, `RC5`, `RC6`, `SAFER+`, `TWOFISH`, `XTEA`), так и потоковым (`CHACHA20`, `RC4`, `SOBER128`).

  Параметр `mode` (режим шифрования: `CBC`, `CFB`, `CTR`, `ECB`, `OFB`) обязателен для блочных алгоритмов. Ключ задаётся параметром `KEY`. Вектор инициализации `IV` должен быть указан для всех блочных алгоритмов, кроме режима `ECB`, и для всех потоковых алгоритмов, кроме `RC4`.

  Параметры `ctr_type` (порядок байтов счётчика, по умолчанию `CTR_LITTLE_ENDIAN`) и `ctr_length` (длина счётчика в байтах, по умолчанию равна длине IV) допустимы только в режиме `CTR`. Начальное значение счётчика `COUNTER` допустимо только для алгоритма `CHACHA20` и по умолчанию равно 0.

  Функция возвращает `BLOB SUB_TYPE BINARY`, если первый аргумент — `BLOB`, и `VARBINARY` для всех остальных текстовых и двоичных типов.

  Размеры строк (`key`, `iv`) должны соответствовать требованиям выбранного алгоритма и режима. Как правило, размер `iv` должен совпадать с размером блока алгоритма. Для режимов `ECB` и `CBC` входные данные должны быть кратны размеру блока — при необходимости их следует вручную дополнить нулями или пробелами.

  ## Пример

  ```sql
  -- Потоковое шифрование SOBER128
  SELECT ENCRYPT('897897' USING SOBER128 KEY 'AbcdAbcdAbcdAbcd' IV '01234567')
  FROM rdb$database;

  -- Блочное шифрование AES в режиме CBC: входные данные дополнены до 16 байт
  SELECT ENCRYPT('secret-data-16by' USING AES MODE CBC
                 KEY '0123456789ABCDEF' IV 'FEDCBA9876543210')
  FROM rdb$database;
  ```

  ---

  См. также: `DECRYPT`.

To resume this session: kimi -r session_02d1582b-4b39-4aed-ab22-6b1a6746201f
