from hyrobot.common import *
from lib.IndependentPharmacies.general import *
from lib.IndependentPharmacies.CompanyExchange import *
# ==========================================
import time


class autotest:
    name = '管理员首页 - UI-0101'

    def teststeps(self):
        STEP(1, '打开网址')
        # testing = open_Firefox("https://test.91medicine.net/pharmacy-system/#/login")
        # testing = open_Chorme("https://test.91medicine.net/pharmacy-system/#/login")
        # testing = open_Chorme("https://test-store-single.91medicine.net/singledrugstore/#/login")
        testing = open_Firefox("https://test-store-single.91medicine.net/singledrugstore/#/login")

        STEP(2, '登录')
        login(testing, 'zhang001', '123456a')
        time.sleep(2)

        STEP(3, '打开供应商首营')
        open_company(testing)

        STEP(4, '添加供应商首营')
        add_company(testing)
        #
        # data = {"供应商名称": "123", "供应商类别": "生产企业", "注册日期": "2021-07-01", "地址": "1",
        #         "法定代表人": "1", "助记码": "1", "开户行": "1", "银行账户": "1", "开户户名": "1",
        #         "企业负责人": "1", "质量负责人": "1", "联系电话": "1", "邮箱": "1", "邮政编码": "1", }
        #
        # scope = ["非处方药"]
        #
        # info_basic(testing, data, scope)

        STEP(5, '新增销售人员信息')
        pull_button(testing)
        pull_button(testing)

        data = [
            {"姓名": "1", "身份证号码": "632323190605261642", "身份证有效期": "", "手机号码": "15996857412"},
            {"姓名": "2", "身份证号码": "632323190605261642", "身份证有效期": "", "手机号码": "15996857412"},
            {"姓名": "3", "身份证号码": "632323190605261642", "身份证有效期": "", "手机号码": "15996857412"}
        ]

        info_personnel(testing, data)
