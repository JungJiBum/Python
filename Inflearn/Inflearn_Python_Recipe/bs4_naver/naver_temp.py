from bs4 import BeautifulSoup as bs
#리스트나 딕셔너리의 데이터가 엄청 길 경우 편하게 보여주는 용도로 사용
from pprint import pprint
#웹 페이지에 요청을하는 용도
import requests

html = requests.get('https://search.naver.com/search.naver?query=날씨')
# pprint(html.text)

soup = bs(html.text,'html.parser')
# pprint(soup)
'''
HTML 요소
태그 : div
속성 : class
속성값 : detail_box
속성값은 여러개를 가질수 있음
'''
data1 = soup.find('div',{'class':'_weekly_weather'})    # 영역 추출
# pprint(data1)

data2 = data1.findAll('li') #data1영역안에서 li 태그를 가지고 있는 결과만 findAll
# pprint(len(data2))  #길이는 10
# pprint(data2[0])
'''
<li class="week_item today"> <div class="day_data"> <div class="cell_date"> <span class="date_inner"> <strong class="day">오늘</strong>
<span class="date">9.19.</span> </span> </div>
<div class="cell_weather"> <span class="weather_inner"> <span class="weather_left"> <strong class="time">오전</strong>
<span class="rainfall">0%</span> </span> <i class="wt_icon ico_wt1"><span class="blind">맑음</span></i> </span>
<span class="weather_inner"> <span class="weather_left"> <strong class="time">오후</strong> <span class="rainfall">10%</span>
</span> <i class="wt_icon ico_wt1"><span class="blind">맑음</span></i> </span> </div>
<div class="cell_temperature"> <span class="temperature_inner"> <span class="lowest"><span class="blind">최저기온</span>21°</span>
<span class="bar">/</span> <span class="highest"><span class="blind">최고기온</span>28°</span> </span> </div> </div> </li>
'''

# .text를 통해 텍스트 값만 도출
find_dust = data2[0].find('span',{'class':'temperature_inner'}).text #data2[0]번의 값에서 span 태그의 temperature_inner 클래스 값 조회
pprint(find_dust)