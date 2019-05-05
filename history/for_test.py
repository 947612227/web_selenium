#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 16:22:54
# @Author  : zhangjia (947612227@163.com)
# @Link    : http://www.huaxialijian.com
# @Version : $Id$

import os
import sys
def sort_by_value(dic):
    for key,value in sorted(dic.items(),key=lambda x:x[1]):
#        print(key,value)
        print(value)
# print (sys.version)
arr1 = {'username':'0000',
        'password':'1111',
        'bankcard':'2222',
        'idcard':'3333',
        'bankphone':'4444'}
sort_by_value(arr1)
# list = ['1','2','3','0','4']
# for i in list:
#     print(i)
arr1.items()