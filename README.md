# Сlient Django



## Часть проекта разработанная лично.

* Подключен Celery и его таски которые находятся в core/celery и core/task
* В приложении help_translation написана views для разовой и ежемесячной оплаты с отправкой идентификатора отмены на почту help_translation/views
* Придумана и написана логика автоплатежей с помощью базы данных help_translation/management/commands/auto.py и управляется с помощью Сelery, крон можно посмотреть core/settings.py 173-180 строчки.
* Собраны 3 контейнера в docker-compose.yaml : Redis, Celery,Celery-beat



