from pprint import pprint
from bs4 import BeautifulSoup
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = BeautifulSoup(html.text,'html.parser')
html.close()

def title_print():
    data1 = soup.findAll('a',{'class':"title"})
    week_title_list= [t.text for t in data1]
    pprint(week_title_list)

title_print()