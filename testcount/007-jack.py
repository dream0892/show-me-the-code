
import os
import re
#import pdb
CODE_PATH = os.path.join('.','testcount')
#pdb.set_trace()
'''
        这是大块的注释，用来测试是不是好用
        re.match(r'^[[\s\t]*[\'\'\']|[\s\t]*[\"\"\"]].line)
'''
#匹配需要换成正则匹配
code_files = []
code_line_count = 0
code_blank_line_count = 0
code_comment_line_count = 0
code_comment_block_count = 0

def walk(rootDir):
    code_files=[]
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if os.path.isdir(path):
            walk(path)
        else:
            if os.path.splitext(lists)[1].upper() == '.PY':
                code_files.append(path)
    return code_files


for code_file in walk(CODE_PATH):
    file = open(code_file,'rt', encoding='gbk', errors='ignore')
    g_comment=0
    for line in file:
        if not g_comment:
            if line.strip() == '\n' or line.strip() == '':
                code_blank_line_count += 1
            elif line.replace(' ', '').replace('\t', '')[0] == '#':
                code_comment_line_count += 1
            #elif line.replace(' ', '').replace('\t', '')[:3] == '\'\'\'':
            elif  re.match(r'^[[\s\t]*[\'\'\']|[\s\t]*[\"\"\"]]',line):
                code_comment_block_count+=1
            else:
                code_line_count += 1
        else:
            if line.replace(' ', '').replace('\t', '')[:3] == '\'\'\'':
                g_comment=0
            code_comment_block_count+=1


print ('文件数量：', len(walk(CODE_PATH)))
print ('代码行数：', code_line_count)
print ('空行行数：', code_blank_line_count)
print ('注释行数:', code_comment_line_count)
print ('注释块数:', code_comment_block_count)