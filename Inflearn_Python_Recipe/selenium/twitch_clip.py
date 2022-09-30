from time import time
from selenium import webdriver
import time

opt = webdriver.ChromeOptions()
opt.add_argument('headless') # 
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome('Inflearn_Python_Recipe/selenium/chromedriver', chrome_options=opt)
driver.get("https://www.twitch.tv/soorte214/clip/AgileGracefulCheesecakePeteZarollTie")

#활성화 시간 3초
time.sleep(3)

'''
f12 -> element 서치 -> find (video>) -> src
'''
# video 태그 확인
url_element = driver.find_element_by_tag_name('video')
# 속성을 구할때 .get_attribute를 사용함 / 가져올 속성명은 'src'
vid_url = url_element.get_attribute('src')
print(vid_url)

# 클립 제목과 날짜 확인
'''
#live-channel-stream-information > div > div > div.Layout-sc-nxg1ff-0.iQhdFE.metadata-layout__split-top > div.Layout-sc-nxg1ff-0
웹 코드가 맞지않아서 실행이 안됨
'''
# title_element1 = driver.find_element_by_class_name('CoreText-sc-cpl358-0 hzkHyc')
# title_element2 = title_element1.find_elements_by_tag_name('span')
# vid_title,vid_date = None, None

# for span in title_element2:
#     try:
#         d_type = span.get_attribute('data-test-selector')
#         if d_type == "title":
#             vid_title = span.text
#         elif d_type == 'date':
#             vid_date = span.text
#     except:
#         pass

driver.close()