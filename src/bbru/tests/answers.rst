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
приложения "Вопросы и Ответы" (иначе говоря, обеспечивающая базу
данных вопросов и ответов), устанавливается не в сайт-менеджер,
а, для удобства, в корень самого сайта, чтобы треверсить по имени.

В сайт-менеджере она только регистрируется по интерфейсу как утилита.

В действительности, можно было бы и положить в сайт-менеджер, а
в во всех видах вызывать по интерфейсу из реестра. Тем не менее,
здесь сделано так - и это вполне естесственно::

  >>> from bbru.answers.interfaces import IAnswers

  >>> sm.getUtility(IAnswers) is site[u'answers']
  True
