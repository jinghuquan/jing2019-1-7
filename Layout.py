import smtplib
from smtplib import SMTP_SSL
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = 'smtp.sina.com'  # sina邮箱smtp服务器
sender_sina= '13432123694@sina.cn'  # sender_sina 为发件人的邮箱
pwd = 'jing1213548100' # pwd为邮箱的密码

sender_sina_mail = '13432123694@sina.cn'  # 发件人的邮箱
receiver = '13432123694@sina.cn' # 收件人邮箱

mail_title = 'python办公自动化的邮件' # 邮箱标题
mail_content = "你好，这是使用python登录Sina邮箱发送邮件的测试: https://www.python.org"  # 邮件的正文

msg = MIMEMultipart()  # 邮件主体
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_sina_mail
msg["To"] = Header("测试邮箱", 'utf-8')
msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

smtp = SMTP_SSL(host_server)  # ssl登录
smtp.login(sender_sina, pwd)
smtp.sendmail(sender_sina_mail, receiver, msg.as_string())
smtp.quit()