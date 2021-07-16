# 支付方式
import time

def new_payment(driver):
    driver.find_element_by_css_selector("div.btns-qj > div > button").click()
    time.sleep(1)
