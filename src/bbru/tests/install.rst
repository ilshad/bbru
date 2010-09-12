=============================
Установка локальных компонент
=============================

:doctest:
:functional-zcml-layer: ftesting.zcml

Небольшая подготовка тестового окружения::

  >>> from zope.testbrowser.testing import Browser
  >>> from zope.publisher.browser import TestRequest
  >>> from zope.interface.verify import verifyObject

  >>> root = getRootFolder()

  >>> root_url = 'http://localhost'
  >>> admin_skin = root_url + '/++skin++control'
  >>> browser = Browser()

Откроем страницу на корневом объекте (bbru.rootpage)::

  >>> browser.open(root_url)
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.getLink(text=u'Admin UI').url == admin_skin
  True

Удостоверимся, страница содержит правильные ссылки на ресурсы скина::

  >>> 'http://localhost/@@/default.css' in browser.contents
  True

  >>> 'http://localhost/@@/js/jquery.js' in browser.contents
  True

  >>> 'http://localhost/@@/js/bbru.js' in browser.contents
  True

и что эти ресурсы доступны::

  >>> browser.open(root_url + '/@@/default.css')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open(root_url + '/@@/js/jquery.js')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open(root_url + '/@@/js/bbru.js')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open(root_url + '/@@/img/bluebream_logo.png')
  >>> browser.headers['status']
  '200 Ok'

Установим сайт. Здесь, в тестах, не будем пользоваться Aja'овой
контрольной панелью, но формы добавления и конфигурации сайта
доступны по своим URL'ам, так что можно их открыть как обычные
страницы.

Добавление сайта::

  >>> browser.open(root_url + '/@@add_site')
  Traceback (most recent call last):
  ...
  HTTPError: HTTP Error 401: Unauthorized

хм... надо авторизоваться::

  >>> browser.addHeader('Authorization','Basic mgr:mgrpw')
  >>> browser.handleErrors = False

Стучимся туда снова, теперь уже с менеджерскими правами::

  >>> browser.open(root_url + '/@@add_site')
  >>> browser.getControl(name='form.widgets.name').value = 'site'
  >>> browser.getControl(name='form.buttons.add').click()

и убедимся, что после отсылки формы сработал редирект::

  >>> browser.url == root_url + '/getControlDetailsContents'
  True

Проверим, что при создании сайта в него установлена утилита уникальных
идентификаторов, и она зарегистрирована в локальном реестре компонент
как утилита::

  >>> site = root[u'site']
  >>> sm = site.getSiteManager()
  >>> list(sm)
  [u'intids']

  >>> from zope.intid.interfaces import IIntIds
  >>> sm.getUtility(IIntIds)
  <zope.intid.IntIds object at ...>

Запустим обновление сайта::

  >>> browser.open(root_url + '/site/@@getControlDetailsConfigurators')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open(root_url + '/site/@@getControlDetailsConfigurators?form.pluginNames=Upgrade&form.actions.apply=True')
  >>> 'Applied: Upgrade' in browser.contents
  True

Проверка установленных утилит
+++++++++++++++++++++++++++++

Ранее была проверена установка утилиты IIntIds. В этой секции проверим все
остальные.

  >>> list(sm)
  [u'authentication', u'intids']

и вне сайт-менеджера::

  >>> list(site)
  [u'answers']

Утилита подключаемой аутентификации имеет также является контейнером
для своих плагинов и имеет ряд атрибутов. Проверим их все::

  >>> pau = sm[u'authentication']
  >>> list(pau)
  [u'group', u'principals']

  >>> pau.authenticatorPlugins == (u'principals', u'group')
  True

  >>> pau.credentialsPlugins == (u'Session Credentials',)
  True

  >>> pau.prefix == 'bbru.'
  True

Установка пользователя через конфигуратор
+++++++++++++++++++++++++++++++++++++++++

Введена возможно предустанавливать пользователя с необходимой ролью,
с помощью одного из конфигураторов:
bbru.authentication.config.CreateUserConfigurator

Воспользуемся этй возможностью, чтобы создать пользователя с логином
`frodo`, безопасным паролем `1` и системной ролью `zope.Manager`::

  >>> browser.open(root_url + '/site/@@getControlDetailsConfigurators?form.pluginNames-empty-marker=&form.pluginNames=Create+User&Create+User.title=Frodo+Baggins&Create+User.login=frodo&Create+User.password=1&Create+User.roles.0.=zope.Manager&Create+User.roles.count=1&Create+User.permissions.0.&Create+User.permissions.count=0&form.actions.apply=Apply')
  >>> 'Applied: Create User' in browser.contents
  True

Убидимся, что пользователь создан::

  >>> user = pau['principals'][u'frodo']

  >>> user.login
  u'frodo'
  
  >>> user.passwordManagerName
  'SSHA'

  >>> print user.title
  Frodo Baggins

Проверка страницы управления генерациями
========================================

Убедимся, что bbru есть в списке генераций и что с ним все в порядке::

  >>> browser.open(admin_skin +'/++control++/generations.html')
  >>> browser.getLink(text='bbru').click()

  >>> browser.headers['status']
  '200 Ok'
