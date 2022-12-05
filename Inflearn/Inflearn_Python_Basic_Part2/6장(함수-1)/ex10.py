# 구의 부피를 계산하는 함수 sphereVolume()를 작성하여 보자.
# 반지름을 사용자로부터 입력 받아 구의 부피를 구하는 함수 호출하라.
# 구의 부피 공식 : 4/3 * pi * r의 세제곱
import math

# 구의 부피를 구하는 함수 선언 및 구현
def sphereVolume(radius):
    volume = (4.0/3.0) * math.pi * math.pow(radius,3)
    return volume


radius = float(input("구의 반지름을 입력하세요 : "))
print(f"반지름이 {radius}인 구의 부피는 : {round(sphereVolume(radius),2)}")
