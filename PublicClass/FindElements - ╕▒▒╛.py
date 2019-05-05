#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 13:11:40
# @Author  : zhangjia (947612227@163.com)
# @Link    : http://www.huaxialijian.com
# @Version : $Id$
# find_element
import os
from selenium.webdriver.support.wait import WebDriverWait #显示等待
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

class FindEleClass():
    """docstring for FindElement"""
    def __init__(self, driver):
        self.driver = driver

    def findElementFun(self,type,name,i=None):
        if type == 'id':
            ele = self.driver.find_element_by_id(name)
            return ele
        elif type == 'name':
            ele = self.driver.find_element_by_name(name)
            return ele
        elif type == 'classname':
            ele = self.driver.find_element_by_class_name(name)
            return ele
        elif type == 'xpath':
            ele = self.driver.find_element_by_xpath(name)
            return ele
        elif type == 'csss':
            ele = self.driver.find_elements_by_css_selector(name)[i]
            return ele
        elif type == 'ids':
            ele = self.driver.find_elements_by_id(name)[i]
            return ele
        else:
            print("参数错误！")

    def waits_unit(self,driver,i,type,name):
        """显示等待"""
        if type == 'id':
            try:
                wait = WebDriverWait(driver,i).until(lambda x: x.find_element_by_id(name))
            except TimeoutException as e:
                print(repr(e))
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


