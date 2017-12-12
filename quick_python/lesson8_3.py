#coding=utf-8
import os,re
ure = re.compile(r'\d\d\d')
uDir = '893'
for file in os.listdir(uDir):
    if os.path.splitext(file)[1] == '.txt':
        f = open(os.path.join(uDir,file))
        print('在文件'+f.name+'中查找:')
        for (num,value) in enumerate(f):
            if re.search(ure,value):
                print('第'+str(num+1)+'行'+' 内容为:'+value),
        print('\n'),