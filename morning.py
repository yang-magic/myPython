import os
import requests
from lxml import etree
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import regex

def getit(url1,receivers1):
    #初始化打开
    txt=open('log.txt','w',encoding='utf-8' )

    #获取html
    url=url1
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
    r=requests.get(url,headers=header)
    r.encoding="utf-8"
    r=r.text
    r=etree.HTML(r)

    #地点
    where=r.xpath("//h2/text()")
    print(where[0])
    txt.write(where[0]+'\n')

    #日期
    date=r.xpath("//dd[@class='week']/text()")
    da=regex.findall(r"庚子年(.+)",date[0])
    da=''.join(da)
    print(da)
    txt.write('阴历:庚子年'+da+'\n')

    #当前温度
    a=r.xpath("//dd[@class='weather']/p/b/text()")
    print('当前温度:'+a[0]+'℃')
    txt.write("当前温度:"+a[0]+'℃\n')

    # 整体情况
    b=r.xpath("//dd[@class='weather']/span/b/text()")
    print("整体情况:"+b[0])
    txt.write('整体情况:'+b[0]+'\n')
    rain='雨' in b[0]
    ti="早安，今天天气："+b[0]
    if rain:
        print("今天可能有雨，注意带伞！！！")
        txt.write("今天可能有雨，注意带伞！！！\n")
        ti='早安！可能有雨哦!记得带伞!!!'

    #低高温度
    c=r.xpath("//dd[@class='weather']/span/text()")
    print("高低温:"+c[0])
    txt.write("高低温:"+c[0]+'\n')

    #空气质量
    d=r.xpath("//dd[@class='kongqi']/h5/text()")
    print(d[0])
    txt.write(d[0]+'\n')
    d=r.xpath("//dd[@class='kongqi']/h6/text()")
    print(d[0])
    txt.write(d[0]+'\n')

    #紫外线
    e=r.xpath("//dd[@class='shidu']/b[1]/text()")
    print(e[0])
    txt.write(e[0]+'\n')
    e=r.xpath("//dd[@class='shidu']/b[3]/text()")
    print(e[0])
    txt.write(e[0]+'\n')

    #日出日落
    f=r.xpath("//dd[@class='kongqi']/span/text()")
    print(f[0]+f[1])
    txt.write(f[0]+'\n')
    txt.write(f[1]+'\n')

    #保存
    txt.close()

    #读取txt
    txt2=open('zao.txt','r',encoding='utf-8' )
    txt3=txt2.read()
    print("获取成功！！！")
    # return txt3

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "yangcode@qq.com"  # 用户名
    mail_pass = "gaemspbgqfpjcjcd"  # 口令

    sender = '3459677992@qq.com'
    receivers = receivers1  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #3428573186
    # receivers2 = ['1493481385@qq.com']

    message = MIMEText(txt3, 'plain', 'utf-8')
    message['From'] = Header("杨晨", 'utf-8')
    message['To'] = Header("赵燕玲", 'utf-8')

    #主题
    subject = ti
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        # smtpObj.sendmail(sender, receivers2, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


import datetime
def gettime():
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)
    h=str(datetime.datetime.now().hour)
    mi=str(datetime.datetime.now().minute)
    s=str(datetime.datetime.now().second)
    print(m+"月"+d+"日"+h+"时"+mi+"分"+s+"秒")



import time
from time import sleep
# 3428573186
# 1493481385
# receivers1=['3459677992@qq.com','3428573186@qq.com']
receivers2=['3459677992@qq.com']
print("开始时间:")
gettime()
# getit("https://www.tianqi.com/dengzhou",receivers1)
# gettime()
getit("https://www.tianqi.com/minhang",receivers2)
gettime()
print("successful")
sleep(60*60*23)