#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2022/12/26 16:28
# @Author : mayonglin
# @File : lianxi.py
# @Software: PyCharm
# 功能描述
import os, xlrd
class AAA():
    """
    #确定文件的位置
    #打开文件
    #确定文件的标签页
     #获取当前标签页的所有行
     #获取当前标签页的所有列
    """
    def __init__(self):
        try:
            cur_path = os.path.dirname(os.path.dirname(__file__))
            excel_path = cur_path + '/testData/data.xlsx'
            self.file = xlrd.open_workbook(excel_path)
            print("文件打开成功")
            self.sheet_tag = self.file.sheet_by_name('Sheet1')
            self.nrows = self.sheet_tag.nrows
            self.ncols = self.sheet_tag.ncols
        except:
            print("文件打开失败")
        finally:
            self.file.release_resources()
    def getData(self):
        """
        #定义一个空列表，后续用于接收取出来的每行数据
        #将第一行的数据单独取出来
        #遍历循环其他行的数据
        #第一行的数据已经被单独取出来，并不需要再次取，所以跳过这个循环
        #循环遍历出其他行的数据
        #定义一个空字典，作为出来的数据载体
        #循环遍历将第一行的数据当成key值，其他行的数据当成value值存到字典中
        #value[name[j]]将第一行的数据当成key值直接使用；row_value[j]将其他行的数据当成value值
        #将字典存到总列表中
        """
        list_all = []
        name = self.sheet_tag.row_values(0)
        for i in range(self.nrows):
            if i == 0:
                continue
            row_value = self.sheet_tag.row_values(i)
            valuse = {}
            for j in range(len(row_value)):
                valuse[name[j]] = row_value[j]
            list_all.append(valuse)
            print(list_all)

if __name__ == '__main__':
    a = AAA()
    a.getData()