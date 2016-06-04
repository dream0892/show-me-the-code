#!/usr/bin/env python
# -*-coding:utf-8-*-

# 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数
# 过滤了多个空格以及标点符号还有数字，可以显示每个单词的使用次数
from collections import Counter
import re


def creat_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub(r"[\"|,|\.|\;|0-9]+", " ", line)
            datalist.extend(re.split(r'\s+',content.strip()))          
    return datalist


def wc(filename):
    print(Counter(creat_list(filename)))

if __name__ == "__main__":
    filename = 'test.txt'
    wc(filename)