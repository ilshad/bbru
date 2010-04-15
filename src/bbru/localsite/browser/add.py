# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from z3c.form import form, field, button
from zope.schema import TextLine
from zope.container.interfaces import INameChooser
from zope.lifecycleevent import ObjectCreatedEvent
from zope.event import notify
from bbru.localsite.localsite import Site

class Add(form.Form):
    """Добавить локальный сайт. Форма зарегистрирована как Details вид на
    корневой папке, доступный в административном интерфейсе.
    """

    fields = field.Fields(field.Field(TextLine(), name='name'))
    ignoreContext = True
    ignoreReadonly = True

    @button.buttonAndHandler(u"Добавить", name="add")
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        site = Site()
        notify(ObjectCreatedEvent(site))
        name = INameChooser(self.context).chooseName(data['name'], site)
        self.context[name] = site
        self.request.response.redirect("getControlDetailsContents")
