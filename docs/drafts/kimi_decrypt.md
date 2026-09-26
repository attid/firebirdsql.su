kimi version 2.0.2
• Just write the page content. Probably output as markdown in reply; maybe write to file? User says "Напиши справочную страницу" — just output it. I'll produce the markdown directly.

• # DECRYPT

  ## Доступно в

  DSQL, PSQL

  ## Формат

  ```
  DECRYPT (encrypted_input
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

  Функция `DECRYPT` дешифрует данные, зашифрованные симметричным шифром. На вход подаётся зашифрованный BLOB или двоичная строка; результат возвращается как `BLOB` или `VARBINARY`.

  Алгоритм указывается в предложении `USING` и может быть блочным (`AES`, `ANUBIS`, `BLOWFISH`, `KHAZAD`, `RC5`, `RC6`, `SAFER+`, `TWOFISH`, `XTEA`) или потоковым (`CHACHA20`, `RC4`, `SOBER128`). Ключ шифрования передаётся в предложении `KEY`.

  Для блочных алгоритмов обязателен режим шифрования `MODE` (`CBC`, `CFB`, `CTR`, `ECB`, `OFB`). Вектор инициализации `IV` необходим для всех блочных алгоритмов, кроме режима `ECB`, и для всех потоковых алгоритмов, кроме `RC4`.

  Предложения `<ctr_type>` и `CTR_LENGTH` допустимы только в режиме `CTR`: порядок байтов счётчика по умолчанию — `CTR_LITTLE_ENDIAN`, а длина счётчика по умолчанию равна длине вектора инициализации. `COUNTER` (начальное значение счётчика, по умолчанию 0) можно указывать только для алгоритма `CHACHA20`.

  Размеры строк, передаваемых в функцию, должны соответствовать требованиям выбранного алгоритма и режима. Параметры дешифрования обязаны совпадать с теми, что использовались при шифровании функцией `ENCRYPT`, иначе данные будут восстановлены некорректно.

  ## Пример

  ```sql
  select decrypt(x'0154090759DF' using sober128 key 'AbcdAbcdAbcdAbcd'
                 iv '01234567')
  from rdb$database;

  select decrypt(secret_field using aes mode ofb key '0123456701234567'
                 iv init_vector)
  from secure_table;
  ```

To resume this session: kimi -r session_c9bf0712-ecc4-442d-accd-5a78df63b463
