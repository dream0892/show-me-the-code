#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
#需要弄清楚mysql与pymysql的区别
'''
用过mysql-python和pymysql，两者皆有不尽如人意的地方
比如mysql-python是封装的mysqlclient ，无法到底连接的socket。
而pymysql可以得到连接socket，却不能使用use_result语义，我有个项目两种情况都需要。
我只好两个都用。

作者：shafreeck
链接：https://www.zhihu.com/question/19869186/answer/13465316
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
import mysql.connector
import string
import random

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return (string.ascii_letters + string.digits)


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(str(key_gen()))
    return result


class mysql_init(object):

    def __init__(self, conn):
        self.conn = None

    # connect to mysql
    def connect(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="fjfh1so",
            db="test",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()


def process():
    dbconn.connect()
    conn = dbconn.cursor()
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryData(conn)
    dbconn.close()

# def execute(sql):
#     '''执行sql'''
#     conn=dbconn.cursor()
#     conn.execute(sql)

# def executemany(sql, tmp):
#     '''插入多条数据'''
#     conn=dbconn.cursor()
#     conn.executemany(sql,tmp)


def query(sql, conn):
    '''查询sql'''
    # conn=dbconn.cursor()
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


def DropTable(conn):
    # conn=dbconn.cursor()
    conn.execute("DROP TABLE IF EXISTS `code`")


def CreateTable(conn):
    # conn=dbconn.cursor()
    sql_create = ''' CREATE TABLE `code` (`code` varchar(50) NOT NULL,`id` INT NOT NULL AUTO_INCREMENT,PRIMARY KEY (`id`))'''
    conn.execute(sql_create)


def InsertDatas(conn):
    # conn=dbconn.cursor()
    # insert_sql = "insert into user_key values(%s)"
    insert_sql = "INSERT INTO code(code) VALUES (%(value)s)"
    key_list = key_num(KEY_ALL)

    conn.executemany(insert_sql, [dict(value=v) for v in key_list])


def DeleteData():
    del_sql = "delete from user_key where id=2"
    execute(del_sql)


def QueryData(conn):
    sql = "select * from code"
    rows = query(sql, conn)
    printResult(rows)


def printResult(rows):
    if rows is None:
        print("rows None")
    for row in rows:
        print(row)

if __name__ == "__main__":
    dbconn = mysql_init(None)
    process()
