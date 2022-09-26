from pprint import pprint
from bs4 import BeautifulSoup
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text,'html.parser')
html.close()

# # 월요웹툰 영역 추출하기
# data1_list=soup.findAll('div',{'class':'col_inner'})
# # pprint(len(data1_list))

# # 전체 웹툰 리스트
# week_title_list=[]

# for data1 in data1_list:
# # 제목 영역 추출
#     data2 = data1.findAll('a',{'class':'title'})
#     # pprint(data2)
#     # text만 추출
#     # title_list=[]
#     # for t in data2:
#     #     title_list.append(t.text)
#     title_list = [t.text for t in data2]
#     # week_title_list.append(title_list)
#     week_title_list.extend(title_list)

    
# print(week_title_list)
# print(week_title_list[6])

def title_print():
    data1 = soup.findAll('a',{'class':"title"})
    week_title_list= [t.text for t in data1]
    pprint(week_title_list)

title_print()