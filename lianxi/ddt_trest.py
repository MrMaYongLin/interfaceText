"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/12 14:25
@Author : mayonglin
@File : ddt_trest.py
@Software: PyCharm
功能描述：
实现逻辑：
"""
import unittest
from ddt import ddt, data, unpack

test_data = [[1, 2], [3, 4], [5, 6], [7, 8]]
@ddt
class Testmyddt(unittest.TestCase):
    #单次执行，每次传递多个参数
    @data((11, 11))
    @unpack
    def test_one(self, value1, value2):
        print('------------' , value1, value2)
        self.assertEqual(value1, value2)
    #多次传递，每次传递多个参数
    @data([1, 2], [3, 4])
    @unpack
    def test_two(self, value1, value2):
        print('++++++++++', value1, value2)
        self.assertEqual(value1, value2)
    #可变参数，根据所传元素的个数决定传递次数
    @data(*test_data)
    @unpack
    def test_three(self, value1, value2):
        print('???????????', value1, value2)
        self.assertEqual(value1, value2)
if __name__ == '__main__':
    unittest.main(verbosity=3)