==============
Отправка почты
==============

:doctest:
:functional-zcml-layer: ftesting.zcml

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

Отправка тестового сообщения::

  >>> from bbru.mail.send import send_mail

  >>> send_mail("test message", "Welcome", "man@mail.ru")
  *** Sending email from support@bluebream.ru to ['man@mail.ru']:
  MIME-Version: 1.0
  Content-Type: text/plain; charset="utf-8"
  Content-Transfer-Encoding: base64
  Subject: =?utf-8?q?Welcome?=
  From: =?utf-8?q?support=40bluebream=2Eru?=
  To: =?utf-8?q?man=40mail=2Eru?=
  <BLANKLINE>
  dGVzdCBtZXNzYWdl
  <BLANKLINE>
