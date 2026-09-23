---
title: "Установка Firebird из снапшота"
old_id: ustanovka_firebird_iz_snapshota
section: install
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# Установка Firebird из снапшота

В данной статье рассматривается пример установки Firebird вручную из архива или из архива снапшота.

## Windows

Задача: установить Firebird a) SuperServer или SuperClassicServer, б) ClassicServer в каталог "c:\appl\firebird" из архива (архива снапшота).

⚠️ **Примечание:** При установке на "голую" операционную систему возможно понадобиться предварительная установка Visual C+ Runtime библиотек. Для этого воспользуйтесь утилитами: [Microsoft Visual C++ 2005 Redistributable Package (x86)](http://www.microsoft.com/downloads/details.aspx?FamilyId=32BC1BEE-A3F9-4C13-9C99-220B62A191EE&displaylang=en) или [Microsoft Visual C++ 2005 Redistributable Package (x64)](http://www.microsoft.com/downloads/details.aspx?familyid=90548130-4468-4BBC-9673-D6ACABD5D13B&displaylang=en) в зависимости от версии Вашей операционной системы.

Установка:

  1. Скачиваем дистрибутив Firebird [с официального сайта](http://firebirdsql.org/downloads/snapshot_builds/win/).
  1. При помощи программы архиватора распаковываем архив в каталог "c:\appl\firebird"
  1. Настраиваем сервер, внося изменения в файле "c:\appl\firebird\firebird.conf"
  1. Запускаем программу "Командная строка"
  1. Выполняем команды:
  - Для установки SuperServer или SuperClassicServer
```
 > cd c:\appl\firebird\bin
 > install_super.bat
```
  - Для установки ClassicServer
```
 > cd c:\appl\firebird\bin
 > install_classic.bat
```

Все, сервер установлен и запущен.

## LINUX

## См. также
