# for 문 이용하여 팩토리얼(factorial)을 계산하는 프로그램 작성
# 팩토리얼은 n! 은 1부터 n 까지의 정수의 모두 곱한것을 의미함
# f(1) = 1 이다.

def fac(n):
    fact = 1.0
    #n = int(input("팩토리얼 값을 구할 정수 입력 : "))
    num=n

    for i in range(1, num+1):
        fact *= i # fact = fact * i 를 복합 대입연산자를 사용함

    print(n,"!은", fact,"입니다.")

# fac(7)

from math import factorial
def fact(n):
    # answer = 1
    # fac = 1
    # while fac <= n:
    #     print(f"{fac}가 {n}보다 작을때 answer은 {answer}")
    #     answer +=1
    #     print(f"answer에 +1하여 {answer}, fac는 {fac}")
    #     fac = fac * answer
    #     print(f"fac에다 fac*answer 하여 fac는 {fac}")
    #     print()
    # answer = answer-1

    # return answer
    answer=10
    while n < factorial(answer):
        print(f"n = {n}, factorial = {factorial(answer)}, answer={answer}")
        answer -=1
    return answer
print(fact(3628800))