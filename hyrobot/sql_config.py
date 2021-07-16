import sqlite3

# 连接、关闭数据库
class ConnectSqlLite:

    @staticmethod
    def connect():
        conn = sqlite3.connect('./hyrobot/data.sqlite')
        return conn

    # @staticmethod
    # def conn_cur():
    #     cur = ConnectSqlLite.connect().cursor()
    #     return cur

    @staticmethod
    def close_sql():
        ConnectSqlLite.conn_cur().close()
        ConnectSqlLite.connect().close()

    @staticmethod
    def create_table(sql):
        sql = "create table if not exists area(id integer primary key, name text, num integer)"
        # sql = "create table if not exists menu(id integer primary key, menu_name text, menu_num integer)"
        ConnectSqlLite.connect().cursor().execute(sql)
        ConnectSqlLite.connect().commit()

# area表
class area:

    @staticmethod
    def insert_area(area_name, area_num):
        sql = "insert into area (name ,num) values (?,?);"
        ConnectSqlLite.connect().cursor().execute(sql, (area_name, area_num))
        ConnectSqlLite.connect()().commit()

    @staticmethod
    def delete_area(sql):
        # sql = "delete from area where name = ? or num = ?;"
        ConnectSqlLite.connect().cursor().execute(sql)
        ConnectSqlLite.connect().commit()

    @staticmethod
    def update_area(area_name, area_num):
        sql = "update area set name = ?, num = ?;"
        ConnectSqlLite.connect().cursor().execute(sql, (area_name, area_num))
        ConnectSqlLite.connect().commit()

    @staticmethod
    def select_area(cur, sql):
        re = cur.execute(sql)
        return re

# menu表
class menu:

    @staticmethod
    def insert_menu(name, num):
        sql = "INSERT INTO menu (menu_name, menu_num) VALUES (?,?);"
        ConnectSqlLite.conn_cur().execute(sql, (name, num))
        ConnectSqlLite.connect().commit()

    @staticmethod
    def delete_menu(name, num):
        sql = ""
        ConnectSqlLite.connect().cursor().execute(sql, (name, num))
        ConnectSqlLite.connect().commit()

    @staticmethod
    def update_menu(name, num):
        sql = ""
        ConnectSqlLite.connect().cursor().execute(sql, (name, num))
        ConnectSqlLite.connect().commit()

    @staticmethod
    def select_menu(name):
        sql = "select menu_num from menu where menu_name = '" + name + "'"
        re = ConnectSqlLite.connect().cursor().execute(sql)
        return re.fetchall()


def tuple_to_str(data_info):
    out = "".join(data_info[0])
    return out

if __name__ == '__main__':
    print('启动')
    data = menu.select_menu('首页')
    a = tuple_to_str(data)
    print(type(a), a)
