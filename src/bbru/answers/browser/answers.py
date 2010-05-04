# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Список ответов.
"""

from zope.interface import Interface
from zope.component import getUtility, getMultiAdapter
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore

class Ajax:

    def __call__(self):
        answers = []
        for name, ob in self.context.items():
            view = getMultiAdapter((ob, self.request), Interface, "simple")
            answers.append(view)
        answers.sort(key=lambda x:int(x.context.__name__))
        return u''.join(x() for x in answers)

class Simple:

    def __call__(self):
        formatter = self.request.locale.dates.getFormatter('date')
        auth = getUtility(IAuthentication)

        dc = IZopeDublinCore(self.context)
        principal = auth.getPrincipal(dc.creators[0])

        self.created = formatter.format(dc.created)
        self.user = principal.title

        return self.index()
