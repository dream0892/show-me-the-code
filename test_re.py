import re
test_odc='http://imgsrc.baidu.com/forum/w%3D580%3Bcp%3Dtieba%2C10%2C357%3Bap%3D%C9%BC%B1%BE%D3%D0%C3%C0%B0%C9%2C90%2C365/sign=9f2ea944ae51f3dec3b2b96ca4d5936f/5de7a5b7d0a20cf433959f5177094b36adaf999f.jpg'
test_tmp='abc/jpg'
m=re.search(r'[0-9a-z]+\.jpg', test_odc).group(0)
print('http://imgsrc.baidu.com/forum/pic/item/%s' % m.strip())