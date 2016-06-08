# -*- coding: utf-8 -*-
# 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
import json
import pyexcel
import pdb
f=open('numbers.txt')
d_student=json.load(f)
#pdb.set_trace()
sheet=pyexcel.get_sheet(array=d_student)
sheet.name='student'
sheet.transpose()
sheet.save_as('numbers.xls')