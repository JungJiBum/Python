import time
from matplotlib.pyplot import text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

link = #"웹주소"
log_id = #"계정"
log_pw = #비번

#옵션 세팅
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log_level3')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome("python\crawling\chromedriver.exe",chrome_options=chrome_options)
driver.get(url=link)

# 아이디 입력
driver.find_element_by_name("username").send_keys(log_id)
driver.find_element_by_name("password").send_keys(log_pw)
# 로그인 버튼
driver.find_element_by_xpath("/html/body/div[3]/md-content/form/div[1]/button").click()
# time.sleep(1)
# 경로 이동
driver.get("http://10.12.1.27/#/dashboard/U1lV")
# time.sleep(1)


cnt_plant = driver.find_elements_by_css_selector("#dashboardContentDiv > span") #해당 설비 제목부터 출력
plant_ls = []
speed_ls = []
length_ls = []

for i in cnt_plant:
    #반복문을 통해 텍스트값을 변수별로 나눠 입력 후 필요한 정보들만 리스트에 삽입
    name,b,c,d,line_Speed,f,speed_Val,h,take_Length,j,length_Val,l = i.text.split("\n")
    plant_ls.append(name+"설비")
    speed_ls.append(speed_Val+"(m/min)")
    length_ls.append(length_Val+"(m)")

df = pd.DataFrame(list(zip(plant_ls,speed_ls,length_ls)), columns=['설비명','속도','길이'])
print(df)