#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-18 22:10:44
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : $Id$

import os
import random
import time

class rang_info(object):
    """生成一些配置文件路径"""
    def __init__(self):
        pass

    def range_(typename,i=None):
        """user:随机用户名
           password:随机密码
           logpath:返回日志路径+文件名
           image:截图路径+文件名
           reportpath：测试报告+文件名
           checkpath：验证码图片+文件名
           casepath:测试用例路径
        """
        datetime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        dates = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        days = time.strftime("%Y-%m-%d",time.localtime())
        rootpath = "/root/selenium/web_selenium/"

        if typename == "user":
            user_info = "".join(random.sample("1234567890abcdefghigklmnopqrstuvwxyz_", i))
            return user_info

        elif typename == "password":
            pass_info = "".join(random.sample("1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ_", i))
            return pass_info

        elif typename == "logpath":
            path = rootpath + "Log/log_" + days + ".log"
            return path

        elif typename == "image":
            image = rootpath + "image/scr_" + datetime + ".jpg"
            return image

   #     elif typename == "reportpath":
   #         reportpath = rootpath + "ReportHtml/" + datetime + ".html"
   #         return reportpath
        elif typename == "reportpath":
            reportpath = "/home/wwwroot/default/report/" + dates + ".html"
            return reportpath

        elif typename == "checkpath":
            path = rootpath + "checkpath/" + datetime + ".html"
            return path

        elif typename == "casepath":
            casepath = rootpath + "TestCase/"
            return casepath
        else:
            print("参数错误！")


#if __name__ == "__main__":
#    rang = rang_info.range_("reportpath")
#    print (rang)
