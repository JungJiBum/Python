# 피보나치 수열의 함수만 선언 및 구현 -- 모듈의 형태
'''
모듈의 정의 : 함수나 변수들을 모아놓은 파일
모듈이란 자주 사용될 것으로 예상되는 함수들을 선언 및 구현으로 정의 해놓은 파일
타 프로그램에서 import 키워드로 다른 실행파일에 도움을 주는 형태의 파일
'''
# def fib(n):
#     a,b = 0,1
#     while b < n:
#         print(b, end=' ')
#         a,b = b, a+b
#     print()

def fib(n):
    n1 = 0
    n2 = 1 
    n3 = n1 + n2
    while n3 < n:
        print(n3, end=' ')
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print()

# 1 ~ n 까지의 합계를 구하는 함수
def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
