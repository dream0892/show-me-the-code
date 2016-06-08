# -*- coding: utf-8 -*-
# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
import json
import pyexcel
import pdb
f=open('city.txt')
d_city=json.load(f)
#pdb.set_trace()
sheet=pyexcel.Sheet()
sheet.name='city'
for m,n in d_city.items():
    sheet.row+=[m,n]
#sheet.transpose()
sheet.save_as('city.xls')