========================
Развертывание на сервере
========================

Подразумевается использование ZEO. Если ZEO-сервер еще не развернут,
то это нужно сделать, см. `zeo-server.rst`

Само же приложение в единственном или множественном числе развертывается
как WSGI-приложение, использующее ZEO-клиент.

1. Нужно воздерживаться от использования веток из системы контроля
   версий, пусть бы и распределенной. При создании нового релиз-тэга
   GitHub автоматически публикует релиз в виде архива.

   Например, для развертывания версии 0.2.0::

      $ wget http://github.com/astoon/bbru/tarball/0.2.0
      $ tar -xzvf astoon-bbru-0.2.0-0-gf4d5037.tar.gz
      $ rm astoon-bbru-0.2.0-0-gf4d5037.tar.gz
      $ mv astoon-bbru-0.2.0-0-gf4d5037 bbru-0.2.0
      $ cd bbru-0.2.0
      
   В результате на диске будет лежать директория bbru-0.2.0

2. После распаковки необходимо собрать WSGI-приложение::

     $ python bootstrap.py
     $ bin/buildout

3. В файле `etc/deploy.zcml` есть директива (вернее 2 директивы),
   декларирующая существование глобального пользователя с абсолютными
   правами. Она закомментирована. Для того чтобы использовать
   глобального суперпользователя (а это нужно в первый раз),
   необходимо явно раскомментировать директиву и указать логин и пароль.

4. В том же файле указать пароль к почтовому ящику в директиве `smtpMailer`.

5. Предварительно прогнав тесты, запустить приложение в режиме UNIX демона::

     $ bin/test
     $ bin/paster serve --daemon zeo.ini

6. Остановить предыдущую версию приложения и удалить ее (rm -r). Поскольку
   используется ZEO-клиент, то никакой ценной информации там нет. За исключением
   логов, но они есть и в полном варианте у ZEO-сервера.

7. Зайти в административный интерфейс и провести процедуру обновления
   (см. `manage.rst`).

Другие опции команды bin/paster serve
=====================================

Осведомиться о состоянии процесса::

  $ bin/paster serve --status zeo.ini

Остановить демонизированный процесс::

  $ bin/paster serve --stop-daemon

С другими опциями можно ознакомиться в встроенной справке::

  $ bin/paster serve --help
