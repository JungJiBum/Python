from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome('selenium\chromedriver')
driver.get("https://www.youtube.com")

time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="search-input"]')

search.send_keys("반원 코딩")
time.sleep(1)

search.send_keys(Keys.ENTER)