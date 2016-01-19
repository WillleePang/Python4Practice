# -*- encoding: utf-8 -*-
# Filename:

__author__ = 'pangwilllee'

from smtplib import SMTP
from poplib import POP3
from time import sleep


SMTPSVR = 'smtp-mail.outlook.com'
POP3SVR = 'pop.qq.com'

origHdrs = ['From: pangwilllee@hotmail.com',
            'To: 1252248561@qq.com',
            'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP()
sendSvr.connect(SMTPSVR)
sendSvr.login('pangwilllee@hotmail.com', '13833236981')
errs = sendSvr.sendmail('pangwilllee@hotmail.com',
                        ('1252248561@qq.com',), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(5)

recvSvr = POP3(POP3SVR)
recvSvr.user('1252248561@qq.com')
recvSvr.pass_('pangweilishi11')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep + 1:]
assert origBody == recvBody