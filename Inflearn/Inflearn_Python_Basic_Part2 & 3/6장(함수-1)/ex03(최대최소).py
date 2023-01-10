# 두개의 정수를 입력받아 더 큰수만 찾아서 큰 수를 리턴하는 함수 만들기
from calc import *

# def get_max(x,y):
#     temp = 0
#     if x > y:
#         temp  = x
#     else:
#         temp = y
#     return temp

num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
value = get_max(num1,num2)
print(f"{num1}과 {num2}중 큰 숫자값은?  {get_max(num1,num2)}")
print(f"{num1}과 {num2}중 큰 숫자값은?  {value}")


# 두 개의 정수를 입력받아 두 수 중 더 작은수를 찾아 작은 수를 리턴하는 함수 만들기

# def get_min(x,y):
#     temp = 0
#     if x > y:
#         temp = y
#     else:
#         temp = x
#     return temp

num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))
value = get_min(num1,num2)
print(f"{num1}과 {num2}중 작은 숫자값은?  {get_min(num1,num2)}")
print(f"{num1}과 {num2}중 작은 숫자값은?  {value}")


# 거듭 제곱 구하기
num1 = int(input("제곱 대상 숫자 : "))
num2 = int(input("제곱 횟수 숫자 : "))
value = power(num1,num2)
print(f"{num1}과 {num2}중 거듭 제곱 값은?  {value}")