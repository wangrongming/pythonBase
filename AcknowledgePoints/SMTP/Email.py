#MUA：Mail User Agent
#MTA：Mail Transfer Agent
#MDA：Mail Delivery Agent
# 发件人 -> MUA -> MTA -> MTA -> 若干个 MTA -> MDA <- MUA <- 收件人

#1. 编写 MUA 把邮件发到 MTA； SMTP：Simple Mail Transfer Protocol
# 2. 编写 MUA 从 MDA 上收邮
    #POP：Post Office Protocol
    #IMAP：Internet Message Access Protocol
#python 对SMTP 支持分为 smtplib发送邮件和email：构造邮件

from email.mime.text import MIMEText
from email.header import Header
import smtplib
# 正文    subtype，：'plain'表示纯文本，
msg = MIMEText('hello ,send by Python ','plain','utf-8')

# msg['From'] = Header('Python 爱好者','utf-8')
# msg['To'] = Header('管理员','utf-8')
# msg['Subject'] = Header('来自 SMTP 的问候„„', 'utf-8').encode()


# # 输入 Email 地址和口令
# from_addr = '1768389896@qq.com'
# # password = 'nwylzubuddmjedhd'
# password = 'stkigodknnbrecaa' #授权码
# # 输入收件人地址:
# to_addr = '18363031210@163.com'
# # 输入 SMTP 服务器地址:
# smtp_server = 'smtp.qq.com'
#
#
#
# try:
#     server = smtplib.SMTP_SSL(smtp_server, 465)  # smtplib.SMTP() 改成了smtplib.SMTP_SSL()
#     server.set_debuglevel(1)
#     server.login(from_addr, password)
#     server.sendmail(from_addr, [to_addr], msg.as_string())
#     server.quit()
#     print("邮件发送成功")
# except smtplib.SMTPException as e:
#     print(e)

'''
163邮箱：smtp.163.com;
　　QQ邮箱：smtp.qq.com;
　　126邮箱：smtp.126.com;
　　新浪邮箱：smtp.sina.com'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '1768389896@qq.com'
password = 'stkigodknnbrecaa'
# 输入收件人地址:
to_addr = '18363031210@163.com'
# 输入 SMTP 服务器地址:
smtp_server = 'smtp.qq.com'


# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by python</p>' +
    '</body></html>', 'html', 'utf-8')

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')

server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
