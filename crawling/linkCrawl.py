from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs

#옵션 세팅
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log_level3')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

url = "http://www.youtube.com"
# driver = webdriver.Chrome("D:\코딩테스트연습\CODINGTEST_python\chromedriver.exe");
driver = webdriver.Chrome("python\crawling\chromedriver.exe",options=chrome_options)
driver.get(url);

# beautifulSoup로 크롤링 수행
html = driver.page_source
soup = bs(html, 'html.parser'); # parser를 이용하여 parsing 진행
aa = soup.select('#thumbnail') # 해당 유투브 url 링크 정보 입니다.


for a in aa:
    # print(a.attrs)
    k = a.attrs.keys()
    v = a.get('class')  
    l = a.get('href')
    print(f"ID = {v} / link = {l}")
    # keys = a.attrs.keys();
    # value = a.get('href')
    # print("link : ", value);
