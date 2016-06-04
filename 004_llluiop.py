#!/usr/bin.env python
#本方法没有将标点符号另算
import sys


def CalcWords():
    nums = 0
    f = open("english.txt", 'r')

    lines = f.readlines()
    for line in lines:
        for word in line.split():
            nums += 1

    return nums

#word for line in open('english.txt', 'r').readlines() for word in lines.split()

if __name__ == '__main__':
    #print CalcWords()
    print(len([x for lines in open('test.txt', 'r').readlines() for x in lines.split()]))