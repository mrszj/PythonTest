#coding=utf-8
import shutil,os,sys

#9.1 编写一个程序,遍历一个目录树,查找特定扩展名的文件(注入.pdf或.jpg).不论这些文件的位置在哪里,将他们拷贝到一个新的文件夹中
def mv_new(oldpath,newpath,suffix):
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    for folderName,subFolders,fileNames in os.walk(oldpath):
        for fileName in fileNames:
            if os.path.splitext(fileName)[1] == suffix:
                shutil.move((folderName+'/'+fileName), newpath)
mv_new(r'D:\360Downloads',r'd:\new','.jpg')

#9.2delete 100MB file
def del_x(fpath,fsize): #fsize MBytes
    for folderName,subFolders,fileNames in os.walk(fpath):
        for fileName in fileNames:
            filepath = os.path.join(folderName,fileName)
            if os.path.getsize(filepath) > (fsize*1024*1024):
                print filepath
        
del_x(r'd:\new',100)

#9.3消除缺失的编号
def L9831(fpath,prefixa):
    os.chdir(fpath)
    f=1
    s_f='%s%03d.txt' %(prefixa,f)
    for fileName in os.listdir(fpath):
        print(fileName+' now is ')
        if fileName != s_f:
            print('%s is loss')%s_f
            try:
                shutil.move(fileName, s_f)
            except:
                continue
            f=f+1
            s_f='%s%03d.txt' %(prefixa,f)
            continue
        f=f+1
        s_f='%s%03d.txt' %(prefixa,f)
L9831(r'd:\l983','spam')