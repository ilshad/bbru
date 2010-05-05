# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Редактировать текст вопроса.
"""

from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent, Attributes
from bbru.answers.interfaces import IQuestion

class Ajax:

    def __call__(self):
        body = self.request.get('body')

        if body:
            self.context.body = body
            description = Attributes(IQuestion, 'body')
            notify(ObjectModifiedEvent(self.context, description))

            self.request.response.setStatus(202)
            return self.context.body

        return self.index()
