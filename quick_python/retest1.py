import  re
import sys
from selenium import webdriver
print(re.subn('\d','aa','aab2bcc1xx'))
print(re.finditer('\d','2aab2bcc1xx'))
print(re.search('\d','2aab2bcc1xx'))
print(sys.path)
browser=webdriver.Firefox()
url="https://192.168.16.113/userMainAction.action"
browser.get(url)
browser.find_element_by_id("username").send_keys("admin")
browser.find_element_by_id("password").send_keys("topwalkadmin")
