from selenium import webdriver
import time

def doit(sid,pwd):
    wb = webdriver.Chrome(r'/usr/lib/chromium-browser/chromedriver')
    wb.get('https://cas.sues.edu.cn/cas/login')
    wb.find_element_by_id('username').send_keys(sid)
    wb.find_element_by_id('password').send_keys(pwd)
    wb.find_element_by_id('passbutton').click()
    wb.get('https://workflow.sues.edu.cn/default/work/shgcd/jkxxcj/jkxxcj.jsp')
    a = wb.find_elements_by_class_name('form-control')
    a[13].send_keys('36')
    wb.find_element_by_id('post').click()
    # wb.find_element_by_class_name('layui-layer-btn0').click()
    wb.quit()
    print(sid+' is ok')
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

while(True):
    #time.sleep(2*60*60+10*60)
    print('start')
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    yang = ['051718112','YANGchen906008']
    huang = ['051718102','220035']
    huo = ['051718111','MArs712384692..']
    meng = ['101116317','Mjw19970110']
    doit(yang[0],yang[1])
    doit(huang[0],huang[1])
    doit(huo[0],huo[1])
    doit(meng[0],meng[1])
    time.sleep(12*60*60-20)
