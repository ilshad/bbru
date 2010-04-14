# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.interface import implements
from zope.site.folder import Folder
from z3c.configurator import configure
from interfaces import ISite

class Site(Folder):
    implements(ISite)

def siteAdded(site, event):
    configure(site, {}, names=['_initialize',])
