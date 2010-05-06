# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Предложить ответ.
"""

from z3c.form import form, field
from zope.securitypolicy.interfaces import IPrincipalRoleManager
from zope.container.interfaces import INameChooser
from bbru.answers import QuestionAnswer, IQuestionAnswer

class Ajax(form.AddForm):

    fields = field.Fields(IQuestionAnswer)

    def create(self, data):
        ob = QuestionAnswer()
        form.applyChanges(self, ob, data)
        return ob

    def add(self, ob):
        name = INameChooser(self.context).chooseName(u"", ob)
        self.context[name] = ob

        # сделать создателя владельцем ответа
        IPrincipalRoleManager(ob).assignRoleToPrincipal(
            'bbru.answers.Respondent', self.request.principal.id)

    def render(self):
        if self._finishedAdd:
            self.request.response.setStatus(202)
            return ""
        return super(Ajax, self).render()
