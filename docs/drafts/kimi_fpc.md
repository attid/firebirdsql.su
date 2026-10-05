kimi version 2.0.2
• Write the article in Markdown, 400-550 words, Russian, living tech-reference tone. Include code verbatim, nuances. Just write it as reply or as a file? User asked to "напиши статью" — deliver in message; possibly also save file. Working dir /tmp. I'll write a file and present content. Actually deliverable is the article text; I'll write it to a file and show it. Simpler: just output the article in the final message. But file might be handy. I'll create /tmp/fpc-firebird-sqldb.md and include full text in reply.Check word count roughly 450-500. Present article in final message.

• Статья готова, сохранена в `/tmp/fpc-firebird-sqldb.md` (~470 слов). Текст целиком:

  ---

  # Подключение к Firebird из Free Pascal

  Если вы сопровождаете старое Delphi/FPC-приложение на Firebird, хорошая новость: для подключения ничего ставить не нужно. В состав Free Pascal входит библиотека **SQLdb** (пакет fcl-db), а в ней — готовый коннектор `TIBConnection`. Связка стандартная: `TIBConnection` + `TSQLTransaction` + `TSQLQuery`.

  ## Рабочий пример целиком

  Консольная программа (FPC 3.2.2, режим objfpc): читает топ-5 сотрудников по зарплате из учебной базы `employee.fdb`.

  ```pascal
  program employee_top5;

  {$mode objfpc}{$H+}

  uses
    SysUtils, SQLDB, IBConnection;

  var
    Con: TIBConnection;
    Tr: TSQLTransaction;
    Q: TSQLQuery;

  begin
    Con := TIBConnection.Create(nil);
    Tr := TSQLTransaction.Create(nil);
    Q := TSQLQuery.Create(nil);
    try
      Con.DatabaseName := 'firebird:/var/lib/firebird/data/employee.fdb';
      Con.UserName := 'SYSDBA';
      Con.Password := 'masterkey';
      Con.Transaction := Tr;
      Q.Database := Con;
      Q.Transaction := Tr;
      Q.SQL.Text :=
        'SELECT FIRST_NAME, LAST_NAME, SALARY FROM EMPLOYEE ' +
        'ORDER BY SALARY DESC ROWS 5';
      Con.Open;
      Q.Open;
      WriteLn('Топ-5 сотрудников по зарплате:');
      while not Q.EOF do
      begin
        WriteLn(Format('  %s %s — %.2f',
          [Q.FieldByName('FIRST_NAME').AsString,
           Q.FieldByName('LAST_NAME').AsString,
           Q.FieldByName('SALARY').AsFloat]));
        Q.Next;
      end;
      Con.Close;
    finally
      Q.Free;
      Tr.Free;
      Con.Free;
    end;
  end.
  ```

  Обратите внимание на формат `DatabaseName`: `host:path` — хост и путь к файлу базы разделяются двоеточием. В docker compose в качестве хоста указывайте имя сервиса с Firebird.

  ## Нюанс 1: никакого ConnectorType

  В FPC 3.2.2 у `TIBConnection` **нет** свойства `ConnectorType` — оно появилось в более поздних версиях. Попытка присвоить его даст ошибку компиляции. Если переносите пример из свежей документации — просто удалите эту строку, коннектор и так знает, что он для Firebird/InterBase.

  ## Нюанс 2: клиентская библиотека и симлинк

  Это самая частая засада. FPC 3.2.2 ищет клиентскую библиотеку по жёстко зашитым именам: `libfbclient.so.2.5.1` или `libgds.so`. Debian/Ubuntu же ставят пакет `libfbclient2` с другим soname, и программа падает в рантайме с «cannot load Firebird client library». Лечится симлинком на реальный файл из `ldconfig`.

  Приятный факт: клиент 3.0.8 из Ubuntu спокойно работает по сети с сервером Firebird 5.0.4 — протокол совместим, гнаться за пятой версией клиента не обязательно.

  ## Сборка в Docker

  Удобно собирать в образе `ghcr.io/attid/lazarus-build-station` (FPC 3.2.2 + Lazarus 4.6.0), консольной командой `fpc`. Слой с клиентской библиотекой и симлинком выглядит так:

  ```dockerfile
  RUN apt-get update \
      && apt-get install -y --no-install-recommends libfbclient2 \
      && rm -rf /var/lib/apt/lists/* \
      && REAL="$(ldconfig -p | awk '/libfbclient\.so\.[0-9]/ {print $NF; exit}')" \
      && ln -s "$REAL" /usr/lib/x86_64-linux-gnu/libfbclient.so.2.5.1 \
      && ldconfig
  ```

  После этого `fpc employee_top5.pas` собирает бинарник, который сразу находит клиент и подключается к серверу.

  ## Что почитать дальше

  - Параметризованные запросы в SQLdb (`Params`, подготовленные выражения).
  - Управление транзакциями: `CommitRetaining`, уровни изоляции.
  - `TDataSource` и DB-aware-компоненты Lazarus для GUI-приложений.
  - Альтернативные библиотеки доступа (ZeosLib, IBX) — когда SQLdb перестаёт хватать.

  ---

  Структура соответствует заданию: библиотека и почему → код дословно → ConnectorType → симлинк → Docker → дальнейшее чтение.

To resume this session: kimi -r session_69c71520-948c-4a57-a8cd-cd80ae10e4a2
