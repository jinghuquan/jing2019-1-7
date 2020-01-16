
# -*- coding:utf-8 -*-
from email import encoders
import os
import traceback
from email.header import Header   #定义邮件标题
from email.mime.text import MIMEText   #定义邮件内容
from email.mime.image import MIMEImage    #处理图片需要 MIMEImage 类
from email.utils import parseaddr, formataddr
import smtplib   #发送邮件模块
from email.mime.multipart import MIMEMultipart    #处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.base import MIMEBase
from email import encoders
#发送邮件服务器设置
mail_server = 'smtp.163.com'
mail_server_port = 25
#发送邮件用户名密码
username = 'test@163.com' #发送邮件账号
password = 'test123' ## 发送邮件账号密码

##发件人和收件人信息
sender = 'test@163.com'  ## 发件人邮箱, 多人逗号分开
receiver = 'test@163.com,test1@qq.com'  ## 收件人邮箱, 多人逗号分开
cc = 'test2@126.com'  # #抄送邮箱, 多人逗号分开
#邮件内容编辑
#邮件主题
subject = 'Python SMTP 邮件测试 带附件png、txt、xls(中文名称)'
#邮件正文, html有格式的文档
mail_content = '<html><h1>Python mail测试 带附件png、txt、xls(中文名称)</h1><img src="cid:0"></html>'

'''
#构造附件内容
带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身
使用MIMEMultipart来标示这个邮件是多个部分组成的，然后attach各个部分
1、构造一个MIMEMultipart对象代表邮件本身，
2、在MIMEMultipart对象上attach一个MIMEText作为邮件正文，
3、再继续往里面attach一个表示附件的MIMEBase对象,(附件需要用add_header附加声明)
4、如果有多个附件，就继续attach附件
#MIMEText有三个参数，第一个对应文本内容，第二个对应文本的格式，第三个对应文本编码
'''
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = sender
#此处msg接收的收件人,抄送人格式必须是字符串
msg['To'] = receiver
msg['Cc'] = cc
msg['Subject'] = Header(subject, 'utf-8')
#同时支持HTML和Plain格式(发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件)
msg.attach(MIMEText('Python mail测试 文本', 'plain', 'utf-8'))
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
# 添加附件就是加上一个MIMEBase
# 构造图片附件,从本地读取一个图片:
with open('图片1.png', 'rb') as img_file:
# 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
# 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=("gbk", "", "图片1.png"))
    mime.add_header('Content-ID', '<0>')    #正文中引用此图片方法为：<img src="cid:0">
# 把附件的内容读进来:
    mime.set_payload(img_file.read())
# 用Base64编码:
    encoders.encode_base64(mime)
# 添加到MIMEMultipart:
    msg.attach(mime)
# 构造文本附件，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
msg.attach(att1)
# 构造excel附件，传送指定目录下的excel文件
#读取xlsx文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码
xls_file = open("data/approve/20190718申请.xls", "rb").read()
att3 = MIMEBase('application', "octet-stream")
att3.add_header('Content-Disposition', 'attachment', filename=("utf-8", "", "20190718申请.xls"))
att3.set_payload(xls_file)
encoders.encode_base64(att3)
msg.attach(att3)

#开始发送邮件
toaddrs = receiver.split(',') + cc.split(',')
print('发件人:' + sender)
#字符串连接，先用join把toaddrs转换为字符串
print('收件人:' + ";".join(toaddrs))
try:
    server = smtplib.SMTP()
    server.connect(mail_server, mail_server_port)
    server.login(username, password)   #登录邮箱服务器用户名密码
print('开始发送邮件...')
#此处收件人和抄件人必须为列表格式，通过split将字符串转换为列表；as_string()把MIMEText对象变成str
    server.sendmail(sender, toaddrs, msg.as_string())
    server.quit()
print('邮件发送结束')
except smtplib.SMTPException:
print("Error: 无法发送邮件")