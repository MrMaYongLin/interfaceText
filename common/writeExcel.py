"""
!/usr/bin/env python
-*- coding:utf-8 -*-
@Time : 2023/1/18 11:07
@Author : mayonglin
@File : writeExcel.py
@Software: PyCharm
功能描述：拿到test case的实际断言结果，写入到测试数据data.xlsx
实现逻辑：
    1-导包
    2-定义写入数据类
        2.1-定义初始化方法
            1-准备写入的excel文件
            2-确定sheet页
        2.2-定义写入数据的方法
            1-准备写入的测试结果
            2-准备写入的目标单元格的行和列
            3-准备写入
            4-保存
"""
#    1-导包
import xlrd
from xlutils.copy import copy
from common.logs import logger
import os
#    2-定义写入数据类
class WriteExcle():
#2.1-定义初始化方法
    def __init__(self):
        #1-准备写入的excel文件
        self.excle = os.path.dirname(os.path.dirname(__file__)) + r'/testData/data.xls'
        logger.info('写入excel的路径是：%s' % self.excle)
        self.rb = xlrd.open_workbook(self.excle)
        self.wb = copy(self.rb)
        #2-确定sheet页
        self.sheet = self.wb.get_sheet(0)

#2.2-定义写入数据的方法
    def write_excel(self, x, y, real, status):
        """
        :param x:写入数据的行
        :param y:写入数据的列
        :param real:写入的realErrorCode
        :param status:写入的Status
        :return:
        """
        #1-准备写入的测试结果
        #2-准备写入的目标单元格的行和列
        #3-准备写入
        self.sheet.write(int(x), y, real)
        self.sheet.write(int(x), y+1, status)
        self.wb.save(self.excle)
