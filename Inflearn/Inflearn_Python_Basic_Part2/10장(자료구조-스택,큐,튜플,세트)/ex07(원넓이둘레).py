# 문제 : 원의 넓이와 둘레를 동시에 반환하는 함수
# 반지름은 사용자 입력
'''
출력 결과
원의 반지름을 입력하시오 : 10
원의 넓이는 314.15926533589793 이고 원의 둘레는 62.83185307179586이다.
'''
import math

def caclCircle(radius):
    # 원 넓이
    area = math.pi * radius * radius
    # 원 둘레
    circumstance = 2 * math.pi * radius
    # 값을 다중으로 넘기고 싶을때 튜플 사용
    return (area, circumstance)

if __name__ == "__main__":
    radius = float(input("원의 반지름을 입력하시오 : "))
    # 함수 리턴타입이 튜플이니 저장하기 위해 튜플로 반환 값을 저장
    (area, circumstance) = caclCircle(radius)
    print("원의 넓이는 {} 이고 원의 둘레는 {} 이다.".format(area, circumstance))

