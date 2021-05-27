from selenium import webdriver
import time
#活动审核
def activity(driver, personnel):
    driver.find_element_by_css_selector("div.el-table__fixed-right > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > button:nth-child(1)").click()
    time.sleep(2)
    driver.find_element_by_css_selector("div.public-table > div:nth-child(1) > button").click()
    time.sleep(2)
    driver.find_element_by_css_selector("input.el-input__inner").send_key(personnel)
    time.sleep(5)
    driver.find_element_by_css_selector("el-select-dropdown__item hover").click()
    time.sleep(2)
    driver.find_element_by_css_selector("span.dialog-footer > button:nth-child(2)").click()
