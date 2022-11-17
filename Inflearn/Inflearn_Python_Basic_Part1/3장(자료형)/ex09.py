# 파이썬에서의 자료형(Data-type)

# int형 출력
print(type(17))

# float형 출력
print(type(10.77779))

# str형 출력
print(type("하이"))

# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
# 반지름이 5인 구의 부피를 계산하는 프로그램
from math import *
r = 5.0
volume = 4.0/3.0 * pi * r ** 3
#volume = 4.0/3.0 * pi * r ** pow(r, 3)
print(f" 구의 부피 : {volume}")
# print(pi)

# 구의 겉넓이 공식 : 4 * pi * r의 제곱
outer_area = 4 * pi * pow(r,2)
print(f"구의 겉넓이 : {outer_area}")