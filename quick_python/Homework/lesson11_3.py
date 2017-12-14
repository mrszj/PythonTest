#coding=utf-8
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
import time
from selenium.webdriver.common.keys import Keys

logging.basicConfig(level=logging.WARNING,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
def play_2048():
    #登录
    cus_profile = webdriver.FirefoxProfile(r'C:\Users\szj\AppData\Roaming\Mozilla\Firefox\Profiles\selenium3')
    browser = webdriver.Firefox(cus_profile)
    browser.implicitly_wait(15)
    browser.get('https://gabrielecirulli.github.io/2048/')
    browser.find_element_by_link_text("New Game").click()
    play_ele = browser.find_element_by_class_name("game-container")
    while True:
        play_ele.send_keys(Keys.UP)
        play_ele.send_keys(Keys.RIGHT)
        play_ele.send_keys(Keys.DOWN)
        play_ele.send_keys(Keys.LEFT)
        if (browser.find_element_by_class_name("retry-button").text == "Try again"):
            time.sleep(3)
            browser.find_element_by_link_text("New Game").click()
            continue

play_2048()