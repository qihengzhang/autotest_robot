from selenium import webdriver
from hyrobot.sql_config import menu, tuple_to_str
from hyrobot.sql_config import ConnectSqlLite
import time

# 打开浏览器
def open_Chorme(url):
    driver = webdriver.Chorme()
    driver.implicitly_wait(5)
    driver.get(url)
    return driver

def open_Firefox(url):
    driver = webdriver.Firefox()
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
    data = menu.select_menu(OneLevel)
    num = tuple_to_str(data)
    try:
        if OneLevel is not None:

            driver.find_element_by_css_selector(
                ".menu > div > div > div > ul > li:nth-child(" + num + ")").click()
        return driver.find_element_by_css_selector(".menu > div > div > div > ul > li:nth-child(" + num + ")")

    except Exception:
        print('内容不匹配，请输入正确的一级目录', '数据：' + num)

# 打开二级目录
def directory_Two(one, TwoLevel):
    data = menu.select_menu(TwoLevel)
    num = tuple_to_str(data)
    try:
        if TwoLevel is not None:

            one.find_element_by_css_selector("ul > li:nth-child(" + num + ")").click()
        return one.find_element_by_css_selector("ul > li:nth-child(" + num + ")")
    except Exception:
        print('内容不匹配，请输入正确的二级目录', '数据：' + num)

# 打开三级目录
def directory_Three(two, ThreeLevel):
    data = menu.select_menu(ThreeLevel)
    num = tuple_to_str(data)
    try:
        if ThreeLevel is not None:

            two.find_element_by_css_selector(
                "ul > li:nth-child(" + num + ")").click()

    except Exception:
        print('内容不匹配，请输入正确的三级目录', '数据：' + num)


if __name__ == '__main__':
    print('完成')