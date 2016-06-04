#!/usr/local/bin/python
#coding=utf-8

"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""
import re

def count_the_words(path):
    with open(path) as f:
        text = f.read()
        words_list = re.findall(r'[a-zA-Z]+', text)
        count = list(words_list)
    return count

if __name__ == '__main__':
    nums = count_the_words('test.txt')
    print(nums)