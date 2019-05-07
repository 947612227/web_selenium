#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 12:57:53
# @Author  : zhangjia (947612227@163.com)
# @Link    : http://www.huaxialijian.com
# @Version : $Id$
# WEB自动化测试:加上

# from 包名.文件名 import 类名
import sys, time,unittest
sys.path.append('../')
import HTMLTestRunner
from selenium import webdriver
from PublicClass.FindElements import FindEleClass
from Init.webdriverInit import driverInit
from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from PublicClass.rang_ import rang_info
from Init.loginit import logs



class Baidu(unittest.TestCase):
    def setUp(self):
        self
        url = "http://www.baidu.com"
        self.driver = driverInit().driver_init(url,1)
        self.log = logs()
        time.sleep(3)
        #调用了/Init/webdriverInit.py初始化webdriver

    def tearDown(self):
        self.log.info("执行完成退出[tearDown]")
        self.driver.quit()


    def test_1(self):
        self.log.info("这是index的test1")

    def test_baidu(self):
        """百度登陆测试"""
    #百度用户名密码
        self.log.info("执行test_baidu测试用例")
        uname = ""
        psswd = ""
        fd = FindEleClass(self.driver)
        self.log.info("初始化Element")
    #点首页登陆按钮
        login = fd.findElementFun("csss","div[id=u1] a[class=lb]",0)
        self.log.info("首页登陆按钮定位成功")
        login.click()
        self.log.info("首页登陆按钮点击成功")
        time.sleep(2)

    #点用户名登陆
        userlg = fd.findElementFun("csss","p.tang-pass-footerBarULogin",0)
        self.log.info("定位用户名登陆按钮成功")
        userlg.click()
        self.log.info("点击用户名登陆成功")
        time.sleep(1)

    #定位用户名输入框
        username = fd.findElementFun("ids",'TANGRAM__PSP_10__userName',0)
        self.log.info("定位用户名输入框成功")
        username.click()
        self.log.info("点击用户名输入框成功")

        user_str = list(uname)
        for i in user_str:
            username.send_keys(i)
            time.sleep(0.2)

        self.log.info("输入用户名:" + uname + "完成")
        time.sleep(1)

    #定位密码输入框
        password = fd.findElementFun("ids",'TANGRAM__PSP_10__password',0)
        self.log.info("定位密码输入框成功")
        password.click()
        self.log.info("点击密码输入框成功")
        password.clear()
        self.log.info("清空密码输入框成功")
        pass_str = list(psswd)
        for j in pass_str:
            password.send_keys(j)
            time.sleep(0.2)

        self.log.info("输入密码：" + psswd + "完成")
        time.sleep(1)
    #点击登陆按钮
        username = fd.findElementFun("ids",'TANGRAM__PSP_10__submit',0)
        self.log.info("定位登陆按钮成功")
        username.click()
        self.log.info("点击登陆按钮成功")
    #模拟点击登陆按钮
        #username.send_keys(Keys.RETURN)

        endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log.info("结束时间: %s" % (endTime))
        self.log.info("百度登陆用例执行完成")
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()