from lib.general import *
from lib.BasicConfiguration.tax_config import *
from hyrobot.common import *
from lib.BasicConfiguration.ApproveConfiguration import *
import time


class autotest:
    name = '管理员首页 - UI-0101'

    def teststeps(self):
        STEP(1, '打开网址')
        testing = open_Firefox("https://test.91medicine.net/pharmacy-system/#/login")
        # testing = open_Chorme("https://test.91medicine.net/pharmacy-system/#/login")

        STEP(2, '登录')
        login(testing, 'mayday5', 'may111111')
        time.sleep(2)

        STEP(3, '进入目录')
        one = directory_One(testing, '基础配置')
        time.sleep(1)
        two = directory_Two(one, '审批流程配置')
        time.sleep(1)
        #directory_Three(two, '柜组管理')
        #timesleep(2)
        #new_tax(testing, '1231231', '碍事法师', '碍事法师')
        three = activity(testing, '审批流程配置')
        activity(three, '采购员')


