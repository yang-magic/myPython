from twilio.rest import Client
import os
import xlwt
import requests
from lxml import etree
import time
from time import sleep
from translate import Translator

def getit():
    #初始化打开
    translator= Translator(from_lang="chinese",to_lang="english")
    txt=open('log.txt','w',encoding='utf-8' )

    #获取html
    url="https://www.tianqi.com/dengzhou"
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
    r=requests.get(url,headers=header)
    r.encoding="utf-8"
    r=r.text
    r=etree.HTML(r)

    #日期
    date=r.xpath("//dd[@class='week']/text()")
    print(date[0])
    time.localtime(time.time())
    thedate=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    txt.write(thedate+'\n')

    #当前温度
    a=r.xpath("//dd[@class='weather']/p/b/text()")
    print('now:'+a[0]+'℃')
    txt.write("Current temperature:"+a[0]+'\n')

    # 整体情况
    b=r.xpath("//dd[@class='weather']/span/b/text()")
    print("tody:"+b[0])
    translation = translator.translate(b[0])
    txt.write('tody:'+translation+'\n')
    rain='雨' in b[0]
    if rain:
        print("今天可能有雨，注意带伞！！！")
        translation = translator.translate("今天可能有雨，注意带伞！！！")
        txt.write(translation)

    #低高温度
    c=r.xpath("//dd[@class='weather']/span/text()")
    print("temperature:"+c[0])
    txt.write("temperature:"+c[0]+'\n')

    #空气质量
    d=r.xpath("//dd[@class='kongqi']/h5/text()")
    print(d[0])
    translation = translator.translate(d[0])
    txt.write(translation+'\n')
    d=r.xpath("//dd[@class='kongqi']/h6/text()")
    print(d[0])
    translation = translator.translate(d[0])
    txt.write(translation+'\n')

    #紫外线
    e=r.xpath("//dd[@class='shidu']/b[1]/text()")
    print(e[0])
    translation = translator.translate(e[0])
    txt.write(translation+'\n')
    e=r.xpath("//dd[@class='shidu']/b[3]/text()")
    print(e[0])
    translation = translator.translate(e[0])
    txt.write(translation+'\n')

    #日出日落
    f=r.xpath("//dd[@class='kongqi']/span/text()")
    print(f[0]+f[1])
    translation = translator.translate(f[0])
    txt.write(translation+'\n')
    translation = translator.translate(f[1])
    txt.write(translation+'\n')

    #保存
    txt.close()

    #读取txt
    txt2=open('log.txt','r',encoding='utf-8' )
    txt3=txt2.read()
    print(txt3)
    print(type(txt3))

    #发送
    #zhao+8615515748537
    # Your Account SID from twilio.com/console
    account_sid = "AC954635e759ba9decdebb1d71944fd697"
    # Your Auth Token from twilio.com/console
    auth_token  = "4fc11a553f8190c121b4b4c6ccf371cf"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        # 这里中国的号码前面需要加86
        to="+8619821279929",
        from_="+15868008474",
        body=txt3)
    print(message.sid)

#"+8615515748537" zhao
while 1:
    getit()
    sleep(60*60*24)
print("successful")