#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-23 14:48:13
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os
import json
import time

def test_post():
    #url = ""
    #headers = ""
    tm = int(time.time())
    fileopen = open("json//register.json","rb")
    datas = json.load(fileopen)
    for data in datas:
        data["tm"] = tm
        data1 = sorted(data.items())