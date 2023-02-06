from pprint import pprint
from bs4 import BeautifulSoup
import requests
import re
from io import BytesIO
from PIL import Image
import time

html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text,'html.parser')
html.close()
url = "comic.naver.com"
def title_print():
    data1 = soup.findAll('a',{'class':"title"})
    title = [t.text for t in data1]
    link = [url+t["href"] for t in data1]
    # for i in zip(title,link):
    #     print(i)
    ziplist = zip(title,link)
    pprint(list(ziplist))

# title_print()

def test():
    req = requests.get("https://comic.naver.com/webtoon/weekday")
    soup = BeautifulSoup(req.content,'html.parser')
    my_title = soup.findAll('a',{'class':"title"})
    # pprint(my_title)
    data = {}
    for title in my_title:
        data[title.text] = title.get('href')

    # for k,v in data.items():
    #     print("{} : {}".format(k,v))
    
    # for v in data.values():
    #     numbers = re.sub(r'[^0-9]','',v)
    #     print(numbers, v[-3:])
    
# https://comic.naver.com/webtoon/list?titleId={{article.title_numbers}}648419&weekday={{article.week}}mon
#content > div.list_area.daily_all > div.col.col_selected > div > ul > li:nth-child(1) > div > a > img
    dict={}
    img = soup.select('.thumb > a > img')
    for i in img:
        title = i.attrs.get("title")
        src = i.attrs.get('src')
        dict[title] = src
    pprint(dict)
    
    # for i in range(img):
    #     print()
    # for k,v in data.items():
    #     numbers = re.sub(r'[^0-9]','',v)
    #     # print(k, numbers, v[-3:])
    # return data
    
    #content > div.list_area.daily_all
#content > div.comicinfo > div.thumb > a > img

test()