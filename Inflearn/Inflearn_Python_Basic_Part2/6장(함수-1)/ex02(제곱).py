# 정수를 사용자로부터 입력받아 제곱 값을 반환하는 함수
# 사용자가 5를 입력하면 출력값은 25가 되어야 한다.

from calc import square

# # 함수 선언
# def square(num):
#     temp = num * num
#     return temp # return값 처리

#함수 호출
num = int(input("제곱할 숫자 입력 : "))
print("제곱하기전 : ",num)
print("제곱한 후 : ",square(num))

    