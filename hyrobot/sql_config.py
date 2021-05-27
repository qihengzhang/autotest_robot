import sqlite3

# 连接数据库
def connect_sql():
    conn = sqlite3.connect('data.sqlite')
    return conn

def cur_sql():
    cur = connect_sql().cursor()
    return cur

def close_sql():
    connect_sql().close()
    cur_sql().close()

def create_table():
    sql = "create table if not exists area(id integer primary key, name text, num integer)"
    sql = "create table if not exists menu(id integer primary key, menu_name text, menu_num integer)"
    connect_sql().execute(sql)

class area:

    @staticmethod
    def insert_area(area_name, area_num):
        sql = "insert into area (name ,num) values (?,?);"
        connect_sql().execute(sql, (area_name, area_num))
        connect_sql().commit()

    @staticmethod
    def delete_area(sql):
        # sql = "delete from area where name = ? or num = ?;"
        connect_sql().execute(sql)
        connect_sql().commit()

    @staticmethod
    def update_area(area_name, area_num):
        sql = "update area set name = ?, num = ?;"
        connect_sql().execute(sql, (area_name, area_num))
        connect_sql().commit()

    @staticmethod
    def select_area(sql):
        re = connect_sql().execute(sql)
        return re


class menu:

    @staticmethod
    def insert_menu(name, num):
        sql = "INSERT INTO menu (menu_name, menu_num) VALUES (?,?);"
        cur_sql().execute(sql, (name, num))
        connect_sql().commit()

    @staticmethod
    def delete_menu(name, num):
        sql = ""
        cur_sql().execute(sql, (name, num))
        connect_sql().commit()

    @staticmethod
    def update_menu(name, num):
        sql = ""
        cur_sql().execute(sql, (name, num))
        connect_sql().commit()

    @staticmethod
    def select_menu(sql):
        re = cur_sql().execute(sql)
        return re



