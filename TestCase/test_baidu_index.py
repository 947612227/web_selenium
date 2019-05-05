#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 12:57:53
# @Author  : zhangjia (947612227@163.com)
# @Link    : http://www.huaxialijian.com
# @Version : $Id$
# WEB自动化测试:加上

# from 包名.文件名 import 类名
import os, sys, platform ,time, socket, unittest ,logging
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



class Baidu(unittest.TestCase):
    def setUp(self):
        self.logging = logging
        fmt = '[%(asctime)s %(filename)s %(funcName)s line:%(lineno)d %(levelname)s:] [%(message)s]'
        log_path = rang_info.range_("log_path")
        logging.basicConfig(filename=log_path, level=logging.DEBUG, format=fmt)
        # self.logging.info("这是info信息")
        # self.logging.debug("这是debug信息")
        # self.logging.warning("这是waring信息")
        # self.logging.error("这是error信息")


        sysInfo = driverInit.get_sys_info()

        url = "http://www.baidu.com"
        #调用了/Init/webdriverInit.py初始化webdriver
        self.driver = driverInit.driver_init(1,url)
        try:
            assert "百度一下，你就知道" in self.driver.title
            self.logging.info("浏览器初始化完成")
        except Exception as e:
            self.logging.info("浏览器初始化失败：\n" + e.message)
            self.driver.quit()



    def tearDown(self):
        self.driver.quit()
        self.logging.info("执行完成退出[tearDown]")

    def test_1(self):
        self.logging.info("这是index的test1")

    def test_baidu(self):
        """百度登陆测试"""
    #百度用户名密码
        self.logging.info("执行test_baidu测试用例")
        uname = ""
        psswd = ""
        fd = FindEleClass(self.driver)
        self.logging.info("初始化Element")
    #点首页登陆按钮
        login = fd.findElementFun("csss","div[id=u1] a[class=lb]",0)
        self.logging.info("首页登陆按钮定位成功")
        login.click()
        self.logging.info("首页登陆按钮点击成功")
        time.sleep(2)

    #点用户名登陆
        userlg = fd.findElementFun("csss","p.tang-pass-footerBarULogin",0)
        self.logging.info("定位用户名登陆按钮成功")
        userlg.click()
        self.logging.info("点击用户名登陆成功")
        time.sleep(1)

    #定位用户名输入框
        username = fd.findElementFun("ids",'TANGRAM__PSP_10__userName',0)
        self.logging.info("定位用户名输入框成功")
        username.click()
        self.logging.info("点击用户名输入框成功")

        user_str = list(uname)
        for i in user_str:
            username.send_keys(i)
            time.sleep(0.2)

        self.logging.info("输入用户名:" + uname + "完成")
        time.sleep(1)

    #定位密码输入框
        password = fd.findElementFun("ids",'TANGRAM__PSP_10__password',0)
        self.logging.info("定位密码输入框成功")
        password.click()
        self.logging.info("点击密码输入框成功")
        password.clear()
        self.logging.info("清空密码输入框成功")
        pass_str = list(psswd)
        for j in pass_str:
            password.send_keys(j)
            time.sleep(0.2)

        self.logging.info("输入密码：" + psswd + "完成")
        time.sleep(1)
    #点击登陆按钮
        username = fd.findElementFun("ids",'TANGRAM__PSP_10__submit',0)
        self.logging.info("定位登陆按钮成功")
        username.click()
        self.logging.info("点击登陆按钮成功")
    #模拟点击登陆按钮
        #username.send_keys(Keys.RETURN)

        endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.logging.info("结束时间: %s" % (endTime))
        self.logging.info("百度登陆用例执行完成")
        time.sleep(3)


