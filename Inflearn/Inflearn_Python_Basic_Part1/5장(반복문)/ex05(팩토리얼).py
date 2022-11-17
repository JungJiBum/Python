# for 문 이용하여 팩토리얼(factorial)을 계산하는 프로그램 작성
# 팩토리얼은 n! 은 1부터 n 까지의 정수의 모두 곱한것을 의미함
# f(1) = 1 이다.

fact = 1.0
n = int(input("팩토리얼 값을 구할 정수 입력 : "))

for i in range(1, n+1):
    fact *= i # fact = fact * i 를 복합 대입연산자를 사용함

print(n,"!은", fact,"입니다.")
