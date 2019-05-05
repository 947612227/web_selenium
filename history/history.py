#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-11 19:31:14
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : history code+++++++++++++++++++++++++++++

#WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
#WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH,'#//*[@id='u1']/a[7]')))

def test_init(i,http_url):
    try:
        if i == 1:
            init = webdriver.Chrome()
#            print("操作系统：%s" %(platform.platform()))
            print("当前浏览器：%s" % (init.capabilities['browserName']))
            print("浏览器版本：%s" % (init.capabilities['version']))
            print("驱动版本号：%s" % (init.capabilities['chrome']['chromedriverVersion']))
            init.get(http_url)
            if init.title != "百度一下，你就知道":
                print("错误信息#########\n当前标题 %s" %(init.title))
                print("当前链接：%s" %(init.current_url))
                sys.exit()
            return init
        elif i == 2:
            init = webdriver.Ie()
            init.get(http_url)
            return init
        else:
            print("参数错误！")
    except Exception as e:
        print(e)

# #显性等待
def waits(driver,times,type,key):
    try:
        if type == 'id':
            ts = WebDriverWait(driver, times).until(EC.presence_of_element_located((By.ID, key)))
            return ts
        elif type == 'name':
            ts = WebDriverWait(driver, times).until(EC.presence_of_element_located((By.NAME, key)))
            return ts
        elif type == 'xpath':
            ts = WebDriverWait(driver, times).until(EC.presence_of_element_located((By.XPATH, key)))
            return ts
        else:
            print("type或者key 参数错误")
    except TimeoutException:
        print("超时错误：显示等待页面元素超时")
    except NoSuchElementException:
        print("定位错误：寻找页面元素不存在",traceback.print_exc())
    except Exception:
        print(traceback.print_exc())

'''
find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
'''

#    time.sleep(1)

#    waits(driver,3,"id","TANGRAM__PSP_10__footerULoginBtn")
    fd.findElementFun("id","TANGRAM__PSP_10__footerULoginBtn").click()
    time.sleep(1)

    fd.findElementFun("name","userName").send_keys(username)
    time.sleep(1)

    fd.findElementFun("name","password").send_keys(password)
    time.sleep(1)

    fd.findElementFun("id","TANGRAM__PSP_10__submit").click()
    time.sleep(2)

#验证方式
    fd.findElementFun("id","TANGRAM__39__content_select_show").click()
    time.sleep(1)

#选择银行卡验证
    fd.findElementFun("id","TANGRAM__39__select_bank").click()
    time.sleep(1)
#卡号
    fd.findElementFun("id","TANGRAM__39__input_card").send_keys(bancard)
    time.sleep(1)
#身份证
    fd.findElementFun("id","TANGRAM__39__input_idcard").send_keys(idcard)
    time.sleep(1)
#手机号
    fd.findElementFun("id","TANGRAM__39__input_bankphone").send_keys(phone)
    time.sleep(1)

#提交
    fd.findElementFun("id","TANGRAM__39__submit_bank").click()
    time.sleep(1)
    driver.close()

#点击首页登陆按钮
    fd.findElementFun("xpath","//*[@id='u1']/a[7]").click()
    time.sleep(1)

#点击用户名登陆
    fd.findElementFun("id","TANGRAM__PSP_10__footerULoginBtn").click()
    time.sleep(1)

#点击用户名输入框，清空内容
    user = fd.findElementFun("id","TANGRAM__PSP_10__userName")
    user.click()
    user.clear()
    user_str = ['9','4','7','6','1','2','2','2','7']
    for i in user_str:
        user.send_keys(i)
        time.sleep(0.2)

    password = fd.findElementFun("id","TANGRAM__PSP_10__password")
    password.click()
    password.clear()
    pass_str = ['z','h','a','n','g','J','I','A','0','.','.']
    for j in pass_str:
        password.send_keys(j)
        time.sleep(0.2)

    fd.findElementFun("id","TANGRAM__PSP_10__submit").click()
    time.sleep(5)