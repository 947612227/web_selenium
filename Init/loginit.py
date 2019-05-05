#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-23 18:04:22
# @Author  : 张先生 (947612227@qq.com)
# @Link    : http://www.huaxialijian.com/
# @Version : 日志初始化模块

import os , time , sys , logging , logging.handlers
sys.path.append('../')
from PublicClass.rang_ import rang_info

class logs():
    """自定义日志"""
    def __init__(self,logger=None):
        self.logger = logging.getLogger(rang_info.range_("user",6))
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        logfilepath = rang_info.range_("logpath")
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename =logfilepath,
                                                                   maxBytes = 1024 * 1024 * 50,
                                                                   backupCount = 5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s %(filename)s %(funcName)s line:%(lineno)d %(levelname)s:] [%(message)s]')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(console)
        self.logger.setLevel(logging.INFO)


    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)