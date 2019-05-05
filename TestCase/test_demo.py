#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-28 14:26:04
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.maximize_window()

