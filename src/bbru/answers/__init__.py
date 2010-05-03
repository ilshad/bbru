# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from persistent import Persistent
from zope.container.btree import BTreeContainer
from zope.container.contained import Contained, NameChooser
from zope.interface import implements

from interfaces import IAnswers, IQuestion, IQuestionAnswer

class Answers(BTreeContainer):
    implements(IAnswers)

class Question(BTreeContainer):
    implements(IQuestion)
    body = u''

class QuestionAnswer(Contained, Persistent):
    implements(IQuestionAnswer)
    body = u''

class IntegerNameChooser(NameChooser):

    def chooseName(self, *args):
        container = self.context
        i = 1
        while unicode(i) in container:
            i += 1
        return unicode(i)
