=============================
Установка локальных компонент
=============================

:doctest:
:functional-zcml-layer: ftesting.zcml

Небольшая подготовка тестового окружения::

  >>> import transaction
  >>> import zope.component
  >>> from zope.testbrowser.testing import Browser
  >>> from zope.publisher.browser import TestRequest
  >>> from zope.interface.verify import verifyObject

  >>> root_url = 'http://localhost'
  >>> browser = Browser()

Откроем страницу на корневом объекте (bbru.rootpage)::

  >>> browser.open(root_url)
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.getLink(text=u'Admin UI').url
  'http://localhost/++skin++control'

Дотошно удостоверимся, страница содержит правильные ссылки на ресурсы скина::

  >>> 'http://localhost/@@/default.css' in browser.contents
  True

  >>> 'http://localhost/@@/js/jquery.js' in browser.contents
  True

  >>> 'http://localhost/@@/js/bbru.js' in browser.contents
  True

  >>> 'http://localhost/@@/img/bluebream_logo.png' in browser.contents
  True

и что эти ресурсы доступны::

  >>> browser.open('http://localhost/@@/default.css')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open('http://localhost/@@/js/jquery.js')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open('http://localhost/@@/js/bbru.js')
  >>> browser.headers['status']
  '200 Ok'

  >>> browser.open('http://localhost/@@/img/bluebream_logo.png')
  >>> browser.headers['status']
  '200 Ok'
