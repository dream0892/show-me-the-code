from bs4 import BeautifulSoup
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
mydata=request.urlopen('https://www.python.org/events/python-events/').read()
soup=BeautifulSoup(mydata,'html.parser')
for soup_item in soup.find_all('ul',class_='list-recent-events menu'):
    for soup_list in soup_item.find_all('li'):
       # print(soup_list.find('a').getText())
        print('会议名称：' ,soup_list.find('a').getText())
        print('会议时间' ,soup_list.find('time').getText())
        print('会议地点' , soup_list.find('span',class_='event-location').getText())
        print('----------------------------------------')
