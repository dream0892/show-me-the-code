from PIL import Image, ImageOps
import os, os.path
from collections import Counter
import re
import nltk
def create_list(filename):
    datalist = []
    with open(filename, 'r') as f:
        for line in f:
            content = re.sub(r"[\"|,|\.|\;|0-9]+", " ", line)
            if content.strip() !="":    #防止空字符串加入列表
                #使用NLTK的STOPWORDS过滤无意义词组
                datalist.extend(myword for myword in re.split(r'\s+',content.strip()) if not myword in nltk.corpus.stopwords.words('english'))          
    return datalist


def wc(filename):
    print('the %s keywords is:' % filename)
    print(Counter(create_list(filename)).most_common(10))
    #print(create_list(filename))
    print('---------------------------------------------------------------------------------------------------------------')
def keywords_show(dirname):
    if os.path.exists(dirname):
        L = [ x for x in os.listdir(dirname) if os.path.splitext(x)[1].lower()=='.txt' ] 
    for f in L:
        wc(os.path.join(dirname,f))
if __name__ == "__main__":
    dirname = 'diary'
    keywords_show(dirname)