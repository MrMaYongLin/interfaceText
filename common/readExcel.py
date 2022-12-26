"""
readExcel的分析与设计
功能描述：获取testData目录下的data文件，并将文件中的数据提供给testCase使用
目标：
    将每行数据以字典的格式显示，并且将所有的数据以列表的形式显示
    所以最后的结果：[{'id':'1','url':'http://www.baidu.com',...},{'id':'2','url':'http://www.baidu.com',...}]
实现步骤：
    1：先打开文件
    2：定位到文件的标签页
    3：获取当前标签页的最大行
    4：将第一行的数据单独取出来形成列表
    5：将所有行的数据以列表的形式取出来
    6：将第一行的列表以key值，其他行的数据以value值形成一个列表
    7:将整理后的列表提供给testCase使用

注：一个小方法，将两个列表形成一个字典
key = ['id', 'url', 'name']
value = [1, 2, 3]
dict1 = {key[i] : value[i] for i in range(len(key))}

"""
import xlrd, os
class ReadExcel():
    def __init__(self):
        #确定文件的位置
        cur_path = os.path.dirname(os.path.dirname(__file__))
        excel_dir = cur_path + '/testData/data.xlsx'
        print(excel_dir)
        #打开文件
        readbook = xlrd.open_workbook(excel_dir)
        print(readbook)
        #确定文件的标签页
        self.sheet_tag = readbook.sheet_by_name('Sheet1')
        #获取当前标签页的所有行
        self.nrows = self.sheet_tag.nrows
        #获取当前标签页的所有列
        self.ncols = self.sheet_tag.ncols
        print(self.nrows, self.ncols)

    def get_data(self):
        #定义一个空列表，后续用于接收取出来的每行数据
        list_all = []
        #将第一行的数据单独取出来
        name = self.sheet_tag.row_values(0)
        #遍历循环其他行的数据
        for i in range(self.nrows):
            #第一行的数据已经被单独取出来，并不需要再次取，所以跳过这个循环
            if i == 0:
                continue
            #循环遍历出其他行的数据
            row_value = self.sheet_tag.row_values(i)
            #定义一个空字典，作为出来的数据载体
            value = {}
            #循环遍历将第一行的数据当成key值，其他行的数据当成value值存到字典中
            for j in range(len(row_value)):
            #value[name[j]]将第一行的数据当成key值直接使用；row_value[j]将其他行的数据当成value值
                value[name[j]] = row_value[j]
            # list1 = row_value
            #将字典存到总列表中
            list_all.append(value)

        return list_all

if __name__ == '__main__':
    read = ReadExcel()
    read.get_data()
