# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from email.MIMEText import MIMEText
from email.Header import Header
from zope.sendmail.interfaces import IMailDelivery
from zope.component import getUtility

SUPPORT_ADDR = "support@bluebream.ru"
DELIVERY = "bbru-delivery"

def sendMail(message, subject, toAddr, fromAddr=SUPPORT_ADDR):
    """Использование:
    >>> from bbru.mail.send import sendMail
    >>> sendMail("Some text", "Welcome", "man@mail.ru")
    """
    msg = MIMEText(message)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(fromAddr, 'utf-8')
    msg['To'] = Header(toAddr, 'utf-8')
    mailer = getUtility(IMailDelivery, DELIVERY)
    mailer.send(fromAddr, [toAddr,], msg.as_string())
