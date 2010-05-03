# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore

class Pagelet:

    def update(self):
        formatter = self.request.locale.dates.getFormatter('date')

        dc = IZopeDublinCore(self.context)
        auth = getUtility(IAuthentication)

        principal = auth.getPrincipal(dc.creators[0])
        self.user = principal.title

        self.created = formatter.format(dc.created)
