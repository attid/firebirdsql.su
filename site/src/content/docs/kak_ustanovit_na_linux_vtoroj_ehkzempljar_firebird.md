---
title: "Как установить на LINUX второй экземпляр Firebird"
old_id: kak_ustanovit_na_linux_vtoroj_ehkzempljar_firebird
section: install
type: article
firebird:
  since: "2.5"
  until: 
  deprecated: false
---

# Как установить на LINUX второй экземпляр Firebird

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | Да | Да |

## Описание

1. Скачиваем [linux-снапшот](http://web.firebirdsql.org/download/snapshot_builds/linux/)

2. Распаковываем его на сервере, например, сюда: /opt/fb25_26387

3. Входим как root, идём в каталог /etc/xinet.d

4. Копируем файл: cp firebird fb25_26387. Открываем файл firebird25_26387 редактором, вносим следующие исправления:
```
service gds_db1
{
        disable = no
        flags           = REUSE
        socket_type     = stream
        wait            = no
        user                    = firebird
        server          = /opt/fb25_26387/bin/fb_inet_server
}
```

5. Открываем файл /etc/services, добавляем туда строку:
```
gds_db1         3051/tcp  #3051 = номер порта, на котором будет нас "слушать" второй ФБ
```

6. Выполняем перезапуск xinetd:
```
[root@firebirdG etc]# service xinetd reload
Reloading xinetd:                                           [  OK  ]
```
7. Проверяем системный лог: в последних его строках должно быть примерно следующее:
```
[root@firebirdG log]# tail -10 /var/log/messages
Nov  5 01:02:27 firebirdG xinetd[13055]: Exiting...
Nov  5 01:02:27 firebirdG xinetd[13222]: xinetd Version 2.3.14 started with libwrap loadavg labeled-networking options compiled in.
Nov  5 01:02:27 firebirdG xinetd[13222]: Started working: 2 available services
```

8. Проверяем наши права на Главный тестовый файл - таблицу /opt/fb25_26387/examples/empnuild/employee.fdb:
```
ls -la ./examples/empnuild/employee.fdb
```
В случае получения прав только на чтение суперпользователем:
```
-r--r--r-- 1 root root 1105920 Nov  5 00:51 ./examples/empbuild/employee.fdb
```
-- немедленно выправляем ситуацию:
```
chown firebird ./examples/empbuild/employee.fdb
chmod u+w ./examples/empbuild/employee.fdb
```

9. Выходим из-под root'a (logout). Работая далее как `firebird`, переходим в папку нового инстанса и пробуем коннект:

```
[firebird@firebirdG fb25_26387]$ ./bin/isql localhost/3051:/opt/fb25_26387/examples/empbuild/employee.fdb -user sysdba -pas *******
Database:  localhost/3051:/opt/fb25_26387/examples/empbuild/employee.fdb

SQL> select count(*) from employee;

       COUNT
============
          42

SQL> exit;
```

ЗЫ-1. <u>ОСОБОЕ</u> внимание хочу обратить на граблю с правами на employee.fdb: с некоторого недавнего времени они при сборке закладываются внутрь .tgz именно такими: -r--r--r--. Если после скачивания снапшота устанавливать его "официальным скриптом" install.sh, то на все файлы будет применена нужная маска прав. Но этому скрипту нельзя указать "свою" папку и "свой порт". Поэтому я его не запускал. За что и поплатился (см выше "no permission for read-write access to database").

ЗЫ-2. **НЕ трогаем файл firebird.conf** - его параметры RemoteServiceName и RemoteServicePort никакой роли не играют.

## Источник
[Таблоид, SQL.RU](http://www.sql.ru/forum/actualutils.aspx?action=gotomsg&tid=892598&msg=11552600])
