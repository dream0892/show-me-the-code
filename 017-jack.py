# -*- coding:utf-8 -*-
#sheet.to_dict()有bug，有时间需要调试一下
import xml.etree.ElementTree as ET
import json
import pyexcel
import pdb
import logging
sheet=pyexcel.get_sheet(file_name='student.xlsx')
sheet.transpose()
sheet.name_columns_by_row(0)
st_dict=pyexcel.utils.to_dict(sheet)
root=ET.Element('root')
students=ET.SubElement(root,'students')
students.append(ET.Comment(u'''学生信息表 ‘id':［名字，数学，语文，英语］'''))
print(st_dict)
students.text=json.dumps(st_dict,ensure_ascii=False,indent=4)

st_xml=ET.ElementTree(root)
st_xml.write('student.xml',  xml_declaration=True, encoding='utf-8')