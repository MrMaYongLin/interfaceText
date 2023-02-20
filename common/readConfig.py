"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/17 14:11
@Author : mayonglin
@File : configHttp.py
@Software: PyCharm
功能描述：读取config.ini文件，获取目标的参数值，供其他模块使用
实现逻辑：
    1-导包configparser
    2-准备目标文件
    3-创建对象，调用read方法读取
    4-对外提供获取xxsection下的键值对的方法
"""
import configparser
import os
from common.logs import logger

class ReadConfig():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.file = os.path.dirname(os.path.dirname(__file__)) + r'/config.ini'
        self.conf.read(self.file, encoding='utf-8-sig')
        logger.info(f'config.ini文件的路径是:{self.file}')
    def get_data(self, section):
        try:
            result = self.conf.items('mysql')
            logger.info(result)
        except Exception as msg:
            logger.error(f'系统错误，提示：{msg}')
    def get_value(self, section, option):
        try:
            result = self.conf.get(section, option)
            logger.info(result)
        except Exception as msg:
            logger.error(f'系统错误，提示：{msg}')

if __name__ == '__main__':
    rc = ReadConfig()
    rc.get_data('mysql')
    rc.get_value('mysql', 'user')