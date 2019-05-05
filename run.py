#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-04 14:14:51
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# unittest 主程序

import unittest
import HTMLTestRunner
import os,sys,time
from PublicClass.rang_ import rang_info

sys.path.append('../testcase')
def createTests():
    suite = unittest.TestSuite()
    testpath = rang_info.range_("casepath")
    testdir = unittest.defaultTestLoader.discover(
        testpath, pattern='test_*.py')

    for TestSuite in testdir:
        for testcase in TestSuite:
            suite.addTest(testcase)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #定义报告存放的路径，支持相对路径
    file_path = rang_info.range_("reportpath")
    file_result= open(file_path, 'wb')

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = u"测试报告",tester = "QA")
#description = u"描述信息：百度登陆自动化测试报告由'QA'独立编写，本用例包括，登陆，输入",
#    runner = HTMLTestRunner.HTMLTestRunner(stream = file_result, title = self.title, description = self.description)
    runner.run(createTests())
    file_result.close()

