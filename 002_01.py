# -*- coding: utf-8 -*-

import mysql.connector

def store_mysql(filepath):
    conn = mysql.connector.connect(user = 'root', password = 'fjfh1so', database = 'test',host='127.0.0.1')
    cursor = conn.cursor()

    # 判断表是否已经存在
    cursor.execute('show tables in test;')
    tables = cursor.fetchall()
    findtables = False
    for table in tables:
        if 'code' in table:
            findtables = True
    if not findtables:
        cursor.execute('''
                CREATE TABLE `test`.`code` (
                `id` INT NOT NULL AUTO_INCREMENT,
                `code` VARCHAR(100) NOT NULL,
                PRIMARY KEY (`id`));
        ''')

    f = open(filepath, 'rt')
    for line in f.readlines():
        code = line.strip()
        cursor.execute("insert into test.code (code) values(%s);", [code])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    store_mysql('Activation_code.txt')
