from selenium import webdriver
import time

'''
1273036191@qq.com
'''
rightpass = 0
nopass = 0


def DLZC1():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    zh = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input')
    user = zh.get_attribute('placeholder')
    mm = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input')
    pwd = mm.get_attribute('placeholder')
    forget = wd.find_element_by_xpath('/html/body/div[2]/form/p/a')
    login = wd.find_element_by_xpath('/html/body/div[2]/form/button')
    reg = wd.find_element_by_xpath('/html/body/div[2]/p/a')
    if user == '邮箱/手机号码' and pwd == '密码' and forget.text == '忘记密码？' and login.text == '登录' and reg.text == '注册':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC2():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/p/a').click()
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC3():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('//html/body/div[2]/p/a').click()
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC4():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span')
    if msg.text == '帐号不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC5():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span')
    if msg.text == '密码不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC6():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span')
    if msg.text == '账号不存在':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC7():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('13199044512')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span')
    if msg.text == '密码错误':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC8():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('13199044512')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(0.5)
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCDataTransferStorePage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC9():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('test1@qq.com')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(0.5)
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCDataTransferStorePage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC10():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    mobile = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').get_attribute('placeholder')
    pwd = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').get_attribute('placeholder')
    acquire = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/input').get_attribute('placeholder')
    sent = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').text
    reg = wd.find_element_by_xpath('/html/body/div[2]/form/button').text
    out = wd.find_element_by_xpath('/html/body/div[2]/div[2]/div/a').text
    login = wd.find_element_by_xpath('/html/body/div[2]/div[2]/div/p[2]/a').text
    if mobile == '手机号码' and pwd == '密码' and acquire == '验证码' and sent == '发送验证码' and reg == '注册' and out == '海外用户注册' and login == '登录':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC11():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/div[2]/div/a').click()
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC12():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/div[2]/div/p[2]/a').click()
    if wd.current_url == 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC13():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '手机号不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC14():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '用户名不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC15():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '手机号码格式不正确':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC16():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('11111111111')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '验证码不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC17():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('13199044512')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '该手机号已经注册过帐号':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC18():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('11111111111')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/input').send_keys('123')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '密码不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC19():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('11111111111')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/input').send_keys('123')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '请先获取验证码':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC20():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('12344993321')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123456')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(0.5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送成功!':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC21():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('12344993321')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123456')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(0.5)
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '验证码错误':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC22():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('12344993321')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').send_keys('123456')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(60)
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送成功!':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC23():
    pass


def DLZC24():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    mobile = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').get_attribute('placeholder')
    pwd = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[2]/input').get_attribute('placeholder')
    acquire = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/input').get_attribute('placeholder')
    sent = wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').text
    submit = wd.find_element_by_xpath('/html/body/div[2]/form/button').text
    if mobile == '邮箱/手机号码' and pwd == '新密码' and acquire == '验证码' and sent == '发送验证码' and submit == '提交':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()
    wd.quit()


def DLZC25():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == 'Need Username parameter':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC26():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '用户名不能为空':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC27():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == 'Need code parameter':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC28():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('1')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '请输入正确的手机号或者邮箱':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC29():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('13199044512')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == 'Need code parameter':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC30():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('12345678933')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '该用户不存在':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC31():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('419@asd.com')
    wd.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(3)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '该用户不存在':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC32():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('test1@qq.com')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(10)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送成功!':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC33():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('13199044512')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送失败!':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC34():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('15198266364')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送成功！':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC35():
    opt = webdriver.ChromeOptions()
    opt.add_argument('headless')
    wd = webdriver.Chrome(r'D:\programming\programming_software\chromedriver\chromedriver.exe', options=opt)
    wd.implicitly_wait(10)
    wd.get('https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('15198266364')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(3)
    wd.refresh()
    time.sleep(3)
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[1]/input').send_keys('15198266364')
    wd.find_element_by_xpath('/html/body/div[2]/form/div[2]/div[3]/a').click()
    time.sleep(5)
    msg = wd.find_element_by_xpath('/html/body/div[2]/form/div[1]/span').text
    if msg == '发送验证码太快,请等待1分钟后,刷新页面重试.':
        global rightpass
        rightpass += 1
    else:
        global nopass
        nopass += 1
    wd.quit()


def DLZC36():
    pass


def DLZC37():
    pass


if __name__ == '__main__':
    DLZC1()
    DLZC2()
    DLZC3()
    DLZC4()
    DLZC5()
    DLZC6()
    DLZC7()
    DLZC8()
    DLZC9()
    DLZC10()
    DLZC11()
    DLZC12()
    DLZC13()
    DLZC14()
    DLZC15()
    DLZC16()
    DLZC17()
    DLZC18()
    DLZC19()
    DLZC20()
    DLZC21()
    DLZC22()
    DLZC23()
    DLZC24()
    DLZC25()
    DLZC26()
    DLZC27()
    DLZC28()
    DLZC29()
    DLZC30()
    DLZC31()
    DLZC32()
    DLZC33()
    DLZC34()
    DLZC35()
    DLZC36()
    DLZC37()
    print("通过了{}条用例".format(rightpass))
    print("{}条用例没有通过".format(nopass))
