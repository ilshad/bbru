# coding: utf-8
# This code was developed for http://bluebream.ru by its community and
# placed under Public Domain.

from email.MIMEText import MIMEText
from email.Header import Header
from zope.component import getUtility
from zope.sendmail.interfaces import IMailDelivery

SUPPORT_ADDR = "support@bluebream.ru"
DELIVERY = "bbru.mailer"

def send_mail(message, subject, recipient, sender=SUPPORT_ADDR):
    """Использование:
    >>> from bbru.mail.send import sendMail
    >>> send_mail("Some text", "Welcome", "man@mail.ru")
    """
    msg = MIMEText(message.encode('UTF-8'), 'plain', 'UTF-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = Header(sender, 'utf-8')
    msg['To'] = Header(recipient, 'utf-8')
    mailer = getUtility(IMailDelivery, DELIVERY)
    mailer.send(sender, [recipient,], msg.as_string())
