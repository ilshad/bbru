# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Список ответов. Для каждого ответа вызывает вид "display",
рендерит его и соединяет результаты вызова видов в единый текст.
"""

from zope.interface import Interface
from zope.component import getUtility, getMultiAdapter

class Ajax:

    def __call__(self):
        answers = []
        for name, ob in self.context.items():
            view = getMultiAdapter((ob, self.request), Interface, "display")
            answers.append(view)
        answers.sort(key=lambda x:int(x.context.__name__))
        return u''.join(x() for x in answers)
