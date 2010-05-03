# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from zope.interface import Interface
from zope.schema import Text

class IAnswers(Interface):
    """База данных вопросов и ответов"""

class IQuestion(Interface):
    """Вопрос"""

    body = Text()

class IQuestionAnswer(Interface):
    """Ответ на вопрос"""

    body = Text()
