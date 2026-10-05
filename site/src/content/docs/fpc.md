---
title: "Подключение к Firebird из Free Pascal"
old_id: fpc
section: groups
type: article
date: "2026-10-05"
firebird:
  since: 
  until: 
  deprecated: false
---

# Подключение к Firebird из Free Pascal

Firebird и Pascal связаны исторически (InterBase grew up в Borland Pascal мире), и связка работает как в старых добрых: **SQLdb** из состава Free Pascal — `TIBConnection` + `TSQLTransaction` + `TSQLQuery`. Ничего дополнительно не ставится: fcl-db входит в комплект FPC. Понадобится только клиентская библиотека `libfbclient` в рантайме (см. нюанс ниже).

Проверено на FPC 3.2.2 против Firebird 5.0.4; клиент 3.0.8 (Ubuntu) с сервером 5.0.4 по сети работает без проблем — протокол совместим.

## Код

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

`DatabaseName` — `host:path`: хост и путь к базе через двоеточие. В docker compose хост — имя сервиса.

## Нюанс 1: ConnectorType

В FPC 3.2.2 у `TIBConnection` **нет свойства `ConnectorType`** — оно появилось в более новых версиях fcl-db. Попытка присвоить даёт ошибку компиляции `identifier idents no member`. Просто не используйте.

## Нюанс 2: клиентская библиотека

FPC 3.2.2 ищет `libfbclient` по жёстко зашитым именам (`libfbclient.so.2.5.1`, `libgds.so`), а Debian/Ubuntu ставят клиент с другим soname. Рантайм-ошибка выглядит так:

```
EInOutError: Can not load default Firebird clients
("libfbclient.so.2.5.1" or "libgds.so" or "libfbembed.so.2.5")
```

Лечение — симлинк на реальную библиотеку (soname ищем через ldconfig).

## Сборка в Docker

[attid/lazarus-build-station](https://github.com/attid/lazarus-build-station) — образ с FPC 3.2.2 + Lazarus 4.6.0 для воспроизводимых сборок (включая кросс-компиляцию в Windows). Поверх — слой с клиентом Firebird и симлинком:

```dockerfile
FROM ghcr.io/attid/lazarus-build-station:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends libfbclient2 \
    && rm -rf /var/lib/apt/lists/* \
    && REAL="$(ldconfig -p | awk '/libfbclient\.so\.[0-9]/ {print $NF; exit}')" \
    && ln -s "$REAL" /usr/lib/x86_64-linux-gnu/libfbclient.so.2.5.1 \
    && ldconfig

WORKDIR /app
COPY main.pas .
RUN fpc -FE. main.pas

CMD ["./main"]
```

## Пример целиком

Рабочий пример с этим кодом — в [репозитории сайта](https://github.com/attid/firebirdsql.su/tree/main/examples/fpc): Dockerfile на lazarus-build-station + docker compose с Firebird 5.0.4 и демо-базой employee, прогоняется одной командой.

## Что почитать дальше

- [Порты Firebird](/port_3050/) — что открывать в firewall
- [gbak: резервное копирование](/gbak/) — бэкап без остановки сервера
- [Глоссарий](/glossarij/) — сам язык SQL с примерами
