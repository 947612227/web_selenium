#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-13 12:04:55
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os

class execute_script(object):
    """docstring for execute_script"""
    def __init__(self, arg):
        super(execute_script, self).__init__()


    def execute_script(self,jstype):
        if jstype == 'up':
            #火狐
            #js="var q=document.getElementById('id').scrollTop=0"
            js = "var q=document.body.scrollTop=0"
            return js
        elif jstype == 'down':
            js="var q=document.documentElement.scrollTop=10000"
            return js
        elif jstype == 'left':
            js = "window.scrollTo(100,400);"
        elif jstype == 'right':
            pass
        else:
            print("参数不存在")