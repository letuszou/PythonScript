#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.message import *
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendmail():
    from_addr = ''
    password = ''
    to_addr = ''
    smtp_server = ''

    msg = MIMEText('2018-1-29 16:42 hello world')
    msg['From'] = u'python'
    msg['To'] = 'developer'
    msg['Subject'] = 'hello'

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


# for i in range(1,10):   server  port
sendmail()
