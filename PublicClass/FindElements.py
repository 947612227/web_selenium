#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 13:11:40
# @Author  : zhangjia (947612227@163.com)
# @Link    : http://www.huaxialijian.com
# @Version : $Id$
# find_element
import os,sys,time
sys.path.append("../")
from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from Init.loginit import logs


class FindEleClass():
    """docstring for FindElement"""
    def __init__(self, driver):
        self.driver = driver
        self.log = logs()
        self.log.info("初始化定位函数")
    def findElementFun(self,type=None,name=None,i=None):
        """定位函数
        type:id,name,css,xpath
        name:定位元素
        i:elements相关
        """
        ele=None
        if type == 'id':
            try:
                self.driver.find_element_by_id(name).is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_element_by_id(name)
            return ele
        elif type == 'name':
            try:
                self.driver.find_element_by_name(name).is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_element_by_name(name)
            return ele
        elif type == 'classname':
            try:
                self.driver.find_element_by_class_name(name).is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_element_by_class_name(name)
            return ele
        elif type == 'xpath':
            try:
                self.driver.find_element_by_xpath(name).is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_element_by_xpath(name)
            return ele
        elif type == 'csss':
            try:
                self.driver.find_elements_by_css_selector(name)[i].is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_elements_by_css_selector(name)[i]
            return ele
        elif type == 'ids':
            try:
                self.driver.find_elements_by_id(name)[i].is_displayed()
            except Exception as e:
                self.log.info("元素不存在：" + name)
            else:
                self.log.info("发现元素：" + name)
                ele = self.driver.find_elements_by_id(name)[i]
            return ele
        else:
            self.log.info("定位参数错误！")

    def waits_unit(self,driver,i,type,name):
        """显示等待"""
        if type == 'id':
            try:
                wait = WebDriverWait(driver,i).until(lambda x: x.find_element_by_id(name))
            except TimeoutException as e:
                self.log.info("元素不存在：" + name)
            else:
                driver.execute_script("arguments[0].scrollIntoView();", wait)
                return wait

        elif type == 'name':
            try:
                wait = WebDriverWait(driver,i).until(lambda x: x.find_element_by_name(name))
            except TimeoutException as e:
                print(repr(e))
            else:
                driver.execute_script("arguments[0].scrollIntoView();", wait)
                return wait

        elif type == 'css':
            try:
                wait = WebDriverWait(driver,i).until(lambda x: x.find_element_by_css(name))
            except TimeoutException as e:
                print(repr(e))
            else:
                driver.execute_script("arguments[0].scrollIntoView();", wait)
                return wait

        elif type == 'xpath':
            try:
                wait = WebDriverWait(driver,i).until(lambda x: x.find_element_by_xpath(name))
            except TimeoutException as e:
                print(repr(e))
            else:
                driver.execute_script("arguments[0].scrollIntoView();", wait)
                return wait
        else:
            print("参数错误")

        # try:
        #     pass
        # except Exception as e:
        #     raise e


