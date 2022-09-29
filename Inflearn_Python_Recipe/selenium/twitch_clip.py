from time import time
from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver', options=opt)
driver.get("https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie")

time.sleep(3)

'''
f12 -> element 서치 -> find (video>) -> src
'''
# video 태그 확인
url_element = driver.find_element_by_tag_name('video')
vid_url = url_element.get_attribute('src')
print(vid_url)