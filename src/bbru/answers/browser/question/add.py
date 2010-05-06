# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Задать вопрос.
"""

from z3c.form import field
from z3c.formui import form
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.container.interfaces import INameChooser
from bbru.answers import Question, IQuestion

class Pagelet(form.AddForm):

    fields = field.Fields(IQuestion)

    def create(self, data):
        ob = Question()
        form.applyChanges(self, ob, data)
        return ob

    def add(self, ob):
        name = INameChooser(self.context).chooseName(u"", ob)
        self.context[name] = ob

        # сделать создателя владельцем вопроса
        IPrincipalRoleManager(ob).assignRoleToPrincipal(
            'bbru.answers.Querist', self.request.principal.id)

    def nextURL(self):
        return "."
