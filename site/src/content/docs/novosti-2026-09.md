---
title: "Новости Firebird — сентябрь 2026"
old_id: novosti-2026-09
section: news
type: article
date: "2026-09-23"
firebird:
  since: 
  until: 
  deprecated: false
---

# Новости Firebird — сентябрь 2026

## PhoenixVault: новый встраиваемый движок от IBPhoenix

13 сентября IBPhoenix анонсировала [**PhoenixVault**](https://groups.google.com/g/firebird-general/c/eZy5EroDTbo) — защищённый встраиваемый движок баз данных. Детали в анонсе скупые, но само событие заметное: IBPhoenix, исторический коммерческий партнёр Firebird, входит в нишу embedded-хранилищ. Следим за развитием.

## RDB Expert 2026.08

10 сентября вышел [**RDB Expert 2026.08**](https://groups.google.com/g/firebird-general/c/UOYmZXZWtBA) — обновление русского инструмента администрирования и разработки для Firebird. По словам авторов — стабильность и удобство работы с метаданными. Наша аудитория инструмент знает — обновляйтесь.

## Firebird в Apache Arrow

1 сентября представлен [**adbcBridge**](https://groups.google.com/g/firebird-general/c/VybbExnGY2M) — мост из Firebird в мир колоночных данных Apache Arrow через ADBC, работающий поверх **ODBC-драйвера 3.5.0-rc1**. Для аналитики и дата-инженерии: pandas/Polars/DuckDB-экосистема теперь ближе. Заодно это повод обновить наш [раздел про ODBC](/odbc/) — свежий кандидат в релизы драйвера.

## Видео: оптимизация запросов и материализованные представления

В сентябре [официальный канал](https://www.firebirdsql.org/en/news/) выложил три записи: «Типичные ошибки оптимизации SQL-запросов» (части 1 и 2, 8–9 сентября) и «Материализованные представления в Firebird» (16 сентября). Оптимизационные разборы — маст-вотч для всех, кто пишет запросы к большим базам.

## Конец месяца: EmberWings 2026/3, Laravel-драйвер v4, Kubebird 0.3.0

Дополнение от 28 сентября:

- **EmberWings 2026/3** (28 сентября) — осенний номер официального журнала Firebird Foundation: [анонс в группе](https://groups.google.com/g/firebird-general/c/3oYFHYXDbZw). Foundation выпускает журнал стабильно раз в квартал, читать бесплатно.
- [**Laravel Firebird driver v4.0.0-rc.1**](https://groups.google.com/g/firebird-general/c/IYHryqT2e3s) (28 сентября) — независимо поддерживаемое продолжение Laravel-драйвера для Firebird, автор зовёт тестировщиков. Для PHP-сообщества важная новость: драйвер получает вторую жизнь.
- [**Kuberbird 0.3.0**](https://groups.google.com/g/firebird-general/c/goDYu1cN1tU) (26 сентября) — третья версия Kubernetes-оператора за месяц (0.1.0 → 0.2.0 → 0.3.0): проект развивается быстро.

## Дайджест III квартала

Официальный [обзор новостей за Q3 2026](https://firebirdsql.org/en/news/digest-of-of-q3-2026-firebird-news) вышел на границе квартала — июль–сентябрь одним списком: релизы, драйверы, инструменты и события лета-осени. Если по нашим выпускам что-то пропустил — у проекта теперь есть собственная сводка, сверьтесь с ней.

## Мелочью

- На стыке месяцев (31 августа) вышел [**Kubebird 0.2.0**](https://groups.google.com/g/firebird-general/c/TGMWYT3PAHE) — Kubernetes-оператор для Firebird: база как k8s-ресурс, со всем положенным.

---

*Предыдущий выпуск — [август 2026](/novosti-2026-08/).*
