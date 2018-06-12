from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
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
msg =  MIMEMultipart()

msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8')

# 邮件正文是 MIMEText:
msg.attach(MIMEText('hello, send by Python with attachment', 'plain', 'utf-8'))
#添加附件 个 MIMEBase，从本地读取一个图片:
with open('C:\\Users\\Administrator\\Desktop\\TCP.png','rb') as f:
# 设置附件的 MIME 和文件名，这里是 png 类型
    mime =  MIMEBase('image','png',filename='TCP.png')
    #加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='TCP.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    #读取附件内容
    mime.set_payload(f.read())
    #base64编码
    encoders.encode_base64(mime)
    #添加到 MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
# server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()