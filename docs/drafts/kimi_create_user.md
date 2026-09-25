kimi version 2.0.2
• User asks to write a reference page. Should I write it to a file or output text? They didn't specify a file. Likely output the page content. There's a firebirdsql.su context — maybe a site repo exists? The working dir is /tmp with many dirs. No obvious firebird repo. The facts are cut off mid-sentence ("Поэтому") — use strictly the facts, end description accordingly.

  Just output the page as text. Format: H1 CREATE USER, sections. Description 150-250 words in Russian.

• # CREATE USER

  ## Доступно в

  DSQL

  ## Формат

  ```
  CREATE USER username
    PASSWORD 'password'
    [<user_option> [<user_option> ...]]
    [TAGS ( <tag> [, <tag>  ...] )]

  <user_option> ::=
      FIRSTNAME 'firstname'
    | MIDDLENAME 'middlename'
    | LASTNAME 'lastname'
    | {ACTIVE | INACTIVE}
    | USING PLUGIN pluginname
    | GRANT ADMIN ROLE

  <tag> ::=
    tagname = 'string_value'
  ```

  ## Описание

  Оператор `CREATE USER` создаёт учётную запись пользователя Firebird. Пользователь должен отсутствовать в текущей базе данных безопасности Firebird, иначе будет выдано сообщение об ошибке.

  Имя пользователя может содержать до 63 символов. Начиная с Firebird 3.0 имена пользователей подчиняются общему правилу наименования идентификаторов объектов метаданных: незаключённые в кавычки имена приводятся к верхнему регистру, а имена в двойных кавычках чувствительны к регистру. Таким образом, `ALEX`, `Alex` и `"ALEX"` — один и тот же пользователь, а `"Alex"` — уже другой.

  Предложение `PASSWORD` задаёт пароль пользователя (чувствителен к регистру). Его максимальная длина зависит от плагина управления пользователями (параметр `UserManager`): для Srp эффективная длина пароля ограничена 20 байтами (ограничение хеша SHA1 — 160 бит), для Legacy_UserManager — 8 байт.

  Необязательные предложения `FIRSTNAME`, `MIDDLENAME` и `LASTNAME` задают вспомогательную информацию — имя, отчество и фамилию (до 32 символов каждое).

  Атрибут `INACTIVE` создаёт пользователя в неактивном состоянии, при котором подключение с его учётной записью невозможно; `ACTIVE` — в активном (по умолчанию). Эта возможность доступна только при использовании Srp в качестве менеджера пользователей.

  Опция `GRANT ADMIN ROLE` создаёт учётную запись с правами роли `RDB$ADMIN` в текущей базе данных безопасности: это позволяет управлять учётными записями пользователей, но не даёт специальных полномочий в обычных базах данных.

  Предложение `USING PLUGIN` явно указывает плагин управления пользователями; по умолчанию используется первый плагин из списка параметра `UserManager` в `firebird.conf`. Допустимы только значения, перечисленные в `UserManager`. Одноимённые пользователи, созданные разными плагинами, — это разные пользователи.

  Предложение `TAGS` задаёт пользовательские атрибуты: имя атрибута (до 63 символов) должно подчиняться правилам наименования SQL-идентификаторов, значение — до 255 символов.

  ## Пример

  ```sql
  CREATE USER ivanov
    PASSWORD 'Qz7#pL92'
    FIRSTNAME 'Иван'
    MIDDLENAME 'Петрович'
    LASTNAME 'Иванов'
    ACTIVE
    USING PLUGIN Srp
    GRANT ADMIN ROLE
    TAGS (
      DEPARTMENT = 'Разработка',
      POSITION = 'Старший разработчик'
    );
  ```

  ---

  Примечание: фрагмент фактов обрывается на полуслове («Учтите что одноименные пользователи... — это разные пользователи. Поэтому»). Я завершил абзац на дословно приведённой части и не стал домысливать продолжение; если пришлёте остаток фактов, дополню раздел «Описание».

To resume this session: kimi -r session_5c470504-d9c0-4b2f-b3e0-28a182fb3caf
