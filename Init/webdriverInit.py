#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019年4月11日 19:08:44
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/

import os
import platform
import sys
import socket
import time
sys.path.append('../')
from selenium import webdriver
from Init.loginit import logs

class driverInit():
    """Webdriver初始化类"""
    def __init__(self):
        """初始化Webdriver一些配置"""
        self.log = logs()

    def driver_init(self,http_url,i):
        """
        传入URL和浏览器类型，返回driver.get()
        主函数初始化完成请设置延迟
        url:测试地址
        1:谷歌
        2:IE
        其他：暂无
        """
        try:
            if i == 1:
                chrome_opt = webdriver.ChromeOptions()
                chrome_opt.add_argument("--headless")
                chrome_opt.add_argument("--no-sandbox") #这句一定要有"")"")
                #init = webdriver.Chrome()
                init = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_opt)
                self.log.info("谷歌浏览器初始化完成:%s" %(init))
                init.get(http_url)
                self.log.info("测试URL："+ http_url)
                init.maximize_window()
                self.log.info("设置窗口最大化")
                return init
            elif i == 2:
                init = webdriver.Ie()
                init.get(http_url)
                init.maximize_window()
                return init
            else:
                print("driver初始化参数错误")

        except Exception as e:
            print(e)

    def get_sys_info(self):
        '''获取操作系统信息'''
        print("get")


# if __name__ == '__main__':
#     bd_url = "https://zhidao.baidu.com/question/68795962.html"
#     inits = driverInit()
#     driver = inits.driver_init(bd_url,1)
#     driver.find_element_by_xpath("//*[@id='answer-bar']").click()
#     time.sleep(5)
