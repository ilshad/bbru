# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Задать вопрос.
"""

from zope.event import notify
from zope.container.interfaces import INameChooser
from zope.lifecycleevent import ObjectCreatedEvent
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
            self.request.response.redirect(".")
