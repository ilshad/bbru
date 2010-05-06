# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Редактировать текст вопроса.
"""

from z3c.form import form, field
from bbru.answers.interfaces import IQuestion

class Ajax(form.EditForm):

    fields = field.Fields(IQuestion)
