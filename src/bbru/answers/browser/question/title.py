# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Редактировать заголовок ответа.
"""

from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent, Attributes
from zope.dublincore.interfaces import IZopeDublinCore

class Ajax:

    def __call__(self):
        dc = IZopeDublinCore(self.context)

        if 'dctitle'in self.request:
            dc.title = unicode(self.request['dctitle'])
            description = Attributes(IZopeDublinCore, 'title')
            notify(ObjectModifiedEvent(self.context, description))

            return dc.title

        return self.index(title=dc.title)
