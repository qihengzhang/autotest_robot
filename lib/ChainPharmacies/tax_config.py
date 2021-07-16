from selenium import webdriver
import time

def new_tax(driver, tax_no, drawer, reviewer):
    driver.find_element_by_css_selector(".btns-qj > div > button").click()
    time.sleep(1)
    driver.find_element_by_css_selector("form.el-form > div:nth-child(1) > div > div > input").send_keys(tax_no)
    driver.find_element_by_css_selector("form.el-form > div:nth-child(2) > div > div > input").send_keys(drawer)
    driver.find_element_by_css_selector("form.el-form > div:nth-child(3) > div > div > input").send_keys(reviewer)
    time.sleep(1)
    driver.find_element_by_css_selector("div.dialog-footer  > button:nth-child(2)").click()
