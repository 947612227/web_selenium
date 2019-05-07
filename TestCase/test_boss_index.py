#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-26 12:10:35
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @boss直聘
# url:https://www.zhipin.com/



import os ,sys ,time
sys.path.append("../")
import unittest
from selenium import webdriver
from PublicClass.FindElements import FindEleClass
from Init.webdriverInit import driverInit

class BossZhiPin(unittest.TestCase):
    """Boss直聘"""
    def setUp(self):
        url = "https://www.zhipin.com/"
        self.driver = driverInit().driver_init(url,1)
        self.log = logs()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    # def test_login_Boss(self):
    #     fd = FindEleClass(self.driver)
    #     login_btn = fd.findElementFun("xpath","//*[@class='btns']/a[5]")
    #     login_btn.click()
    #     time.sleep(3)

    def test_search_job(self):
        """boss直聘"""
        fd = FindEleClass(self.driver)
        search_edit = fd.findElementFun("name","query")
        search_edit.click()
        search_edit.send_keys("软件测试工程师")
        time.sleep(1)

        search_btn = fd.findElementFun("xpath","//*[@class='search-form ']/form/button")
        search_btn.click()
        time.sleep(1)

        #选择热门城市-北京
        chose_bj_btn = fd.findElementFun("xpath","//*[@class='condition-box']/dl[1]/dd/a[4]")
        chose_bj_btn.click()
        time.sleep(1)

        #工作经验（时间）
        work_exp = fd.findElementFun("xpath","//*[@class='ipt']")
        work_exp.click()
        time.sleep(1)

        #选择3-5年工作经验
        chose_years = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[1]//ul[1]/li[5]/a")
        chose_years.click()
        time.sleep(1)

        #学历要求按钮
        #"//*[@id='filter-box']/div/div[4]/div[2]/span/input"
        chose_edu = fd.findElementFun("xpath","//*[@id='filter-box']/div/div[4]/div[2]/span/input")
        chose_edu.click()
        time.sleep(1)

        #选择大专学历
        chose_dazhuan = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[2]/span[1]/div[1]/ul[1]/li[5]/a")
        chose_dazhuan.click()
        time.sleep(1)

        #选择薪资
        chose_salary = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[3]//input")
        chose_salary.click()
        time.sleep(0.5)

        #选择10-15k
        chose_ten = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[3]/span[1]/div[1]/ul/li[5]/a")
        chose_ten.click()
        time.sleep(3)

        
        rz = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[4]/span/input[1]")
        time.sleep(0.5)
        rz.click()
        time.sleep(1)

        #融资阶段选择不限
        rzr = fd.findElementFun("xpath","//*[@id='filter-box']/div/div[4]/div[4]/span/div/ul/li[1]/a")
        time.sleep(0.5)
        rzr.click()
        time.sleep(1)
    
        #公司规模也选择不限吧
        comp = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[5]/span[1]/input[1]")
        time.sleep(0.5)
        comp.click()
        time.sleep(1)

        compa = fd.findElementFun("xpath","//*[@class='filter-select-box']/div[5]/span[1]/div[1]/ul[1]/li[1]/a")
        time.sleep(0.5)
        compa.click()
        time.sleep(1)

        #元素定位暂时就写那么多












    def test_error1(self):
        """这是一个错误，以防全部通过没绩效"""
        print(1/0)
# if __name__ == '__main__':
#     unittest.main()
