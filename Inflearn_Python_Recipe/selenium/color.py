from selenium import webdriver
from pprint import pprint
import time
from collections import Counter

opt = webdriver.ChromeOptions()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    'Inflearn_Python_Recipe/selenium/chromedriver', options=opt)
driver.get('http://zzzscore.com/color')
driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
# print(len(btns))


def analysis():

    btns_rgba = [btn.value_of_css_property('background-color') for btn in btns]
    # pprint(btns_rgba)

    result = Counter(btns_rgba)
    pprint(result)  # 여기서 val이 1인게 정답

    # val이 1인것 탐색
    for k, v in result.items():
        if v == 1:
            answer = k
            break
    else:
        answer = None
        print("정답 없음")

    # 정답 클릭
    # 1. btns_rgba에서 인덱스 값을 비교
    # 2. 그 인덱스 값으로 btns 인덱스에 접근. 클릭
    if answer:
        index = btns_rgba.index(answer)
        btns[index].click()

## 메인 부분
start = time.time()
while time.time() - start <= 60:
    print("되냐?")
    analysis()
    print("맞냐?")