# 지구에서 가장 가까운 별은 프록시마 켄타우리라는 별이다.
# 프록시마 켄타우리는 지구로부터 40 * 10의 12승 Km 떨어져 있다.
# 빛의 속도로 이 별에 간다면 시간이 얼마나 걸리는지 계산하는 프로그램

from math import *

# 빛의속도 값 저장
light_speed = 300000
distance = 40 * pow(10,12)

seconds = distance / light_speed
print(f"걸리는 시간(초) : {seconds}")
light_year = seconds/(60 * 60 * 24 * 365)
print(f"걸리는 년도 : {light_year}")
# 정수 10과 실수 10.0은 동일하다
print(10 == 10.0)
# 문자열 '10'과 실수 10.0은 완전히 다른것으로 인식한다
print('10' == 10.0)
