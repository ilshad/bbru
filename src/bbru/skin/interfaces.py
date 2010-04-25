# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

"""Здесь кроется очень многое. Смешивая различные интерфейсы слоев
(layers), мы создаем свои неповторимые слои. Смешивая различные слои,
создаем скины (skins).

В данном случае - достаточно стандартный 'суп'. Ниже перечислены
его 'ингредиенты', в порядке импортов:

1. Слой, на который зарегистрированы компоненты фреймворка z3c.form.

2. Слой, позволяющий строить полностью компонентное представление
   на основе паджелетов (составных компонентых видов) z3c.pagelet
   (альтернатива - встраивание макросов в шаблоны).

3. Слой, в котором зарегистрированы шаблоны для форм z3c.form с
   версткой на div'ах, используемые посредством пакета z3c.template.
   (Альтернативы - шаблоны с табличной версткой, шаблоны без
   использования z3c.template)

   Дело в том, что в z3c.from логика и представление отчуждены
   друг от друга. В данном пункте импортируется и подмешивается
   именно представление.

4. Стандартизированный набор минимальных паттернов поведения,
   позволяющий не кодировать в проекте многие мелкие вещи.
"""

from z3c.form.interfaces import IFormLayer
from z3c.layer.pagelet import IPageletBrowserLayer
from z3c.formui.interfaces import IDivFormLayer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class ILayer(IFormLayer, IPageletBrowserLayer, IDefaultBrowserLayer):
    """Skin layer"""

class ISkin(IDivFormLayer, ILayer):
    """Skin"""
