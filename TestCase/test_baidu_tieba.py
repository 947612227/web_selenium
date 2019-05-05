#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-16 12:45:03
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# 登陆百度贴吧 一键签到

import os, sys, time, unittest ,logging
sys.path.append('../')
# import HTMLTestRunner
from selenium import webdriver
from PublicClass.FindElements import FindEleClass
from Init.webdriverInit import driverInit
from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.common.exceptions import *
from PublicClass.rang_ import rang_info
from Init.loginit import logs
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class baiDuTieBa(unittest.TestCase):
    """百度贴吧测试用例CLASS"""
    def __init__(self,methodName='test_baiDuTieba'):
        super(baiDuTieBa,self).__init__(methodName)
        #调用了/Init/webdriverInit.py初始化webdriver
        url = "http://www.baidu.com"
        self.driver = driverInit.driver_init(url,1)
        self.log = logs()

    def setUp(self):
        print("setup")
        # sysInfo = driverInit.get_sys_info()

        # try:
        #     assert "百度一下，你就知道" in self.driver.title
        # except Exception as e:
        #     print(e.message)

    def tearDown(self):
        self.driver.quit()

    def test_baiDuTieba(self):
        """贴吧登陆自动化用例"""
        # self.log = logs()
        self.log.info("++++++处理贴吧登陆用例开始++++++")
        uname = ""
        upass = ""
        fd = FindEleClass(self.driver)
        self.log.info("初始化find_element函数")
        #搜索百度贴吧
        search = fd.findElementFun("id","kw")
        search.click()
        keys = "百度贴吧"
        u = list(keys)
        for i in u:
            search.send_keys(i)
            time.sleep(0.2)
        time.sleep(1)

        #点击搜索
        btn1 = fd.findElementFun("id","su")
        btn1.click()
        time.sleep(1)
        #点击搜索结果
        opentb = fd.findElementFun("xpath","//*[@id='1']/h3/a[1]")
        opentb.click()
        time.sleep(1)
#点击搜索结果之后会打开新标签，这时候需要切换标签
        handles = self.driver.window_handles
        self.driver.switch_to_window(handles[-1])
        time.sleep(1)
        self.log.info("成功切换到新打开的标签句柄")


        #点击登陆
        login_btn = fd.findElementFun("xpath","//*[@id='com_userbar']/ul/li[4]/div/a")
        login_btn.click()
        time.sleep(1)


#点击用户名登陆方式
        user_login = fd.findElementFun("id","TANGRAM__PSP_10__footerULoginBtn")
        user_login.click()
        time.sleep(1)

        #定位用户名输入框
        user_input = fd.findElementFun("id","TANGRAM__PSP_10__userName")
        user_input.click()
        user_input.clear()

        username = list(uname)
        for j in username:
            user_input.send_keys(j)
            time.sleep(0.2)
        time.sleep(1)

        #定位密码输入框
        passwd_input = fd.findElementFun("id","TANGRAM__PSP_10__password")
        passwd_input.click()
        passwd_input.clear()

        passwd = list(upass)
        for a in passwd:
            passwd_input.send_keys(a)
            time.sleep(0.2)
        time.sleep(1)

        #定位登陆按钮
        login_btn1 = fd.findElementFun("id","TANGRAM__PSP_10__submit")
        login_btn1.click()
        time.sleep(3)
        self.log.info("登陆完成")

        #定位一键签到按钮xpath
        oneKeyBtn = fd.findElementFun("xpath","//*[@id='onekey_sign']/a")
        oneKeyBtn.click()
        time.sleep(1)
        self.log.info("点击完成")

        startBtn = fd.findElementFun("xpath","//*[@id='dialogJbody']/div/div/div[1]/a")
        startBtn.click()
        time.sleep(3)
        self.log.info("++++++执行完成，安全退出线程++++++")
#验证是否签到成功
        # try:
        #     fd.waits_unit(self.driver,5,"xpath","//*[@id='dialogJbody']/div/div/div[1]/span")
        #             except Exception as e:
        #     raise e



#//*[@id="dialogJbody"]/div/div/div[1]/p
##//*[@id="dialogJbody"]/div/div/div[1]/span
#if __name__ == '__main__':
#    unittest.main()
