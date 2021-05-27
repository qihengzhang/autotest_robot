from selenium import webdriver
import time

# 打开浏览器
def open_browser(url):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(url)
    driver.find_element_by_css_selector()
    return driver

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
    }

    cities = {
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
