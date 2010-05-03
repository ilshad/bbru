# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Показать вопрос.
"""

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore
from zc.resourcelibrary import need

class Pagelet:

    def update(self):
        need('bbru.answers')

        formatter = self.request.locale.dates.getFormatter('date')
        auth = getUtility(IAuthentication)

        dc = IZopeDublinCore(self.context)
        principal = auth.getPrincipal(dc.creators[0])

        self.user = principal.title
        self.created = formatter.format(dc.created)
        self.title = dc.title
