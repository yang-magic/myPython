import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_user = "3459677992@qq.com"  # 用户名
mail_pass = "gaemspbgqfpjcjcd"  # 口令


sender = '3459677992@qq.com'
receivers = ['3459677992@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#3428573186
txt="""
2020年04月17日　星期五　庚子年三月廿五 
当前温度:16℃
整体情况:Light Rain
今天可能有雨，注意带伞!!!
温度:12 ~ 19℃
空气质量：优
PM: 19
湿度：99%
紫外线：无
日出: 05:59
日落: 19:03
"""
message = MIMEText(txt, 'plain', 'utf-8')
message['From'] = Header("杨晨", 'utf-8')
message['To'] = Header("燕玲", 'utf-8')

#主题
subject = '天气'
message['Subject'] = Header(subject, 'utf-8')

# try:
server = smtplib.SMTP_SSL(mail_host)
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")
