"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/18 11:12
@Author : mayonglin
@File : logs.py
@Software: PyCharm
功能描述：定义公共的日志输出模块，以便其他模块调试使用
实现逻辑：
    1-导包
    2-basicconfig定制日志参数
    3-获取日志记录器，并返回
"""
"""
步骤分析:
1.配置日志记录器名称
2.配置日志级别
3.配置日志格式(可以分别配置,也可以统一配置)
4.创建并添加handler-控制台
5.创建并添加handler-文件
6.对外提供日志记录器
"""
import logging
import os
#获取日志目录
log_path = os.path.dirname(os.path.dirname(__file__)) + r"/testLog/"

def log():
    #1.配置日志记录器名称
    logger = logging.getLogger("Test")
    #2.配置日志级别
    logger.setLevel(logging.DEBUG)
    #3.配置日志格式(可以分别配置,也可以统一配置)
    format = logging.Formatter("日志：%(name)s-级别：%(levelname)s-时间：%(asctime)s-模块：%(module)s.py-第%(lineno)d行:%(message)s")
    #4.创建并添加handler-控制台
    sh = logging.StreamHandler()
    sh.setFormatter(format)
    logger.addHandler(sh)
    #5.创建并添加handler-文件
    fh = logging.FileHandler(log_path + r"test.txt", encoding="utf-8")
    fh.setFormatter(format)
    logger.addHandler(fh)

    #6.对外提供日志记录器
    return logger

#单例模式
logger = log()
