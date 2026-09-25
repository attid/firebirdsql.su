kimi version 2.0.2
• The user wants a reference page written in Russian for firebirdsql.su about CREATE SEQUENCE. Just write the page per the format. Probably output it as text, or write to a file? The task says "Напиши справочную страницу" — I'll write it to a file, e.g., create-sequence.md in /tmp, and also show it. Actually simplest: output the page as the reply. But as a CLI agent, writing to a file makes sense. I'll write to /tmp/create-sequence.md and show content. Actually, just presenting it in the reply is fine; but writing a file is more useful. I'll do both: write file, brief summary. Let me compose.

  Format:
  - H1: CREATE SEQUENCE
  - ## Доступно в
  - ## Формат
  - ## Описание (150-250 words)
  - ## Пример

  Description should mention: назначение, синонимы SEQUENCE/GENERATOR, START WITH semantics (first NEXT VALUE FOR equals start_value in FB 4.0+, before was start+increment), INCREMENT BY, отличие от смежных механизмов — GEN_ID. The general instruction mentions differences for functions/packages, but this is a sequence; the смежный механизм is GEN_ID / identity columns. Facts only include GEN_ID mention. Stick to facts strictly.

  Word count 150-250 — for Russian description.

  Write the file.Present the page in the final reply.

• Готово, страница сохранена в `/tmp/create-sequence.md`. Содержимое:

  ---

  # CREATE SEQUENCE

  ## Доступно в

  DSQL, ESQL

  ## Формат

  ```
  CREATE {SEQUENCE | GENERATOR} seq_name
  [START WITH start_value] [INCREMENT [BY] increment]
  ```

  ## Описание

  Оператор `CREATE SEQUENCE` создаёт новую последовательность (генератор) — объект базы данных, предназначенный для выдачи уникальных числовых значений, которые обычно используются в качестве суррогатных первичных ключей. Слова `SEQUENCE` и `GENERATOR` являются синонимами: можно использовать любое из них, однако рекомендуется применять `SEQUENCE`. Имя последовательности может содержать до 63 символов.

  Необязательное предложение `START WITH` задаёт начальное значение последовательности (по умолчанию равно 1). В момент создания последовательности ей устанавливается значение, указанное в `START WITH`, минус значение приращения из предложения `INCREMENT [BY]`. Если предложение `START WITH` отсутствует, последовательности устанавливается значение 1. Таким образом, если начальное значение равно 100, а приращение равно 10, то первое значение, выданное оператором `NEXT VALUE FOR`, будет равно 100. Обратите внимание: до Firebird 4.0 первое значение, выданное `NEXT VALUE FOR`, было равно 110, то есть начальному значению плюс шаг приращения.

  Необязательное предложение `INCREMENT [BY]` задаёт шаг приращения для оператора `NEXT VALUE FOR`. По умолчанию шаг приращения равен единице; значение приращения — 4-байтовое целое число. Для пользовательских последовательностей приращение не может быть установлено в ноль.

  Значение последовательности изменяется также при обращении к функции `GEN_ID`, где в качестве параметров указываются имя последовательности и значение приращения, которое может отличаться от заданного в предложении `INCREMENT BY`.

  ## Пример

  ```sql
  CREATE SEQUENCE seq_employee
    START WITH 100
    INCREMENT BY 10;

  -- Первый вызов вернёт 100, следующий — 110 и т.д.
  SELECT NEXT VALUE FOR seq_employee FROM RDB$DATABASE;
  ```

  ---

  Описание укладывается в диапазон 150–250 слов (~190 слов), все факты взяты строго из приведённого фрагмента руководства Firebird 5.0, frontmatter и внутренние ссылки отсутствуют.

To resume this session: kimi -r session_f005750c-49bf-4d33-aac4-fcf158f29a57
