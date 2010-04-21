# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.schema import Text
from zope.interface import implements, Interface
from zope.contentprovider.interfaces import IContentProvider
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class IPoster(Interface):

    html_text = Text(title=u'html')

class Poster:
    """Если посмотреть в шаблон этого контент-провайдера
    (см. `poster.pt`) то видно, что в нем используется атрибут `html_text`.
    Его значение нужно передать из выывающего шаблона. Например:

    <div tal:define="html_text string: Привет всем. Бла-бла-бла."
         tal:content="structure provider:bbru.poster" />

    Таким образом организована передача значений из одного шаблона
    в другой без использования макросов.
    """
    implements(IContentProvider, IPoster)

    render = ViewPageTemplateFile('poster.pt')

    def __init__(self, context, request, view):
        self.context = context
        self.request = request
        self.__parent__ = view

    def update(self): pass
