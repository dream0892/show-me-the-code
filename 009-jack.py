#取出HTML中的所有连接地址 

from bs4 import BeautifulSoup
import requests

html_doc=requests.get('http://www.sohu.com')
print(type(html_doc))
soup=BeautifulSoup(html_doc.text,'html.parser',from_encoding='GBK')
f=open('test.html','wt')
for link in soup.find_all('a'):
	f.write(str(link.get('href'))+'\n')
f.close()