# 审核流程配置


from selenium import webdriver
import time

approve_list = {'活动审核': '1', '优惠卷审核': '2', '养护审核': '3', '购进退货审核':'4', '损益申请审核': '5', '仓库购进退货单审核': '6',
                '门店退仓审核': '7', '首营资料审核': '8', '配送申请审核': '9', '采购计划审核': '10', }

# 活动审核
def activity(driver, approve_name, personnel):

    driver.find_element_by_css_selector(
        "div.el-table__fixed-right > div:nth-child(2) > table > tbody > tr:nth-child(" + approve_list[approve_name] +
        ") > td:nth-child(5) > div > button:nth-child(1)"
    ).click()
    time.sleep(2)
    driver.find_element_by_css_selector("div.public-table > div:nth-child(1) > button").click()
    time.sleep(2)

    driver.execute_script('document.getElementsByClassName("el-input__inner")[0].removeAttribute("readonly")')
    driver.find_element_by_css_selector("input.el-input__inner").send_keys(personnel)
    time.sleep(5)
    driver.find_element_by_css_selector("li.el-select-dropdown__item").click()
    time.sleep(2)
    driver.find_element_by_css_selector("span.dialog-footer > button:nth-child(2)").click()
    time.sleep(2)
    driver.find_element_by_css_selector("div.action > div >div:nth-child(2)>button").click()
    driver.find_element_by_css_selector(
        "div.el-table__fixed-right > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > "
        "td:nth-child(5) > div:nth-child(1) > button:nth-child(2) > span:nth-child(1)").click()
    time.sleep(2)
    driver.find_element_by_css_selector("div.el-message-box__btns > button:nth-child(2)").click()
