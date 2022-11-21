# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니 무한루프 이용, 사용자가 "끝"이라고 입력을 하면 탈출하게 만들기.
'''
클래스 -> 객체
클래스의 구성요소는
1. 멤버 변수
2. 멤버 함수(메서드)
3. 생성자
'''
from operator import eq

total = 0
price = 0

while True:
    price = input("상품 금액을 입력하세요.(끝을 입력하면 종료됨) : ")
    #"끝"이라는 입력문구가 있는지 확인 하는 코드, 무한 루프 탈출하는 코드
    # if price =='끝':
    # if price.__eq__("끝"):
    if eq(price,"끝"):
        print("상품의 총 가격 : " + str(total)+"원!")
        break
    total += int(price)
