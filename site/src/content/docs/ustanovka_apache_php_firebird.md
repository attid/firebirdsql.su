---
title: "Установки apache php firebird"
old_id: ustanovka_apache_php_firebird
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# Установки apache php firebird

## Ubuntu

все просто 

sudo apt-get install apache2 php5-interbase firebird2.0-classic

если вам нужен супер сервер то последнее заменяется на firebird2.0-super нужная версия соответсвенно тоже подбирвется с нуждами.

в некоторых версиях еще требуется создать симлинк с /usr/lib/libfbclient.so.что-то_там на /usr/lib/libfbclient.so

## RedHat, Mandriva, Debian

Еще проще.

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
После ввода пароля и нажатия "ок" сервер FireBird будет запущен. Далее редактируем файл aliases.conf
```
#nano /etc/firebird/2.5/aliases.conf
```
Добавляем путь, где у нас будет лежать база данных. Дописываем эту строку и сохраняем
```bash
taximaster = /var/lib/firebird/2.5/data/tme_db.fdb
```
Теперь скачиваем библиотеку UDF rfunc, заходим на сайт

https://www.assembla.com/spaces/audfl_rfunc/documents

На этом сайте скачиваем архив **rfunc.linux_amd64.tar.gz**

Скачиваем программу WinSCP и устанавливаем, затем архив перекидываем на linux.
Распаковываем его
```
#tar xvfz rfunc.linux_amd64.tar.gz
```
Копируем в папку UDF
```
#cp rfunc.co /usr/lib/firebird/2.5/UDF/
```
На этом установка завершена.
