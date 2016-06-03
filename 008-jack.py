from bs4 import BeautifulSoup
import requests

html_doc=requests.get('http://www.baidu.com')
print(type(html_doc))
soup=BeautifulSoup(html_doc.text,'html.parser',from_encoding='utf-8')
f=open('test.html','wt')
f.write(soup.body.text)