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
class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass
    @classmethod
    def setUpClass(cls) -> None:
        # 1、获取测试数据。调用readExcel内部的getdata方法
        cls.read = ReadExcel()
        cls.data = cls.read.get_data()

    #2、提取测试数据内的method方法
    def test_run(self):
        for i in range(len(self.data)):
            url = self.data[i]['interfaceUrl']
            value1 = eval(self.data[i]['value'])
            print(value1)
            expect = self.data[i]['expect']
            id = self.data[i]['id']
            method = self.data[i]['Method']
            if method == 'get':
                result = requests.get(url=url, params=value1)

            elif method == 'post':
                result = requests.post(url=url, data=value1)
            real_code = result.json()['errorCode']
            try:
                self.assertEqual(real_code, expect)
            except AssertionError as msg:
                print('系统提示：', msg)
                status = 'fail'
            finally:
                pass

    def tearDown(self) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

if __name__ == '__main__':
    unittest.main