==================
Начальная страница
==================

:doctest:
:functional-zcml-layer: ftesting.zcml

Тестирование начальной страницы (модуль bbru.frontpage) выделено в
отдельный файл, чтобы показать, как создавать подобные тестовые файлы.

Подготовим тестовое окружение::

  >>> from zope.testbrowser.testing import Browser
  >>> root = getRootFolder()
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

Откроем начальную страницу::

  >>> browser.open(site_url)

  >>> browser.headers['status']
  '200 Ok'
