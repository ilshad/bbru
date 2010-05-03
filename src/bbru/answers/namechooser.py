# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.container.contained import NameChooser

class IntegerNameChooser(NameChooser):

    def chooseName(self, *args):
        container = self.context
        i = 1
        while unicode(i) in container:
            i += 1
        return unicode(i)
