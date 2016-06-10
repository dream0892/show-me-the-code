from bs4 import BeautifulSoup
import pdb
import re
import pyexcel
f=open('../fee_talk.html')
html_doc=f.read()
soup=BeautifulSoup(html_doc,"lxml")
m=soup.find(colspan=re.compile(r'\d'))
title=[]
content=[]
item=[]
talk_time=0
if 'colspan' in m.attrs:
    column=m.attrs['colspan']
for i in soup.find_all('th'):
    if not 'colspan' in i.attrs:
        title.append(i.text)
for i in soup.find_all('td'):
        content.append(i.text)


for j in range(0,len(content)//int(column),7):   
    item.append(content[j:j+7])
    #item.append(title)
sheet=pyexcel.get_sheet(array=item)
sheet.save_as('talk.xls')
for j in item:
    if re.search('主叫',j[2]):
        h,m,s=j[4].split(':')
        talk_time=talk_time+int(h)*3600+int(m)*60+int(s)
print(talk_time,'sec')   
