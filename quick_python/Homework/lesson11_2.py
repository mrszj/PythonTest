#coding=utf-8
import sys
from selenium import webdriver
import logging,requests,os,bs4
import time
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.WARNING,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
'''图像网站下载
    编写一个程序,访问图像共享网站,查找一个类型的图片,然后下载所有查询结果的图像'''
url = "https://stock.tuchong.com/search?term="
search_key ='美女'
os.makedirs("d:\\lesson11_2",exist_ok=True)
print('Downloading page %s...' %url)
res = requests.get(url+search_key)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
dElements =soup.select('img')
for dElement in dElements:
    if dElement == []:
        print('找不到图片')
    else:
        dUrl=dElement.get('src')
        print('Downloading image %s...' %dUrl)
        res = requests.get(dUrl)
        res.raise_for_status()
        imageFile = open(os.path.join("d:\\lesson11_2",os.path.basename(dUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()