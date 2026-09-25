kimi version 2.0.2
• Write the reference page. Facts: CLOSE only in PSQL. Syntax. Description 100-200 words in Russian. Example(s). Should I create a file? The user says "напиши справочную страницу" — likely output as markdown. I'll write a file maybe? Better to output in message; maybe also save file? Just output markdown in reply. Could also save to a file for convenience. I'll just output text.

  Description 100-200 words. Example: declare cursor, open, fetch loop, close.

• # CLOSE

  ## Доступно в

  PSQL

  ## Формат

  ```sql
  CLOSE cursor_name;
  ```

  | Параметр | Описание |
  |---|---|
  | cursor_name | Имя открытого курсора. Курсор с таким именем должен быть предварительно объявлен с помощью оператора `DECLARE ... CURSOR`. |

  ## Описание

  Оператор `CLOSE` закрывает открытый курсор. Он применим только к курсорам, объявленным в операторе `DECLARE ... CURSOR`, — закрыть с его помощью что-либо ещё нельзя.

  Явное закрытие не является строго обязательным: любые курсоры, оставшиеся открытыми, будут автоматически закрыты после завершения выполнения кода триггера, хранимой процедуры, хранимой функции или анонимного PSQL-блока, в пределах которого они были открыты. Тем не менее явный `CLOSE` делает код понятнее и позволяет освободить курсор сразу, как только работа с набором данных завершена, не дожидаясь выхода из PSQL-модуля.

  Типичный жизненный цикл курсора в PSQL выглядит так: объявление через `DECLARE ... CURSOR`, открытие оператором `OPEN`, последовательное чтение строк оператором `FETCH` и, наконец, закрытие оператором `CLOSE`.

  См. также: `DECLARE ... CURSOR`, `OPEN`, `FETCH`.

  ## Пример

  ```sql
  SET TERM ^;

  CREATE OR ALTER PROCEDURE list_customers
  RETURNS (cust_name VARCHAR(50))
  AS
    DECLARE c CURSOR FOR (SELECT name FROM customers ORDER BY name);
  BEGIN
    OPEN c;
    WHILE (1 = 1) DO
    BEGIN
      FETCH c INTO :cust_name;
      IF (ROW_COUNT = 0) THEN LEAVE;
      SUSPEND;
    END
    CLOSE c;
  END^

  SET TERM ;^
  ```

  ```sql
  EXECUTE BLOCK
  RETURNS (total NUMERIC(15,2))
  AS
    DECLARE c CURSOR FOR (SELECT amount FROM orders WHERE status = 'N');
    DECLARE amount NUMERIC(15,2);
  BEGIN
    total = 0;
    OPEN c;
    WHILE (1 = 1) DO
    BEGIN
      FETCH c INTO :amount;
      IF (ROW_COUNT = 0) THEN LEAVE;
      total = total + amount;
    END
    CLOSE c;
    SUSPEND;
  END
  ```

To resume this session: kimi -r session_9bcef933-3006-4ef0-84dc-972f978dd0b1
