# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from z3c.configurator import ConfigurationPluginBase
from zope.security.proxy import getObject
from zope.lifecycleevent import ObjectCreatedEvent
from zope.event import notify

class AnswersConfigurator(ConfigurationPluginBase):

    def __call__(self, *args):
        site = getObject(self.context)
        sm = site.getSiteManager()

        #if u'foo' not in sm:
        #    ob = Foo()
        #    notify(ObjectCreatedEvent(ob))
        #    sm[u'foo'] = ob
        #    sm.registerUtility(ob, IFoo)
