# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Список ответов. Для каждого ответа вызывает вид "display",
рендерит его и соединяет результаты вызова видов в единый текст.
"""

from zope.interface import Interface
from zope.component import getMultiAdapter
from zope.dublincore.interfaces import IZopeDublinCore

class Ajax:

    def __call__(self):
        answers = [x for x in self.context.values()]
        answers.sort(key=lambda x:IZopeDublinCore(x).created)

        views = [getMultiAdapter((x, self.request), Interface, "display")
                 for x in answers]

        return u''.join(x() for x in views)
