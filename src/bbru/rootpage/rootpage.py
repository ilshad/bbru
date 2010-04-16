# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

""" Страница, показываемая на самом корне дерева объектов
системному администратору.

BlueBream имеет свободную политику для определения того, как
конструировать и структурировать WSGI-приложения на его основе.
Поэтому специальной такой страницы нет по умолчанию (модуль
`welcome` из типового Paster-шаблона не в счет: его, как правило,
нужно удалять, когда начинаешь писать проект).

Что нам нужно здесь? Сделаем листинг вложенных объектов,
показывающий только локальные сайты и пропускающий другие
объекты, если они вдруг есть.
"""

from zope.component.interfaces import ISite

class Pagelet:

    def sites(self):
        return [x for x in self.context.values() if ISite.providedBy(x)]
