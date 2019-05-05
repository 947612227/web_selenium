#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 10:28:54
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$
from selenium import webdriver
import re
driver = webdriver.Chrome()
driver.get("https://lol.qq.com/client/client_lcu.shtml#protocol=https:&port=54770")
page = driver.page_source
# print page
# "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
url_list = re.findall('href=\"(.*?)\"', page, re.S)
url_all = []
for url in url_list:
    if "https" in url:
        print (url)
        url_all.append(url)
# 最终的url集合
print (url_all)