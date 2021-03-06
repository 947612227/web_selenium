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
    def setUp(self):
        url = "http://www.baidu.com"
        self.driver = driverInit().driver_init(url,1)
        self.log = logs()

    def tearDown(self):
        self.log.info("++++++执行完成，安全退出线程++++++")
        self.driver.quit()

    def test_baiDuTieba(self):
        """贴吧登陆自动化用例"""
        # self.log = logs()
        self.log.info("++++++处理贴吧登陆用例开始++++++")
        uname = "candy霞姐"
        upass = "yixia1112"
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
        time.sleep(3)
        login_btn.click()
        time.sleep(1)
        self.log.info("点击登陆按钮完成")

#点击用户名登陆方式
        user_login = fd.findElementFun("id","TANGRAM__PSP_10__footerULoginBtn")
        user_login.click()
        time.sleep(1)
        self.log.info("点击用户名登陆方式")

        #定位用户名输入框
        user_input = fd.findElementFun("id","TANGRAM__PSP_10__userName")
        user_input.click()
        user_input.clear()
        self.log.info("用户名输入框定位完成")

        username = list(uname)
        for j in username:
            user_input.send_keys(j)
            time.sleep(0.2)
        time.sleep(1)
        self.log.info("用户名输入完成")
        utext = user_input.get_attribute('value')
        self.log.info("输入的用户名为:%s" %(utext))

        #定位密码输入框
        passwd_input = fd.findElementFun("id","TANGRAM__PSP_10__password")
        passwd_input.click()
        passwd_input.clear()
        self.log.info("密码输入框定位完成")

        passwd = list(upass)
        for a in passwd:
            passwd_input.send_keys(a)
            time.sleep(0.2)
        time.sleep(1)
        self.log.info("密码输入完成")
        ptext = passwd_input.get_attribute('value')
        self.log.info("输入的密码为:%s" %(ptext))

        #定位登陆按钮
        login_btn1 = fd.findElementFun("id","TANGRAM__PSP_10__submit")
        login_btn1.click()
        time.sleep(3)
        self.log.info("点击登陆按钮，登陆完成")


        #定位一键签到按钮xpath
        oneKeyBtn = fd.findElementFun("xpath","//*[@class='onekey_btn']")
        oneKeyBtn.click()
        time.sleep(2)
        self.log.info("点击一键签到")



        # startBtn = fd.findElementFun("xpath","//*[@id='dialogJbody']/div/div/div[1]/a")
        # startBtn.click()
        # time.sleep(3)
        # self.log.info("点击签到完成")
#验证是否签到成功
        try:
            check_out = fd.findElementFun("xpath","//*[@class='sign_btn sign_suc_nonmember']")
        except Exception as e:
            print("签到失败%s" % e)
        else:
            self.log.info("签到完成")
            print("签到完成")
