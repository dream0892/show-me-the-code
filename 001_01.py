#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
# uuid取前20位
import string
import uuid

KEY_LEN = 20
KEY_ALL = 200

def key_num(num, result=None):
    
    if result is None:
        result = []
    for i in range(num):
	tmp_key=str(uuid.uuid1()).replace("-","")[:KEY_LEN]
        result.append(tmp_key)
    return result


def print_key(num):
    f = open('Activation_code.txt', 'wt')
    for i in key_num(num):
        print(i)
        #print(type(i))
        f.write(i + '\n')
    f.close()


if __name__ == "__main__":
    print_key(KEY_ALL)
