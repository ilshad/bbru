# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from z3c.form.interfaces import IFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer
from z3c.formui.interfaces import IDivFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class ILayer(IFormLayer, IPageletBrowserLayer, IDefaultBrowserLayer):
    """Skin layer"""

class ISkin(IDivFormLayer, ILayer):
    """Skin"""
