#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 11:14:55
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os

def adds(a,b):
    try:
        if a==0:
            res = b/a
    except ZeroDivisionError as e:
        print("被除数不能为0\n%s" % e)

adds(0,1)