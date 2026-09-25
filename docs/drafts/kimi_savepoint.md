kimi version 2.0.2
• Write the reference page. Output as text file? User asks to "write a reference page" — just deliver the markdown content. Probably output directly in reply, maybe write to file. Just deliver in message.

• # SAVEPOINT

  ## Доступно в

  DSQL

  ## Формат

  ```
  SAVEPOINT sp_name
  ```

  | Параметр | Описание |
  |---|---|
  | sp_name | Имя точки сохранения. Должно быть уникальным в рамках транзакции. |

  ## Описание

  Оператор `SAVEPOINT` создаёт SQL:99 совместимую точку сохранения, к которой можно позже откатить работу с базой данных, не отменяя все действия, выполненные с момента старта транзакции. Механизм точек сохранения также известен под термином «вложенные транзакции» (nested transactions).

  Если имя точки сохранения уже существует в рамках транзакции, то существующая точка сохранения будет удалена, и создаётся новая с тем же именем.

  Для отката изменений к точке сохранения используется оператор `ROLLBACK TO SAVEPOINT`.

  :::note
  Внутренний механизм точек сохранения может использовать большие объёмы памяти, особенно если вы обновляете одни и те же записи многократно в одной транзакции. Если точка сохранения уже не нужна, но вы ещё не готовы закончить транзакцию, то можно её удалить оператором `RELEASE SAVEPOINT`, тем самым освобождая ресурсы.
  :::

  ## Пример

  DSQL-сессия с использованием точек сохранения:

  ```sql
  CREATE TABLE TEST (ID INTEGER);
  COMMIT;
  INSERT INTO TEST VALUES (1);
  COMMIT;
  INSERT INTO TEST VALUES (2);
  SAVEPOINT Y;
  DELETE FROM TEST;
  SELECT * FROM TEST; -- возвращает пустую строку
  ROLLBACK TO Y;
  SELECT * FROM TEST; -- возвращает две строки
  ROLLBACK;
  SELECT * FROM TEST; -- возвращает одну строку
  ```

  См. также: `ROLLBACK TO SAVEPOINT`, `RELEASE SAVEPOINT`.

  ---

  Страница готова. Если сайт использует Markdown, а не AsciiDoc-блоки типа `:::note`, могу заменить примечание на цитату (`>`) или жирный текст — скажите, в каком формате публикуется справочник.

To resume this session: kimi -r session_e4e5207c-b655-412c-b6f0-223ddd063e23
