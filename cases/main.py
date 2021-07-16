field = [
        ["供应商名称"],
        ["注册日期", "地址", "法定代表人"],
        ["助记码", "开户行", "银行账户"],
        ["开户户名", "企业负责人", "质量负责人"],
        ["联系电话", "邮箱", "邮政编码"],
    ]
driver = 1
data = []


# host = driver.find_element_by_css_selector("div.el-tabs__content > div > form")
for i in range(0, len(field)):
    print("第" + str(i + 1) + "行")
    rows = str(i+1)
    hangshu = "div:nth-child(" + rows + ")"


    for j in range(0, len(field[i])):
        print("第" + str(j+1) + "个")
        print(field[i][j])
        sort = str(j+1)
        geshu = hangshu + " > div:nth-child(" + sort + ") > div > div > div > input"
        print(geshu)
