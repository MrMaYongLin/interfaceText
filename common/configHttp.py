"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/17 14:11
@Author : mayonglin
@File : configHttp.py
@Software: PyCharm
功能描述：接收TestCase传入的接口请求测试数据，根据具体的请求逻辑完成接口测试，并将结果返回给TestCase
实现逻辑：
    1-接收TestCase传入的数据
    2、提取测试数据内的method方法
    3、根据method方法进行判断
        3-1 如果是get方法就调用get方法
        3-2 如果是post方法就调用post方法
    4、从接口请求的结果中，提取需要断言的字段errorCode
    5、将实际提取的errorCode与Excel中的预期值进行对比
        5-1 相同即通过 success
        5-2 不同即失败 fail
"""
import requests
from common.logs import logger
class ConfigHttp():
    def __init__(self, url, value, method):
        self.url = url
        self.value = value
        self.method = method
        self.header = {}
        logger.info('这是输出日志')
    def run(self):
        """
        3、根据method方法进行判断
        3-1 如果是get方法就调用get方法
        3-2 如果是post方法就调用post方法
        """
        try:
            if self.method.lower() == 'get':
                return self.__get()
            elif self.method.lower() == 'post':
                return self.__post()
            elif self.method.lower() == 'put':
                return self.__put()
        except Exception as msg:
            print('System error: ', msg)
    def __get(self):
        result = requests.get(url=self.url, params=eval(self.value), headers=self.header)
        realErrorCode = result.json()['errorCode']
        statusCode = result.status_code
        return statusCode, realErrorCode
    def __post(self):
        result = requests.post(url=self.url, data=eval(self.value), headers=self.header)
        realErrorCode = result.json()['errorCode']
        #print(result.text)
        statusCode = result.status_code
        return statusCode, realErrorCode
    def __put(self):
        result = requests.put(url=self.url, data=eval(self.value), headers=self.header)
        realErrorCode = result.json()['errorCode']
        statusCode = result.status_code
        return statusCode, realErrorCode
