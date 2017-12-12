#coding=utf-8
import  os
import zipfile
import shelve
import shutil


os.chdir(r'..')
for folderName,subfolders,filenames in os.walk(os.getcwd()):
    print('当前文件夹是:'+folderName)
    for subfolder in  subfolders:
        print(folderName+'的子文件夹:'+subfolder)
    for filename in filenames:
        print(folderName+'中的文件'+filename)
    print('')
