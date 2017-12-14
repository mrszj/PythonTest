#coding=utf-8
import sys
from selenium import webdriver
import logging
import time
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
def login_mailSina(username,passwd,to,title,text):
    #登录
    cus_profile = webdriver.FirefoxProfile(r'C:\Users\szj\AppData\Roaming\Mozilla\Firefox\Profiles\selenium3')
    browser = webdriver.Firefox(cus_profile)
    browser.implicitly_wait(15)
    browser.get('https://mail.qq.com')
    browser.switch_to.frame("login_frame")
    browser.find_element_by_id("switcher_plogin").click()
    browser.find_element_by_id("u").clear()
    browser.find_element_by_id("u").send_keys(username)
    browser.find_element_by_id("p").clear()
    browser.find_element_by_id("p").send_keys(passwd)
    browser.find_element_by_id("login_button").click()

    #发送邮件
#    browser.switch_to.frame("Top Window")
#   browser.switch_to.default_content()
    browser.switch_to.default_content()
    browser.find_element_by_id("composebtn").click()
    browser.switch_to.frame("mainFrame")
    browser.find_element_by_xpath("html/body/form[2]/div[2]/div[3]/div[2]/table[2]/tbody/tr/td[2]/div[1]/div[2]/input").send_keys(to)
    browser.find_element_by_id("subject").send_keys(title)
    time.sleep(2)
    browser.find_element_by_class_name("qmEditorIfrmEditArea").send_keys(text)
    time.sleep(2)
    browser.find_element_by_link_text(u'发送').click()
    browser.quit()

login_mailSina('2399090338','bokezhidi',sys.argv[1],sys.argv[2],sys.argv[3])
