# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Редактировать заголовок ответа.
"""

from z3c.form import form, field
from zope.dublincore.interfaces import IZopeDublinCore

class Ajax(form.EditForm):

    fields = field.Fields(IZopeDublinCore).select('title')
