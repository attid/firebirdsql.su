kimi version 2.0.2
• Just write the reference page. Should I create a file or output text? The user says "Напиши справочную страницу" — probably output the markdown. No file specified; likely just output in chat. Format strictly. RECREATE vs ALTER: from facts — RECREATE = DROP+CREATE one operation, fails if dependencies; ALTER preserves privileges/dependencies... Actually ALTER VIEW from Firebird docs: ALTER VIEW doesn't fail on dependencies, preserves grants. But I must use strictly provided facts. The facts only say RECREATE fails if dependencies exist. I can state the difference: since RECREATE is DROP+CREATE, if view has dependencies it fails, unlike ALTER VIEW which modifies without dropping. That's an inference consistent with facts but "использовать строго их" — the note says "применение и отличия от ALTER — раскрой из фактов". From the facts: RECREATE drops and creates; fails if dependencies. So difference: ALTER VIEW changes definition without dropping, so dependencies (and grants) preserved; RECREATE fails with dependencies. I'll keep it minimal.

  Also version: appeared in Firebird 3.0 — mention in "Доступно в": DSQL, Firebird 3.0 и выше (user stated it appeared in 3.0, that's part of the task context).

• # RECREATE VIEW

  ## Доступно в

  DSQL, Firebird 3.0 и выше.

  ## Формат

  ```
  RECREATE VIEW viewname [ (colname [, colname ...]) ]
  AS <select_statement>
  [WITH CHECK OPTION]
  ```

  ## Описание

  `RECREATE VIEW` создаёт новое представление или пересоздаёт уже существующее под тем же именем. По сути оператор эквивалентен последовательному выполнению `DROP VIEW` и `CREATE VIEW` в рамках одной операции: если представление с именем `viewname` уже существует, сервер пытается удалить его и создать заново с определением, заданным оператором `select_statement` (оператор `SELECT`).

  Имя представления может содержать до 63 символов. Необязательный параметр `full_column_list` задаёт список столбцов представления; имена столбцов в этом списке не должны дублироваться. Предложение `WITH CHECK OPTION` контролирует попытки изменения данных через представление.

  Ключевое отличие `RECREATE VIEW` от `ALTER VIEW` вытекает из природы операции. Поскольку `RECREATE VIEW` — это удаление с последующим созданием, он не выполнится, если существующее представление имеет зависимости (на него ссылаются другие представления, хранимые процедуры, триггеры и т. п.). При этом даже при успешном пересоздании «старое» представление физически удаляется, поэтому привязанные к нему свойства теряются и должны быть восстановлены заново.

  Оператор удобен, когда представление создаётся «с нуля» или его определение полностью меняется и гарантированно отсутствуют зависимости: не нужно отдельно отслеживать, существует ли объект. Если же требуется лишь скорректировать определение представления, имеющего зависимости, следует использовать `ALTER VIEW`, который изменяет определение без удаления объекта.

  ## Пример

  ```sql
  RECREATE VIEW ACTIVE_CLIENTS (ID, NAME, CITY)
  AS
  SELECT CLIENT_ID, CLIENT_NAME, CITY
  FROM CLIENTS
  WHERE STATUS = 'ACTIVE';
  ```

To resume this session: kimi -r session_b0f9118f-6a69-4f36-b554-2bd22ecc4d56
