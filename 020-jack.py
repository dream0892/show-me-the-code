from bs4 import BeautifulSoup
import pdb
import re
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

#item.append(title)
m=0
for j in range(len(content)//int(column)):   
    item.append(content[m:m+7])
    m=m+7
#pdb.set_trace()
for j in item:
    if re.search('主叫',j[2]):
        h,m,s=j[4].split(':')
        talk_time=talk_time+int(h)*3600+int(m)*60+int(s)
print(talk_time,'sec')   
