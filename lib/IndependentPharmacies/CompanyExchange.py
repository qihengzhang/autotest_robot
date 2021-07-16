import time

# 菜单管理完成后删除
def open_company(driver):
    driver.find_element_by_css_selector("#app > section > div > div.el-scrollbar > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > aside > ul > li:nth-child(2) > div").click()
    driver.find_element_by_css_selector(
        "#app > section > div > div.el-scrollbar > div.el-scrollbar__wrap.el-scrollbar__wrap--hidden-default > div > aside > ul > li.el-submenu.is-opened > ul > li:nth-child(1)").click()


def add_company(driver):

    """
    删除输入框属性
    driver.execute_script('document.getElementsByClassName("el-input__inner")[0].removeAttribute("readonly")')

    data = {"供应商名称": "", "供应商类别": "", "注册日期": "", "地址": "",
            "法定代表人": "", "助记码": "", "开户行": "", "银行账户": "", "开户户名": "",
            "企业负责人": "", "质量负责人": "", "联系电话": "", "邮箱": "", "邮政编码": "", "经营范围": "", }

    ScopeBusiness = {"非处方药": "1", "双轨制处方药": "2", "单轨制处方药": "3", "中药饮片": "4",
    "一类医疗器械": "5", "二类医疗器械": "6", "三类医疗器械": "7", "保健食品": "8", }
    """
    driver.find_element_by_css_selector("div.main > div > div > div:nth-child(1) > button").click()
    time.sleep(2)

def info_basic(driver, data: dict, Scope: list) -> dict:
    field = [
        ["供应商名称"],
        ["注册日期", "地址", "法定代表人"],
        ["助记码", "开户行", "银行账户"],
        ["开户户名", "企业负责人", "质量负责人"],
        ["联系电话", "邮箱", "邮政编码"],
    ]
    # 循环输入
    for i in range(0, len(field)):
        rows = str(i + 1)
        rows_path = "div.el-tabs__content > div > form > div:nth-child(" + rows + ")"
        for j in range(0, len(field[i])):
            input_value = field[i][j]   # 当前输入框名称
            if input_value == "供应商名称":
                sort = str(j+2)
            else:
                sort = str(j+1)
            input_path = rows_path + " > " + "div:nth-child(" + sort + ") > div > div > div > input"
            driver.find_element_by_css_selector(input_path).send_keys(
                data[input_value])

    host = driver.find_element_by_css_selector("div.el-tabs__content > div > form")

    # 供应商类别
    driver.execute_script('document.getElementsByClassName("el-input__inner")[1].removeAttribute("readonly")')
    host.find_element_by_css_selector(
        "div:nth-child(1) > div:nth-child(3) > div > div > div > div > div > input").send_keys(data["供应商类别"])
    time.sleep(1)
    driver.find_element_by_css_selector(
        "div[aria-hidden=" + '"false"' + "]> div:nth-child(1) > div > div:nth-child(1) > ul > li:nth-child(1)").click()
    time.sleep(1)

    """
    # 第一行
    供应商名称必填
    host.find_element_by_css_selector("div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(data["供应商名称"])
    time.sleep(1)

    driver.execute_script('document.getElementsByClassName("el-input__inner")[1].removeAttribute("readonly")')
    host.find_element_by_css_selector("div:nth-child(1) > div:nth-child(3) > div > div > div > div > div > input").send_keys(data["供应商类别"])
    time.sleep(1)
    driver.find_element_by_css_selector("div[aria-hidden=" + '"false"' + "]> div:nth-child(1) > div > div:nth-child(1) > ul > li:nth-child(1)").click()
    time.sleep(1)

    # 第二行
    # 输入失败
    driver.execute_script('document.getElementsByClassName("el-input__inner")[2].removeAttribute("readonly")')
    for i in range(1, 4):
        host.find_element_by_css_selector("div:nth-child(2) > div:nth-child(1)  > div > div  > div > input").send_keys(
            data["注册日期"])
        time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(2) > div:nth-child(1)  > div > div  > div > input").send_keys(data["注册日期"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(2) > div:nth-child(2)  > div > div  > div > input").send_keys(data["地址"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(2) > div:nth-child(3)  > div > div  > div > input").send_keys(data["法定代表人"])
    time.sleep(1)

    # 第三行
    host.find_element_by_css_selector("div:nth-child(3) > div:nth-child(1)  > div > div  > div > input").send_keys(data["助记码"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(3) > div:nth-child(2)  > div > div  > div > input").send_keys(data["开户行"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(3) > div:nth-child(3)  > div > div  > div > input").send_keys(data["银行账户"])
    time.sleep(1)

    # 第四行
    host.find_element_by_css_selector("div:nth-child(4) > div:nth-child(1)  > div > div  > div > input").send_keys(data["开户户名"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(4) > div:nth-child(2)  > div > div  > div > input").send_keys(data["企业负责人"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(4) > div:nth-child(3)  > div > div  > div > input").send_keys(data["质量负责人"])
    time.sleep(1)

    # 第五行
    host.find_element_by_css_selector("div:nth-child(5) > div:nth-child(1)  > div > div  > div > input").send_keys(data["联系电话"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(5) > div:nth-child(2)  > div > div  > div > input").send_keys(data["邮箱"])
    time.sleep(1)

    host.find_element_by_css_selector("div:nth-child(5) > div:nth-child(3)  > div > div  > div > input").send_keys(data["邮政编码"])
    time.sleep(1)
    """

    """
    经营范围必填
    """
    ScopeBusiness = {"非处方药": "1", "双轨制处方药": "2", "单轨制处方药": "3", "中药饮片": "4",
                     "一类医疗器械": "5", "二类医疗器械": "6", "三类医疗器械": "7", "保健食品": "8", }
    for i in range(len(Scope)):
        host.find_element_by_css_selector("div:nth-child(6) > div:nth-child(1)  > div > div > div  > div > div:nth-child(2) > input").click()
        time.sleep(1)
        driver.find_element_by_css_selector("div[aria-hidden=" + '"false"' + "] > div:nth-child(1) > div > div:nth-child(1) > ul > li:nth-child("
                                            + ScopeBusiness[Scope[i]] + ")").click()
        time.sleep(1)

def pull_button(driver):
    driver.find_element_by_css_selector("div.person > button").click()
    time.sleep(1)

def info_personnel(driver, data):
    """
    data = [
    {"姓名": "", "身份证号码": "", "身份证有效期": "", "手机号码": ""},
    {"姓名": "", "身份证号码": "", "身份证有效期": "", "手机号码": ""},
    {"姓名": "", "身份证号码": "", "身份证有效期": "", "手机号码": ""}
]
    """
    person_num = driver.find_element_by_css_selector("div.person > div")
    print(type(person_num))
    print(person_num.size())
    for i in range(0, person_num):
        num = str(i+3)
        driver.find_element_by_css_selector("div.person > div:nth-child(" + num + ")"
        ">form > div:nth-child(1) > div:nth-child(1) > div > div > div > input").send_keys(data[i]["姓名"])
        time.sleep(1)

        driver.find_element_by_css_selector("div.person > div:nth-child(" + num + ") "
        ">form > div:nth-child(1) > div:nth-child(2) > div > div > div > input").send_keys(data[i]["身份证号码"])
        time.sleep(1)

        driver.find_element_by_css_selector("div.person > div:nth-child(" + num + ") "
        ">form > div:nth-child(1) > div:nth-child(3) > div > div > div > input").send_keys(data[i]["身份证有效期"])
        time.sleep(1)

        driver.find_element_by_css_selector("div.person > div:nth-child(" + num + ") "
        ">form > div:nth-child(2) > div:nth-child(1) > div > div > div > input").send_keys(data[i]["手机号"])
        time.sleep(1)
