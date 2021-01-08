To launch nginx + gunicorn:
$ sudo brew services start nginx
$ sudo gunicorn askme.wsgi (in the django project root, gunicprn.conf.py config file should be in the project root as well)

nginx config should proxy to gunicorn properly as in the seminar

Сейчас настроено кэширование динамический запросов, обновление кжша раз в 10 минут, поэтому на главной страницу динамика отображается некорректно
TODO: корректно настроить кэширование а пока мб отключить