import sqlite3

# 连接数据库
def connect_sql():
    con = sqlite3.connect('data.sqlite')
    cur = con.cursor()
    return cur

def create_table():
    sql = "create table if not exists area(id integer primary key, name text, num integer)"
    sql = "create table if not exists menu(id integer primary key, menu_name text, menu_num integer)"
    connect_sql().execute(sql)

def insert_area(area_name, area_num):
    sql = "insert into area (name,num) values (" + area_name + ", " + area_num + ")"
    connect_sql().execute(sql)

def updata_area(area_name, area_num):
    sql = "update area set name = " + area_name + ", num = " + area_num + ""
    connect_sql().execute(sql)

def delete_area(area_name, area_num):
    sql = "delete from area where name = " + area_name + " or num = " + area_num + ""
    connect_sql().execute(sql)

def select_area(sql):
    return connect_sql().execute(sql)
sql = "select * from area"
a = connect_sql().execute(sql)
print(a)