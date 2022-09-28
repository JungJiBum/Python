import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])
link = "https://www.youtube.com"

# browser = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver',options=options)
browser = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver',options=options)
browser.get(url = link)

time.sleep(5)

search = browser.find_element_by_xpath('//*[@id="search"]')

# search = browser.find_element(By.CSS_SELECTOR, "#search")
# search = driver.find_elements(by=By.XPATH, value='//*[@id="search"]')
search.send_keys("반원 코딩")
time.sleep(3)

search.send_keys(Keys.ENTER)

