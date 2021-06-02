import time

#库区
def new_storage(driver):
    driver.find_element_by_css_selector("div.btns-qj > div > button").click()
    time.sleep(2)