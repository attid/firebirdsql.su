---
title: "Новости Firebird — октябрь 2026"
old_id: novosti-2026-10
section: news
type: article
date: "2026-10-31"
firebird:
  since: 
  until: 
  deprecated: false
---

# Новости Firebird — октябрь 2026

## Краудфандинг на усиление QA Firebird

Главное событие месяца касается будущего всех релизов. 8 октября [объявлен краудфандинг](https://firebirdsql.org/en/news/crowdfunding-to-improve-firebird-qa) на содержание QA-инженеров и тестовых стендов: у проекта скопилось 93 незакрытых pull request, и без полноценной проверки их нельзя вливать — это тормозит и подготовку Firebird 6. Нужна сумма около $20 000 на полгода. А 9 октября Алексей Ковязин (IBSurgeon) опубликовал [статью о том, как сейчас устроено тестирование Firebird](https://firebirdsql.org/en/news/how-firebird-qa-works-and-why-it-needs-to-be-stronger) и почему ему не хватает рук — [обсуждение в группе](https://groups.google.com/g/firebird-general/c/1EqGAEnxaM8). Если проект вам полезен — поучаствовать может каждый.

## fb-cpp 1.0.0: современная обёртка клиентского API на C++

30 октября [в группе опубликован анонс](https://groups.google.com/g/firebird-general/c/qv7pUAn30MU) **fb-cpp 1.0.0** — [библиотеки-обёртки над клиентским API Firebird на современном C++](https://asfernandes.github.io/2026/09/04/fb-cpp-1-0-0) от кор-коммиттера проекта Adriano dos Santos Fernandes. Версия 1.0.0 знаменует, что публичный API обёртки стал feature-complete — покрывает весь клиентский интерфейс Firebird. Тем, кто пишет нативные приложения на C++, стоит присмотреться.

## Database Workbench 7 release 2

[Второй релиз седьмой версии Database Workbench](https://groups.google.com/g/firebird-general/c/5jBnr195_Y4) от Upscene (30 октября): [новые просмотрщики планов выполнения запросов](https://www.upscene.com/news/item/20261028), доработки встроенных AI-функций и изменения в импорте/экспорте данных. Инструмент мульти-СУБДный, Firebird — один из основных поддерживаемых серверов.

## Firebird в sysbench: честные OLTP-бенчмарки

Zlatan Omerović написал [драйвер Firebird для sysbench](https://groups.google.com/g/firebird-general/c/8GNJPpgvM_4) — стандартного OLTP-бенчмарка, результатами которого обычно сравнивают MySQL и PostgreSQL. Теперь те же десять нагрузок (point selects, read/write, bulk insert и остальные) можно гонять и по Firebird. Драйвер использует современный объектный API (`fb_c_api.h`, `IBatch` для bulk-загрузки) и работает с Firebird 4–6. [Результаты](https://zlatanomerovic.github.io/firebird-sysbench/) пока получены на одной машине под WSL2 — автор просит сообщество запускать бенчмарк на своём железе и делиться цифрами, [исходники](https://github.com/ZlatanOmerovic/firebird-sysbench) открыты.

## FibPlus: 7.9.1 и 7.9.2

Комьюнити-продолжение Delphi-библиотеки FibPlus не сбавляет темп: [**7.9.1**](https://github.com/madorin/fibplus/releases/tag/v7.9.1) (9 октября) добавила посимвольные кодировки по колонкам (WIN1251, SJIS, KOI8 и другие), таймауты и read consistency-транзакции для Firebird 4+, параллельные воркеры sweep/backup/restore для Firebird 5+, а также около 70 исправлений. [**7.9.2**](https://github.com/madorin/fibplus/releases/tag/v7.9.2) (31 октября) — массовая вычитка багов в соединениях, транзакциях, датасетах и сервисах.

## Видео: оптимизатор Firebird 5 и записи с конференции

Денис Симонов, автор русскоязычной документации Firebird, разобрал [практические трюки с оптимизатором Firebird 5](https://rutube.ru/video/3f9ca15cc5347757c424dc9066e4b796/) — как влиять на план запроса точечно, не выключая оптимизатор целиком (2 октября). РЕД База Данных продолжает выкладывать записи выступлений с Firebird Conf 2026: [Flutter + Firebird в мобильном приложении](https://rutube.ru/video/da8de417096c11ffa9e2c1534290ba2d/) (8 октября), [Firebird как основа высоконагруженной ERP](https://rutube.ru/video/b8d23bd757e841c54199aac1c5489ba3/) (16 октября) и [Firebird в Kubernetes: от прототипа до внедрения](https://rutube.ru/video/8ef3410fca0b62c5ca035ed619d3809b/) (22 октября).

## РЕД База Данных: багбаунти и два релиза РБД Эксперт

Форк отчитался об [итогах первого этапа программы багбаунти](https://rdb.red-soft.ru/about/news/novosti/zavershen-pervyy-etap-programmy-bagbaunti-dlya-subd-red-baza-dannykh-zakryto-75-uyazvimostey-i-vypla/) (28 октября): 144 отчёта, 75 уязвимостей принято и закрыто (5 критических, 40 высоких), исследователям выплачено более 3 млн рублей. Программа продолжается. Кроме того, за месяц вышло два релиза их инструмента администрирования **РБД Эксперт**: [2026.09](https://rdb.red-soft.ru/about/news/novosti/reliz-rbd-ekspert-2026-09/) (12 октября — масштабное обновление редактора ER-диаграмм, экспорт в Mermaid/draw.io, импорт IBExpert) и [2026.10](https://rdb.red-soft.ru/about/news/novosti/reliz-rbd-ekspert-2026-10/) (30 октября — работа без обработки плана запроса, исправления зависаний при переподключении). В базе знаний проекта появился раздел [практических руководств для разработчиков](https://rdb.red-soft.ru/about/news/novosti/prakticheskie-rukovodstva-dlya-razrabotchikov/) (23 октября).

## Демо-база Marketplace на SQLtest

Slava Rozhnev (SQLtest.online) [добавил демо-базу Marketplace](https://habr.com/ru/news/1092798/) (10–11 октября): товары, продавцы, заказы и категории — реалистичная структура маркетплейса для тренировки SQL-запросов. [Попробовать](https://sqlize.online/s/JF) можно прямо в браузере.

## Мелочью

- [**Jaybird 6.0.7**](https://groups.google.com/g/firebird-general/c/RHud6T41H3k) (11 октября) — выпуск Java-драйвера с исправлениями ошибок, [анонс на официальном сайте](https://firebirdsql.org/en/news/jaybird-6-0-7-released).
- [**hqisql**](https://github.com/IBSurgeon/hqisql) от IBSurgeon (репозиторий опубликован 31 октября) — замену консольного isql на его же кодовой базе: строчный редактор с историей, подсветка синтаксиса, импорт/экспорт CSV, Parquet и Avro.

---

*Предыдущий выпуск — [сентябрь 2026](/novosti-2026-09/).*
