"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/17 14:11
@Author : mayonglin
@File : configHttp.py
@Software: PyCharm
功能描述：
实现逻辑：
    1-导包
    2-初始化方法内配置邮箱设置
    3-获取最新报告
    4-添加附件
    5-对外提供发送邮件的方法
"""
import smtplib, time, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

class ConfigEmail():
    def __init__(self):
        #第一步，配置邮箱属性
        #发送邮箱
        self.sender = "2929271246@qq.com"
        #接收邮箱
        self.receiver = "2929271246@qq.com"
        #发送邮件主题
        self.theme = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        self.subject = '自动化测试结果_' + self.theme
        #发送邮箱服务器
        self.stmpserver = 'smtp.qq.com'
        #发送邮箱用户/密码
        self.username = '2929271246@qq.com'
        self.pwd = 'fxifdshsbrrqdeae'
        self.current = os.path.dirname(os.path.dirname(__file__))

    def get_report(self):
        all_report = os.listdir(self.current + '/report/')
        new_report = sorted(all_report)[-1]
        with open(self.current + '/report/' + new_report, 'rb') as f:
            mail_body = f.read()
            #组装邮件内容和标题
            msg = MIMEMultipart()
            #添加附件内容
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = f'attachment; filename = {new_report}'
            msg.attach(att)
            #添加邮件的文本内容
            content = '自动化测试报告详情，请查收'
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            msg['Subject'] = Header(self.subject, 'utf-8')
            msg['From'] = self.sender
            msg['To'] = self.receiver
            return msg

    def send_email(self):
        msg = self.get_report()
        try:
            #实例化smtp类
            stmp = smtplib.SMTP()
            #连接smtp服务器
            stmp.connect(self.stmpserver)
            #登陆邮箱
            stmp.login(self.username, self.pwd)
            #设置发送人，接收人，邮件内容
            stmp.sendmail(self.sender, self.receiver.split(','), msg.as_string())
        except Exception as msg:
            print(u"邮件发送失败！%s" % msg)
        else:
            print("邮件发送成功")
        finally:
            stmp.quit()
