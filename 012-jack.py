#敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」
import re
f=open('filter_words.txt','rt')
fword=[]
for line in f:
    fword.append(line.strip())
def out_print(str,filterword):
    freedom = False
    for i in filterword:
        str=str.replace(i,'*'*len(i))
    return str

print(out_print('我在北京看电视',fword))