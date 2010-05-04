# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

import urllib
from zope.component.hooks import getSite
from zope.security import checkPermission
from zope.traversing.browser.absoluteurl import absoluteURL
from z3c.menu.ready2go.item import ContextMenuItem

class FilterPermissionAction(ContextMenuItem):
    """ Класс для элементов меню, доступных только тогда,
    когда _не_хватает_ определенного разрешения. Его можно указать
    позиционным аргументом filter_permission в zcml-директиве.
    """

    filter_permission = None # указать в zcml-директиве

    @property
    def available(self):
        return not checkPermission(self.filter_permission, self.context)

class LoginAction(FilterPermissionAction):
    """ Обычно это не требуется, т.к. фреймворк сам перенаправляет
    на страницу авторизации, если не хватает прав (в deploy-режиме).
    Однако иногда полезно сделать элемент меню с прямо заданным
    подобным поведением, например для Ajax-форм.
    """

    next_name = None # указать в zcml-директиве

    @property
    def url(self):
        context_url = absoluteURL(self.context, self.request)

        return u'%s/loginForm.html?camefrom=%s' % (
            context_url, context_url + u'/' + self.next_name)
