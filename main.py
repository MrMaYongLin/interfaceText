"""
@Author : mayonglin
@File : configHttp.py
@Software: PyCharm
功能描述：查找所有的测试用例，执行测试用例并生成报告，实现自动清理报告
实现逻辑：
    1-导包，unit test，HTMLTestrunner
    2-使用Testloader查找测试用例，生成测试套件
    3-使用HTMLTestrunner执行测试用例，并生成报告
    4-实现自动清理报告的功能（1-自动判断报告的数量。2-每次运行前，清理之前的报告。二选一）
    5-自动将生成的报告添加到邮件的附件并投送
"""
#1-导包，unit test，HTMLTestrunner
import unittest
import os,time
from HTMLTestRunner import HTMLTestRunner
from common.logs import logger
from common.configEmail import ConfigEmail
project_dir = os.path.dirname(__file__)

def create_suite():
    """
    2-使用Testloader查找测试用例，生成测试套件
    :return:
    """
    case_dir = project_dir + '/testCase'
    print(case_dir)
    suite = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='Test*.py', top_level_dir=None)
    return suite

def auto_clear():
    """
    实现自动清理报告的功能
    :return:
    """
    filelist = sorted(os.listdir(project_dir + '/report'))
    logger.info(f'report下面的所有文件： {filelist}')
    if len(filelist) > 5:
        for i in range(len(filelist) - 5):
            logger.debug(len(filelist))
            os.remove(project_dir + '/report/' + filelist[i])
    logger.debug(filelist)

if __name__ == '__main__':
    #print(create_suite())
    create_time = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
    suite = create_suite()
    #3 - 使用HTMLTestrunner执行测试用例，并生成报告
    reports = project_dir + '/report/' + create_time +'_report.html'
    fp = open(reports, 'wb')
    runner = HTMLTestRunner(stream=fp, title="接口测试报告", description="接口测试报告详情")
    runner.run(suite)
    fp.close()
    auto_clear()
    ce = ConfigEmail()
    ce.send_email()

