# Подключение к Firebird из Free Pascal

При поддержке или модернизации проектов на Free Pascal и Lazarus (включая миграцию старых кодовых баз с Delphi) встаёт задача надёжного подключения к СУБД Firebird. Хорошая новость: тянуть сторонние библиотеки вроде IBX, ZEOS или UIB вовсе не обязательно. Во Free Pascal входит штатный стек доступа к данным — **SQLdb** (пакет `fcl-db`). 

Связка компонентов `TIBConnection`, `TSQLTransaction` и `TSQLQuery` доступна сразу «из коробки», не требует установки сторонних пакетов и отлично подходит как для GUI-приложений Lazarus, так и для консольных утилит или фоновых демонов.

---

## Минимальный рабочий пример

Ниже приведён законченный пример консольного приложения под FPC 3.2.2, которое подключается к базе и выбирает пять самых высокооплачиваемых сотрудников.

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

---

## Подводные камни и нюансы настройки

### 1. Ошибка компиляции: свойство ConnectorType
Если вы встретите в современной документации или на форумах совет выставить `Con.ConnectorType := 'Firebird...'` — игнорируйте его для FPC 3.2.2. Это свойство появилось в более поздних ревизиях компилятора. В стабильной версии 3.2.2 у класса `TIBConnection` свойства `ConnectorType` просто **нет**, и попытка присвоить ему значение завершится фатальной ошибкой компиляции. Тип подключения полностью определяется самим классом `TIBConnection`.

### 2. Формат строки DatabaseName
Формат строки базы данных подчиняется классическому синтаксису Firebird: `host:path`. Хост и абсолютный путь к файлу базы на сервере разделяются двоеточием (например, `192.168.1.10:/var/lib/firebird/data/employee.fdb`). При запуске в Docker Compose в качестве `host` указывается имя соответствующего сервиса из `docker-compose.yml` (в коде выше — `firebird`).

### 3. Рантайм в Linux: поиск клиента и симлинк
В Linux-окружении FPC 3.2.2 динамически загружает клиентскую библиотеку, перебирая строго зашитые в рантайме имена: `libfbclient.so.2.5.1` или устаревший `libgds.so`. Современные дистрибутивы (Debian, Ubuntu) при установке пакета `libfbclient2` создают библиотеки с другими версиями soname (например, `libfbclient.so.2` или `libfbclient.so.3.0.8`). Из-за этого FPC не находит установленный клиент и падает в рантайме.

Решение — вручную создать симлинк на реальную библиотеку. При этом клиент `libfbclient` версии 3.0.8 из репозиториев Ubuntu без нареканий взаимодействует с современным сервером Firebird 5.0.4 по сети, так как сетевой протокол обратно совместим.

---

## Сборка в Docker через lazarus-build-station

Для предсказуемой сборки проектов на CI/CD удобно использовать готовый образ `ghcr.io/attid/lazarus-build-station` (FPC 3.2.2 + Lazarus 4.6.0), где сборка выполняется консольной командой `fpc`.

Чтобы подготовить рантайм-слой с нужной библиотекой и симлинком, добавьте в `Dockerfile` следующий шаг:

```dockerfile
RUN apt-get update \
    && apt-get install -y --no-install-recommends libfbclient2 \
    && rm -rf /var/lib/apt/lists/* \
    && REAL="$(ldconfig -p | awk '/libfbclient\.so\.[0-9]/ {print $NF; exit}')" \
    && ln -s "$REAL" /usr/lib/x86_64-linux-gnu/libfbclient.so.2.5.1 \
    && ldconfig
```

Этот скрипт автоматически определяет фактический путь к установленной библиотеке через `ldconfig` и создаёт симлинк с именем, которое ожидает FPC 3.2.2.

---

## Что почитать дальше

- Управление транзакциями в `fcl-db`: настройка `TSQLTransaction.Params` (`read_committed`, `rec_version`, `nowait`) для устранения взаимоблокировок.
- Параметризованные запросы в `TSQLQuery` и пакетная вставка больших объёмов данных (`ExecSQL`, `Params`).
- Особенности миграции с BDE/IBX на SQLdb: различия в поведении автокоммитов и генераторов первичных ключей (`Sequence` / `Gen_ID`).
- Тонкая настройка кодировок: работа с `UTF8` в связке FPC `{$H+}` и Firebird `CHARSET UTF8`.
