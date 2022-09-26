import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs

#옵션 세팅
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log_level3')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
# 크롬드라이버 사용하여 url 접속
driver = webdriver.Chrome("python\crawling\chromedriver.exe",options=chrome_options)
# driver = webdriver.Chrome("python\crawling\chromedriver.exe")
link = "http://www.youtube.com"
driver.get(url=link)

# media_name = driver.find_elements_by_css_selector("#contents")
# media_name = driver.find_elements_by_css_selector("#video-title-link")
# media_name = driver.find_elements_by_css_selector("#meta > h3")
media_name = driver.find_elements_by_css_selector("#video-title")

ls = []
for i in media_name:
    ls.append(i.text)
for i in ls:
    # i = i.replace(" ","")
    print(i)