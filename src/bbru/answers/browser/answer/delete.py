# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Удалить ответ.
"""

from z3c.form import form, button

class Ajax(form.Form):

    @button.buttonAndHandler(u"Удалить", name="delete")
    def handleDelete(self, action):
        name = self.context.__name__
        parent = self.context.__parent__
        del parent[name]

    @button.buttonAndHandler(u"Отмена", name="cancel")
    def handleCancel(*args): pass
