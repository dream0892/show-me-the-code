# -*- coding:utf-8 -*-
#sheet.to_dict()有bug，有时间需要调试一下
import xml.etree.ElementTree as ET
import json
import pyexcel
import pdb
import logging
sheet=pyexcel.get_sheet(file_name='numbers.xls')
sheet.transpose()
#sheet.name_columns_by_row(0)
#st_dict=pyexcel.utils.to_dict(sheet)
st_dict=sheet.to_array()
root=ET.Element('root')
students=ET.SubElement(root,'numbers')
students.append(ET.Comment(u'''-----数字信息-----'''))
print(st_dict)
students.text=json.dumps(st_dict,ensure_ascii=False,indent=4)

st_xml=ET.ElementTree(root)
st_xml.write('numbers.xml',  xml_declaration=True, encoding='utf-8')