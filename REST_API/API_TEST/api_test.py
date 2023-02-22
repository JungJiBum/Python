# 공공데이터 포털에서 API를 가지고 연결하는 과정
import requests
from pprint import pprint

url = 'http://apis.data.go.kr/3330000/HeaundaeCctvInfoService/getCctvList'
# params ={'serviceKey' : 'qhTuKPsoFxyb7Bepg5ZlzZBFwFCcyLwD71AP/i8ej3jHHWrOCXIbEA0Pku9qMtYEv5OGM1WEtRvN3ihmhYDTUg==', 'pageNo' : '1', 'numOfRows' : '10', 'area' : '광운빌라인근', 'resultType' : 'json' }
params ={'serviceKey' : 'qhTuKPsoFxyb7Bepg5ZlzZBFwFCcyLwD71AP/i8ej3jHHWrOCXIbEA0Pku9qMtYEv5OGM1WEtRvN3ihmhYDTUg=='}
response = requests.get(url, params=params)


text = response.content.decode('utf-8')
pprint(text)

