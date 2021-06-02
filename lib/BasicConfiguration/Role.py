import self as self
from selenium import webdriver
import time
from lib.general import *
from hyrobot.common import *
#路线管理
class role:

    @staticmethod
    def new(driver, rolename, explain, node, day1,day2):
        driver.find_element_by_css_selector("div.btns-qj > div > button").click()
        time.sleep(2)
        STEP(1, '登录')
        driver.find_element_by_css_selector("div.el-form-item:nth-child(1) > div:nth-child(2) > div >input").send_keys(rolename)
        time.sleep(2)
        driver.find_element_by_css_selector(".el-form-item__content > div > div").click()
        time.sleep(5)
        # 运输类型需要设置变量
        driver.find_element_by_css_selector("li.el-select-dropdown__item:nth-child(3)").click()
        time.sleep(2)

        driver.find_element_by_css_selector(".el-textarea__inner").send_keys(explain)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(4) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(node)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(5) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(day1)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(day2)
        time.sleep(2)
        driver.find_element_by_css_selector("div.dialog-footer > button:nth-child(2)").click()
        driver.find_element_by_css_selector("div.el-table__fixed-right > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button.el-button--default:nth-child(2) > span:nth-child(1)").click()
        time.sleep(1)

    #编辑
    @staticmethod
    def edit(driver,rolename,explain,node,day1,day2):
        driver.find_element_by_css_selector("div.el-table__fixed-right > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(1) > div:nth-child(2) > div >input").send_keys(rolename)
        time.sleep(2)
        driver.find_element_by_css_selector(".el-form-item__content > div > div").click()
        time.sleep(5)
        # 运输类型需要设置变量
        driver.find_element_by_css_selector("li.el-select-dropdown__item:nth-child(3)").click()
        time.sleep(2)

        driver.find_element_by_css_selector(".el-textarea__inner").send_keys(explain)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(4) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(node)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(5) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(day1)
        time.sleep(2)
        driver.find_element_by_css_selector("div.el-form-item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(day2)
        time.sleep(2)
        driver.find_element_by_css_selector("div.dialog-footer > button:nth-child(2)").click()

    #删除
    @staticmethod
    def delete(driver):
        driver.find_element_by_css_selector(".el-table__fixed-right > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(10) > div:nth-child(1) > button:nth-child(3) > span:nth-child(1)").click()

