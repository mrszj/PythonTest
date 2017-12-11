#coding=utf-8
import  os
import zipfile
import traceback
import logging
import webbrowser,pyperclip
import requests

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
    
logging.debug('Start of program')

address = ''.join(pyperclip.paste())

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))
print(res.status_code)
print(len(res.text))
print(res.text[:250]) 






logging.debug('End of program')