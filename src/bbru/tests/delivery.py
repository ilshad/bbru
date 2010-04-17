# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from email import message_from_string
import zope.interface
from zope.sendmail.interfaces import IMailDelivery

class TestMailDelivery:
    """Этот фейк регистрируем в функциональных тестах как
    утилиту-доставщик писем вместо обычной.
    """
    zope.interface.implements(IMailDelivery)

    def send(self, fromaddr, toaddrs, message):
        print "*** Sending mail from %s to %s:" % (fromaddr, toaddr)
        print message_from_string(message).get_payload(decode=True)
        return "fake@foo.com"
