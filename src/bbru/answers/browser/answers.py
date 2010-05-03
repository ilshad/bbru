# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Список ответов.
"""

from zope.component import getUtility
from zope.authentication.interfaces import IAuthentication
from zope.dublincore.interfaces import IZopeDublinCore

class Ajax:

    def __call__(self):
        formatter = self.request.locale.dates.getFormatter('date')
        auth = getUtility(IAuthentication)

        answers = []

        for k,v in self.context.items():
            dc = IZopeDublinCore(v)
            principal = auth.getPrincipal(dc.creators[0])

            answers.append({
                    'name': k,
                    'created': formatter.format(dc.created),
                    'user': principal.title,
                    'body': v.body                           
                    })

        answers.sort(key=lambda x:int(x['name']))

        return self.index(answers=answers)
