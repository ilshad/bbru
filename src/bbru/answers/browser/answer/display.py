# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Список ответов.
"""

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore

class View:

    def __call__(self):
        formatter = self.request.locale.dates.getFormatter('date')
        auth = getUtility(IAuthentication)

        dc = IZopeDublinCore(self.context)
        principal = auth.getPrincipal(dc.creators[0])

        self.created = formatter.format(dc.created)
        self.user = principal.title

        return self.index()
