from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

opt = webdriver.ChromeOptions()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver', options=opt)
driver.get('http://zzzscore.com/color')
driver.implicitly_wait(300)

#전역 변수
#현재 찾아야될 숫자

start = time.time()

while time.time() - start <= 60:
    try:
        btn = driver.find_element_by_class_name("main")
        btn.click()
    except:
        pass