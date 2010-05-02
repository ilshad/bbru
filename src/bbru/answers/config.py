# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from z3c.configurator import ConfigurationPluginBase
from zope.security.proxy import getObject
from zope.lifecycleevent import ObjectCreatedEvent
from zope.event import notify

from bbru.answers.interfaces import IAnswers
from bbru.answers import Answers

class AnswersConfigurator(ConfigurationPluginBase):

    def __call__(self, *args):
        site = getObject(self.context)
        sm = site.getSiteManager()

        if u'answers' not in site:
            ob = Answers()
            notify(ObjectCreatedEvent(ob))
            site[u'answers'] = ob
            sm.registerUtility(ob, IAnswers)
