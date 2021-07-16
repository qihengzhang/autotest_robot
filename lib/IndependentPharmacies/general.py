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
    driver.find_element_by_css_selector('div.el-row > div:nth-child(1) > div > div > div > input')\
        .send_keys(username)
    driver.find_element_by_css_selector('div.el-row > div:nth-child(2) > div > div > div > input')\
        .send_keys(password)
    time.sleep(2)
    driver.find_element_by_css_selector('div.el-row > button').click()


if __name__ == '__main__':
    print('完成')