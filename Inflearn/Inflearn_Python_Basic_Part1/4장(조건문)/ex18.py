# 주사위 눈을 랜덤으로 발생시켜 해당하는 숫자를 출력하는 프로그램 만들기
# randint() 함수를 검색하여 사용법 익힌 후 프로그램 출력

from random import *

# # random() 함수는 0.0 부터 1.0 미만의 임의의 값을 float 형태로 반환해주는 함수
# num = random()
# print("num : ",num)
# # randrange(start,stop,step) 함수는 start부터 stop사이의 step의 값에 따라 임의의 수를 반환해주는 함수
# # randrange(a)함수는 0부터 a 미만까지 임의의 정수값 반환
# num = randrange(1,101,2)
# print("num : ",num)

# randint(a,b) 함수는 a부터 b 사이의 임의의 정수를 반환하는 함수
num = randint(1,6)
# print("주사위 눈 : {}".format(num))

if num == 1:
    print(f"주사위 눈 : {num}")
elif num == 2:
    print(f"주사위 눈 : {num}")
elif num == 3:
    print(f"주사위 눈 : {num}")
elif num == 4:
    print(f"주사위 눈 : {num}")
elif num == 5:
    print(f"주사위 눈 : {num}")
else:
    print(f"주사위 눈 : {num}")
