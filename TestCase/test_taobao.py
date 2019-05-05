#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-11 18:28:31
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @淘宝自动化,cookies
import os, sys, platform ,time, socket, unittest
sys.path.append('../')
import HTMLTestRunner
from selenium import webdriver
from PublicClass.FindElements import FindEleClass
from Init.webdriverInit import driverInit
from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class testTaoBao(unittest.TestCase):
    """淘宝首页"""
    def setUp(self):
        sysInfo = driverInit.get_sys_info()
        url = "http://www.taobao.com"
        #调用了/Init/webdriverInit.py初始化webdriver
        self.driver = driverInit.driver_init(1,url)
        self.driver.maximize_window()
#        try:
#            assert "百度一下，你就知道" in self.driver.title
#        except Exception as e:
#            print(e.message)

    def tearDown(self):
        self.driver.quit()

    def test_tb(self):
        fd = FindEleClass(self.driver)
    #验证首页是否打开
        fd.waits_unit(driver,3,"xpath","/html/body/div[2]/div/div/div[1]/div/h1/a")

    #点击首页导航登陆按钮
        fd.findElementFun("xpath","//*[@id='J_SiteNavLogin']/div[1]/div[1]/a[1]").click()
        time.sleep(2)

    #点击登陆界面的密码登陆
        fd.findElementFun("xpath","//*[@id='J_QRCodeLogin']/div[5]/a[1]").click()
        time.sleep(2)

    #定位用户名输入框
        phone = ""
        password = ""
        username = fd.findElementFun("xpath","//*[@id='TPL_username_1']")
        user_str = list(phone)
        for i in user_str:
            username.send_keys(i)
            time.sleep(0.2)
        time.sleep(1)

    #插入JS，跳过滑动验证码

    #定位密码输入框
        password = fd.findElementFun("xpath","//*[@id='TPL_password_1']")
        pass_str = list(password)
        for j in pass_str:
            password.send_keys(j)
            time.sleep(0.2)

        time.sleep(1)




    #点击登陆按钮
        login_btn = fd.findElementFun("xpath","//*[@id='J_SubmitStatic']")
        login_btn.click()

        time.sleep(3)

    #跳转到淘宝首页
        ahref = fd.findElementFun("xpath","//*[@id='J_SiteNavHome']/div/a/span")
        ahref.click()
        time.sleep(2)

    #点击淘宝网首页的搜索框
        search_input = fd.findElementFun("id","q")
        search_input.click()
        search_input.clear()
        search_input.send_keys("DDR4 2133 8G 金士顿")
        time.sleep(30)
        driver.quit()

        endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("结束时间: %s" % (endTime))

