==============================================
bbru.answers - Управление Вопросами и Ответами
==============================================

:doctest:
:functional-zcml-layer: ftesting.zcml

Подготовим тестовое окружение::

  >>> from zope.testbrowser.testing import Browser
  >>> browser = Browser()
  >>> browser.addHeader('Authorization','Basic mgr:mgrpw')
  >>> browser.handleErrors = False
  >>> root_url = 'http://localhost'
  >>> site_url = root_url + '/site'

Установим и настроим сайт::

  >>> browser.open(root_url + '/@@add_site')
  >>> browser.getControl(name='form.widgets.name').value = 'site'
  >>> browser.getControl(name='form.buttons.add').click()
  >>> browser.open(root_url + '/site/@@getControlDetailsConfigurators?form.pluginNames=Upgrade&form.actions.apply=True')
  >>> 'Applied: Upgrade' in browser.contents
  True

  >>> root = getRootFolder()
  >>> site = root[u'site']
  >>> sm = site.getSiteManager()

Локальная утилита-контейнер, обеспечивающее персистентную часть
приложения "Вопросы и Ответы" (иначе говоря, обеспечивающая хранение
вопросов и ответов), устанавливается не в сайт-менеджер, а, для удобства,
в корень самого сайта, чтобы треверсить по имени.

В сайт-менеджере она только регистрируется по интерфейсу как утилита::

  >>> from bbru.answers.interfaces import IAnswers
  >>> sm.getUtility(IAnswers) is site[u'answers']
  True

Создадим пользователя gandalf с ролью модератора::

  >>> browser.open(site_url + '/@@getControlDetailsConfigurators?form.pluginNames-empty-marker=&form.pluginNames=Create+User&Create+User.title=Magus+Gandalf&Create+User.login=gandalf&Create+User.password=1&Create+User.roles.0.=bbru.answers.Moderator&Create+User.roles.count=1&Create+User.permissions.count=0&form.actions.apply=Apply')
  >>> 'Applied: Create User' in browser.contents
  True

И пользователей frodo и sam с ролью участника::

  >>> browser.open(site_url + '/@@getControlDetailsConfigurators?form.pluginNames-empty-marker=&form.pluginNames=Create+User&Create+User.title=Hobbit+Frodo&Create+User.login=frodo&Create+User.password=1&Create+User.roles.0.=bbru.Community&Create+User.roles.count=1&Create+User.permissions.count=0&form.actions.apply=Apply')
  >>> 'Applied: Create User' in browser.contents
  True

  >>> browser.open(site_url + '/@@getControlDetailsConfigurators?form.pluginNames-empty-marker=&form.pluginNames=Create+User&Create+User.title=Hobbit+Sam&Create+User.login=sam&Create+User.password=1&Create+User.roles.0.=bbru.Community&Create+User.roles.count=1&Create+User.permissions.count=0&form.actions.apply=Apply')
  >>> 'Applied: Create User' in browser.contents
  True

Добавление вопроса
++++++++++++++++++

Авторизоваться::

  >>> browser.mech_browser.addheaders = []
  >>> browser.handleErrors = False

  >>> browser.open(site_url + '/login.html')
  >>> browser.getControl(name='login').value = 'frodo'
  >>> browser.getControl(name='password').value = '1'
  >>> browser.getControl(name="SUBMIT").click()

Попытка сохранить форму без текста::

  >>> browser.open(site_url + '/answers/add')
  >>> browser.getControl(name="form.buttons.add").click()
  >>> browser.url == site_url + '/answers/add'
  True

и с текстом::

  >>> browser.getControl(name="form.widgets.body").value = "How do you do?"
  >>> browser.getControl(name="form.buttons.add").click()
  >>> browser.url == site_url + '/answers/'
  True

Просмотр вопроса не авторизованным пользователем::

  >>> browser.open(site_url + '/logout.html')

  >>> browser.open(site_url + '/answers/1/')

  >>> "How do you do?" in browser.contents
  True

  >>> "Hobbit Frodo" in browser.contents
  True

Авторизоваться::

  >>> browser.getLink(url='http://localhost/site/answers/1/loginForm.html?camefrom=http://localhost/site/answers/1/').click()

  >>> browser.getControl(name='login').value = 'sam'
  >>> browser.getControl(name='password').value = '1'
  >>> browser.getControl(name="SUBMIT").click()

  >>> browser.url == site_url + '/answers/1/'
  True

Ответ - форма для ajax-вида возвращает cnfnec 202::

  >>> browser.open(site_url + '/answers/1/add')
  >>> browser.getControl(name='form.widgets.body').value='Thanks'
  >>> browser.getControl(name='form.buttons.add').click()
  Traceback (most recent call last):
  ...
  HTTPError: HTTP Error 202: Accepted

Ответы::

  >>> browser.open(site_url + '/answers/1/listing')
  >>> 'Thanks' in browser.contents
  True

  >>> 'Hobbit Sam' in browser.contents
  True

Отредактировать ответ::

  >>> browser.open(site_url + '/answers/1/1/edit')
  >>> browser.getControl(name='form.widgets.body').value = 'Welcome!'
  >>> browser.getControl(name='form.buttons.apply').click()

  >>> browser.open(site_url + '/answers/1/listing')
  >>> 'Thanks' in browser.contents
  False

  >>> 'Welcome' in browser.contents
  True

Удалить ответ::

  >>> browser.open(site_url + '/answers/1/1/delete')
  >>> browser.getControl(name='form.buttons.delete').click()

  >>> browser.open(site_url + '/answers/1/listing')
  >>> 'Welcome' in browser.contents
  False

Отредактировать вопрос::

  >>> browser.open(site_url + '/answers/1/edit')
  Traceback (most recent call last):
  ...
  Unauthorized: (<zope.browserpage.metaconfigure.Ajax object at ...>, 'browserDefault', 'bbru.answers.EditQuestion')

  >>> browser.open(site_url + '/logout.html')

  >>> browser.open(site_url + '/login.html')
  >>> browser.getControl(name='login').value = 'frodo'
  >>> browser.getControl(name='password').value = '1'
  >>> browser.getControl(name="SUBMIT").click()

  >>> browser.open(site_url + '/answers/1/edit')
  >>> browser.getControl(name='form.widgets.body').value = 'foo bar baaz'
  >>> browser.getControl(name="form.buttons.apply").click()

  >>> browser.open(site_url + '/answers/1/')

  >>> "How do you do?" in browser.contents
  False

  >>> "foo bar baaz" in browser.contents
  True

Отредактировать заголовок::

  >>> browser.open(site_url + '/answers/1/title')
  Traceback (most recent call last):
  ...
  Unauthorized: (<zope.browserpage.metaconfigure.Ajax object at ...>, 'browserDefault', 'bbru.answers.Manage')

  >>> browser.open(site_url + '/logout.html')

  >>> browser.open(site_url + '/login.html')
  >>> browser.getControl(name='login').value = 'gandalf'
  >>> browser.getControl(name='password').value = '1'
  >>> browser.getControl(name="SUBMIT").click()

  >>> browser.open(site_url + '/answers/1/title')
  >>> browser.getControl(name='form.widgets.title').value = 'First Question'
  >>> browser.getControl(name='form.buttons.apply').click()

  >>> browser.open(site_url + '/answers/1/')
  >>> 'First Question' in browser.contents
  True

