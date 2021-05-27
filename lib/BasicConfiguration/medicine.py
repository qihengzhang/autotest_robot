from selenium import webdriver
import time



# 新增门店
def info_medicine(driver, province, city, district):
    # 点击新增按钮
    driver.find_element_by_css_selector(
        'div.btns-qj > div:nth-child(1) > button:nth-child(1)').click()
    time.sleep(2)

    # 选择门店地址
    driver.find_element_by_css_selector('form.el-form > div:nth-child(9) > div > div > div:nth-child(1)').click()

    # 选择省/市
    Provinces = {
        '北京市': '1', '安徽省': '2', '福建省': '3', '江西省': '4', '山东省': '5', '河南省': '6', '湖北省': '7', '天津市': '8', '湖南省': '9',
        '广东省': '10', '广西壮族自治区': '11', '山西省': '12', '海南省': '13', '重庆市': '14', '四川省': '15', '贵州省': '16', '云南省': '17',
        '西藏自治区': '18', '陕西省': '19', '甘肃省': '20', '青海省': '21', '宁夏回族自治区': '22', '新疆维吾尔自治区': '23', '台湾省': '24',
        '香港特别行政区': '25', '澳门特别行政区': '26', '河北省': '27', '内蒙古自治区': '28', '辽宁省': '29', '吉林省': '30',
        '黑龙江省': '31', '上海市': '32', '江苏省': '33', '浙江省': '34',
    }

    cities = {
        '北京城区': '1', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',
        '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '', '': '',

    }

    districts = {

    }
    root = driver.find_element_by_css_selector('body > div:nth-child(7) > div:nth-child(1)')
    root.find_element_by_css_selector(
        "div.el-scrollbar:nth-child(1) > div:nth-child(1) > ul > li:nth-child(" + Provinces[province] + ")").click()
    driver.find_element_by_css_selector(
        "div.el-scrollbar:nth-child(2) > div:nth-child(1) > ul > li:nth-child(" + cities[city] + ")").click()
    driver.find_element_by_css_selector(
        "div.el-scrollbar:nth-child(3) > div:nth-child(1) > ul > li:nth-child(" + districts[district] + ")").click()

    return driver
