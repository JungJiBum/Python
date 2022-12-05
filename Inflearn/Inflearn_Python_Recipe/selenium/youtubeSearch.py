from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver')
driver.get("https://youtube.com")

time.sleep(3)

search = driver.find_element_by_xpath('//input[@id="search"]')
# search = driver.find_element_by_name("search_query")

search.send_keys('반원코딩')
time.sleep(1)

search.send_keys(Keys.ENTER)


# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(크롬드라이버 경로)
# driver.get(링크)
