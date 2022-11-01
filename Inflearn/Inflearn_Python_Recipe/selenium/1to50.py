from selenium import webdriver

opt = webdriver.ChromeOptions()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    'Inflearn_Python_Recipe/selenium/chromedriver', options=opt)
driver.get('http://zzzscore.com/1to50')
driver.implicitly_wait(300)

# 전역 변수
# 현재 찾아야 될 숫자
num = 1

def clickBtn():
    global num
    btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')  # div[*]을 통해 패턴을 인식

    for btn in btns:
        print(btn.text, end='\t')
        if btn.text == str(num):
            btn.click()
            print(True)
            num+=1
            return
# 메인코드
while num <=50:
    clickBtn()