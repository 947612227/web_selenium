#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-23 18:22:02
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os,sys ,logging
sys.path.append("../")
from Init.loginit import logs

def testa():
    log = logs()
    log.info("你好啊")
    log.debug("debug")
    log.error("error")

if __name__ == '__main__':
    testa()