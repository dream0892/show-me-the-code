from bs4 import BeautifulSoup
from urllib import request
import ssl
import pdb
import re
#m=re.search(r'[0-9a-z]+\.jpg', test_odc).group(0)
#print('http://imgsrc.baidu.com/forum/pic/item/%s' % m.strip())
bd_img_url='http://imgsrc.baidu.com/forum/pic/item/'  #这是贴吧大图地址
ssl._create_default_https_context = ssl._create_unverified_context
mydata=request.urlopen('http://tieba.baidu.com/p/2166231880').read()
soup=BeautifulSoup(mydata,'html.parser')
#pdb.set_trace()
for soup_item in soup.find_all('img',class_='BDE_Image'):
        jpg_url=soup_item['src']
        jpg_add=re.search(r'[0-9a-z]+\.jpg', jpg_url).group(0)
        jpg_add=bd_img_url+jpg_add
        print(jpg_add)
