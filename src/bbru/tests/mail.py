# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

import zope.interface
from email import message_from_string
from zope.sendmail.interfaces import IMailDelivery

class FakeMailDelivery:
    """Этот фейк регистрируем в функциональных тестах как
    утилиту-доставщик писем вместо обычной.
    """
    zope.interface.implements(IMailDelivery)
    
    def send(self, source, dest, body):
        print "*** Sending email from %s to %s:" % (source, dest)
        print body
        return 'fake-message-id@example.com'

