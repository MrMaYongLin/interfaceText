"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/29 11:13
# @Author : mayonglin
# @File : TestCase.py
# @Software: PyCharm
# 功能描述:获取测试数据后，根据实际的请求参数（method），请求对应的方法请求接口
#实现逻辑：
    1、获取测试数据。调用readExcel内部的getdata方法
    2、提取测试数据内的method方法
    3、根据method方法进行判断
        3-1 如果是get方法就调用get方法
        3-2 如果是post方法就调用post方法
    4、从接口请求的结果中，提取需要断言的字段errorCode
    5、将实际提取的errorCode与Excel中的预期值进行对比
        5-1 相同即通过 success
        5-2 不同即失败 fail
    6、将结果断言的结果写入Excel
"""
import unittest
import requests
from common.readExcel import ReadExcel
from ddt import ddt, data, unpack
# 1、获取测试数据。调用readExcel内部的getdata方法
read = ReadExcel()
read_data = read.get_data()

@ddt
class TestCase(unittest.TestCase):
#2、提取测试数据内的method方法
    @data(*read_data)
    @unpack
    def test_run(self, id, interfaceUrl, name, Method, value, expect, real, status):
        id = id
        url = interfaceUrl
        value = eval(value)
        method = Method
        expect = expect
        if method == 'get':
            result = requests.get(url=url, params=value)
            print("result", result.json())
        elif method == 'post':
            result = requests.post(url=url, data=value)
            print("result", result.json())
        real_code = result.json()['errorCode']
        try:
            self.assertEqual(str(real_code),str(expect))
            status = 'success'
        except AssertionError as msg:
            print('系统提示：', msg)
            status = 'fail'
            raise
        finally:
            pass
if __name__ == '__main__':
    unittest.main