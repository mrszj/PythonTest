#coding:utf-8
import subprocess
import time
from PIL import Image
from PIL import ImageOps
from selenium import webdriver
from pytesseract.pytesseract  import  image_to_string


'''python版本：3.4.3
所需要的代码库：PIL，selenium，tesseract,pytesseract
'''

def cleanImage(imagePath):
    image = Image.open(imagePath)   #打开图片
    image = image.point(lambda x: 0 if x<143 else 255)  #处理图片上的每个像素点，使图片上每个点“非黑即白”
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)


def getAuthCode(driver, url):
    time.sleep(5)
    driver.refresh()
    driver.save_screenshot("captcha.png")   #截屏，并保存图片
    #urlretrieve(captchaUrl, "captcha.png")
    time.sleep(0.5)
#    im = driver.find_element_by_xpath(".//*[@id='from']/ul/li[3]/span[2]/img")
    im = driver.find_element_by_class_name("img")
    print('im',im)
    left = im.location['x']
    top = im.location['y']
    right = left + im.size['width']
    bottom = top + im.size['height']
    print(left,top,right,bottom)
    imp = Image.open("captcha.png")
    myim = imp.crop((int(left),int(top),int(right),int(bottom)))
    myim.save("captcha.png")
    cleanImage("captcha.png")

    print image_to_string(Image.open("captcha.png"))

    # p = subprocess.Popen(["tesseract", "captcha.png", "captcha.txt"], stdout= subprocess.PIPE,stderr=subprocess.PIPE)
    # p.wait()
    # f = open("captcha.txt", "r")
    #
    # #Clean any whitespace characters
    # captchaResponse = f.read().replace(" ", "").replace("\n", "")
    #

    # print("Captcha solution attempt: " + captchaResponse)
    # print(captchaResponse)
    # if len(captchaResponse) == 4:
    #     return captchaResponse
    # else:
    #     return False
    return image_to_string(Image.open("captcha.png"))

def withoutCookieLogin(driver,url):
#    driver.maximize_window()
    driver.get(url)
    while True:
        authCode = getAuthCode(driver, url)
        if authCode:
            driver.find_element_by_id("username").clear()
            driver.find_element_by_id("username").send_keys("admin")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("topwalkadmin")
            driver.find_element_by_id("captcha").send_keys(authCode)
            try:
                time.sleep(3)
                driver.find_element_by_class_name("butn").click()
                return driver
            except:
                print("authCode Error:", authCode)
                driver.refresh()
    return driver


if __name__ == '__main__':
    profile=webdriver.FirefoxProfile()
    profile.accept_untrusted_certs=True
    driver=webdriver.Firefox(firefox_profile=profile)
    #driver=webdriver.Ie()
    
driver = withoutCookieLogin(driver,"https://192.168.16.63")
