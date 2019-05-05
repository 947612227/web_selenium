#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-18 23:09:51
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$


import os ,sys
sys.path.append('../')
from PublicClass.rang_ import rang_info

# rang = rang_info()
# pp = rang.range_("casepath")

rang = rang_info.range_("casepath")

print(rang)