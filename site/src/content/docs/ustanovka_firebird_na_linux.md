---
title: "Установка firebird на Linux"
old_id: ustanovka_firebird_na_linux
section: install
type: article
firebird:
  since: 
  until: 
  deprecated: false
---

# Установка firebird на Linux

## Ubuntu

Установка

#sudo apt-get install firebird2.5-classic

Если вам нужен супер сервер то последнее заменяется на firebird2.5-super нужная версия соответсвенно тоже подбирается с нуждами.

В некоторых версиях еще требуется создать симлинк с /usr/lib/libfbclient.so.что-то_там на /usr/lib/libfbclient.so

## RedHat, Mandriva, Debian

С официального сайта [http://www.firebirdsql.org/en/downloads/](http://www.firebirdsql.org/en/downloads/) ставим подходящую сборку сервера **FireBird** 

Устанавливаем сервер **Apache**и поддержку**PHP**(как вариант для Mandriva Linux разумно провести установку пакета**urpmi task-lamp**   подробнее см. [http://wiki.mandriva.com/ru/Linux-Apache-MySQL-PHP](http://wiki.mandriva.com/ru/Linux-Apache-MySQL-PHP)) 

После установки серверов **FireBird**, **Apache**и**PHP** подключаем поддержку FireBird через PHP.

Для этого, устанавливаем пакет **php-interbase**.
Если таковой отсутствует в репозитории, нужный пакет можно скачать с RPM-Finder [http://rpmfind.net/linux/rpm2html/search.php](http://rpmfind.net/linux/rpm2html/search.php).

Для этого в строке поиска набрать '*php-interbase*', в поле **System** -ввести операционную систему, например '*Mandriva*'

Выбрать и установить нужный пакет

## Debian 7 wheezy

Заходим под root
```
#su
```
Обновим систему
```
#apt-get update && apt-get upgrade -y
```
Установка firebird
```
#apt-get install firebird2.5-classic
```
Нажмите "yes". Необходимые пакеты будут загружены и установлены на целевую систему. Также будет создан новый пользователь “firebird” для запуска сервера, но сервер пока не будет запускаться автоматически.
Для запуска сервера Firebird автоматически при старте системы, запустите настройку dpkg-reconfigure на данном пакете и нажмите “Да” при соответствующем вопросе. Затем вам будет предложено ввести пароль SYSDBA:
```
#dpkg-reconfigure firebird2.5-classic
```
После ввода пароля и нажатия "ок" сервер FireBird будет запущен. Теперь скачиваем библиотеку UDF rfunc, заходим на сайт

https://www.assembla.com/spaces/audfl_rfunc/documents

На этом сайте скачиваем архив **rfunc.linux_amd64.tar.gz**

Скачиваем программу WinSCP и устанавливаем, затем архив перекидываем на linux.
Распаковываем его
```
#tar xvfz rfunc.linux_amd64.tar.gz
```
Копируем в папку UDF
```
#cp rfunc.so /usr/lib/firebird/2.5/UDF/
```
На этом установка завершена.
