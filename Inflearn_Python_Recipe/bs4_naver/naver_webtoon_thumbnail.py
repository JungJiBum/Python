import errno
from pprint import pprint
from bs4 import BeautifulSoup
import requests, re, os
from urllib.request import urlretrieve

# 저장 폴더 생성
try:
    if not(os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text,'html.parser')
html.close()

data1_list = soup.findAll('div',{"class":"col_inner"})

li_list=[]
for data1 in data1_list:
    # 제목 + 썸네일 영역 추출
    li_list.extend(data1.findAll('li'))

# pprint(li_list)

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-zㄱ-힗]', '', title) # 해당 영역의 글자가 아닌 것은 ' '로 치환시킨다.
    # print(title, img_src)
    urlretrieve(img_src,'./image/'+title + '.jpg')

