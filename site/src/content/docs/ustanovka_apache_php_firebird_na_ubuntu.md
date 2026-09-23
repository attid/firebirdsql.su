---
title: "ustanovka apache php firebird na ubuntu"
old_id: ustanovka_apache_php_firebird_na_ubuntu
section: groups
type: landing
firebird:
  since: 
  until: 
  deprecated: false
---

# ustanovka apache php firebird na ubuntu

## Версии сервера
| 0.9 | 1.0 | 1.5.3 | 1.5.4 | 1.5.5 | 2.0 | 2.0.3 | 2.0.4 | 2.1 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| - | - | - | - | - | - | - | - | - | - | - |

## Доступно в
[DSQL](/raznovidnosti_jazyka_sql/),  [ESQL](/raznovidnosti_jazyka_sql/),  [ISQL](/raznovidnosti_jazyka_sql/),  [PSQL](/raznovidnosti_jazyka_sql/)

## Формат

## Описание

Сама установка просто до безобразия. но иногда можно наткнуться на неприятные мелочи.
также следуюет прочитать страницу тем кто получил ошибку 
PHP Fatal error:  Call to undefined function:  ibase_connect()
если же ошибку получили в windows просто надо будет использовать другие пути

и так в идеале установка несколько команд, если у вас еще не стоит firebird ставим его с репозаритория
sudo apt-get install firebird2.1-super
или скачиваем с офсайта http://firebirdsql.org

устанавливаем apache php и модуль interbase
sudo apt-get install apache2 php5 php5-interbase 

после этого мы должны включить модуль и перезапустить апач
sudo php5enmods interbase
sudo service apache2 reload

для проверки рекомендую запустить 
php5 -m

и убедиться что модуль interbase есть в списке, если нет то должна быть ошибка почему его нет
в последнем ubuntu пришлось редактировать 
sudo nano /etc/php5/conf.d/interbase.ini
и менять комментарии с # на ;

так же иногда не хватает библиотеки libgds32.so или подобной (смотреть ошибку в "php5 -m"  или "php5 index.php") тогда нужно сделать симлинки с libfbclient.2* на требуемую библиотеку  

## Пример

## См. также

## Источник
опыт (с)
