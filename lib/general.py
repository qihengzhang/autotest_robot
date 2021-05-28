from selenium import webdriver
from hyrobot.sql_config import menu, tuple_to_str
from hyrobot.sql_config import ConnectSqlLite
import time

level_dict = {'首页': '1', '基础配置': '2', '系统管理': '3', '会员管理': '4', '首营管理': '5',
        '商品库': '6', '库存管理': '7', '仓储管理': '8', '订单管理': '9', '采购管理': '10',
        '营销管理': '11', '配送管理': '12', '养护管理': '13', '盘点管理': '14', '班次管理': '15',
        '审核管理': '16', '总部入库': '17', '门店验收': '18',
        '税控盘管理': '1', '审批流程配置': '2', '路线管理': '3', '支付方式': '4', '效期限制': '5',
        '仓储配置': '6', '门店配置': '7', '基础配置-企业资料': '8', '采购合同': '9', '标签库管理': '10',
        '员工管理': '1', '角色管理': '2', '审批角色管理': '3', '日志管理': '4', '字典管理': '5', '字典类型管理': '6',
        '会员列表': '1', '会员等级': '2', '会员活动日': '3', '会员储值': '4',
        '供应商首营': '1', '品种首营': '2',
        '药品': '1', '其他': '2',
        '药品库存': '1', '其他库存': '2',
        '同仓补货': '1', '库区明细': '2', '损益管理': '3', '门店库存查询': '4', '商品总库存查询': '5',
        '收银台': '1', '支付明细': '2', '退款明细': '3',
        '采购计划单': '1', '采购订单': '2', '购进退货申请': '3',
        '促销活动配置': '1', '促销活动列表': '2', '优惠卷': '3', '优惠卷列表': '4',
        '配送申请': '1', '配送单': '2', '配送退仓申请': '3',
        '养护任务': '1', '养护管理-养护管理': '2',
        '盘点': '1',
        '班次设置': '1', '班次列表': '2',
        '品种首营审核': '1', '企业首营审核': '2', '采购审核': '3', '配送审核': '4', '损益审核': '5', '购进退货审核': '6', '配送退仓审核': '7',
        '采购入库': '1', '配送退回入库': '2',
        '库区管理': '1', '货架管理': '2', '柜组管理': '3',
        '门店组管理': '1', '门店管理': '2', '合同缴费订单': '3',
        '登录日志': '1', '操作日志': '2',
        '企业资料': '1', '人员资料': '2',
        '药品首营': '1', '其他首营': '2',
        '收货单': '1', '验货单': '2', '入库单': '3',
        '退仓-收货单': '1', '退仓-验货单': '2', '退仓-入库单': '3',
       }
conn = ConnectSqlLite.connect('data.sqllite')
cur = conn.cursor()

# 打开浏览器
def open_browser(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(url)
    return driver

# 登录
def login(driver, username, password):
    driver.find_element_by_css_selector('.app-form > form > div:nth-child(1) > div > div > div > input')\
        .send_keys(username)
    driver.find_element_by_css_selector('.app-form > form > div:nth-child(2) > div > div > div > input')\
        .send_keys(password)
    time.sleep(2)
    driver.find_element_by_css_selector('.submit-form > button:nth-child(2)').click()

# 注册
def register(driver, username, password):
    driver.find_element_by_css_selector('.submit-form > button:nth-child(3)').click()
    time.sleep(2)

# 打开一级目录
def directory_One(driver, OneLevel):
    data = menu.select_menu(cur, OneLevel)
    num = tuple_to_str(data)
    print(num)
    try:
        if OneLevel is not None:
            driver.find_element_by_css_selector(
                ".menu > div > div > div > ul > li:nth-child(" + num + ")").click()
        return driver.find_element_by_css_selector(".menu > div > div > div > ul > li:nth-child(" + level_dict[OneLevel] + ")")

    except Exception:
        print('内容不匹配，请输入正确的一级目录')

# 打开二级目录
def directory_Two(one, TwoLevel):
    data = menu.select_menu(cur, TwoLevel)
    num = tuple_to_str(data)
    print(num)
    try:
        if TwoLevel is not None:
            one.find_element_by_css_selector("ul > li:nth-child(" + num + ")").click()
        # return one.find_element_by_css_selector("ul > li:nth-child(" + level_dict[TwoLevel] + ")")
        return level_dict[TwoLevel]
    except Exception:
        print('内容不匹配，请输入正确的二级目录')

# 打开三级目录
def directory_Three(two, ThreeLevel):
    try:
        if ThreeLevel is not None:
            data = menu.select_menu(cur, ThreeLevel)
            num = tuple_to_str(data)
            two.find_element_by_css_selector(
                "ul > li:nth-child(" + num + ")").click()

    except Exception:
        print('内容不匹配，请输入正确的三级目录')


if __name__ == '__main__':
    print('完成')