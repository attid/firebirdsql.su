---
title: "SWEEP"
old_id: sweep
section: glossary
type: term
firebird:
  since: 
  until: 
  deprecated: false
---

# SWEEP

## Версии сервера
все

## Доступно в

## Формат

## Описание
Sweep это так называемая сборка мусора.

Что такое sweep и с чем его едят хорошо расписано [на сайте iBase](http://www.ibase.ru/devinfo/sweep.htm)

управлять им мы можем ключами к программе [gfix](/gfix/)

произвести sweep 
gfix -sweep database.fdb
отключит автоматический sweep
gfix database.fdb -housekeeping 0
включить автоматический sweep 
gfix database.fdb -housekeeping 20000

## Пример
```sql
  gfix -sweep 127.0.0.1:emploey -user sysdba -password masterkey
```

## См. также

## Источник
[http://ibase.ru](http://ibase.ru)
