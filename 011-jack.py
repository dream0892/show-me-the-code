#过滤敏感词
import re
f=open('filter_words.txt','rt')
fword=[]
for line in f:
    fword.append(line.strip())
def out_print(str,filterword):
    freedom = False
    for i in filterword:
        if re.search(i,str):
            freedom=True
    return freedom

if out_print('我在看电视',fword):
    print('freedom')
else:
    print('humanright')