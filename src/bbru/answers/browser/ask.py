# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Задать вопрос.
"""

from zope.event import notify
from zope.container.interfaces import INameChooser
from zope.lifecycleevent import ObjectCreatedEvent
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from bbru.answers import Question

class Pagelet:

    def update(self):
        body = self.request.get('body')

        if body:
            ob = Question()
            ob.body = body
            notify(ObjectCreatedEvent(ob))
            name = INameChooser(self.context).chooseName(u"", ob)
            self.context[name] = ob

            # сделать создателя владельцем вопроса
            IPrincipalRoleManager(ob).assignRoleToPrincipal(
                'bbru.answers.Querist', self.request.principal.id)

            self.request.response.redirect(".")
