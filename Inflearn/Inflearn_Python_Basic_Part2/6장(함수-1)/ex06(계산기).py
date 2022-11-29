# 간단한 사칙연산 계산기 만들기

def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return round((n1/n2), 2)

temp = "Y"

while True:
    if temp == "N":
        break
    elif temp == "Y":
        n1 = float(input("숫자 입력 : "))
        n2 = float(input("숫자 입력 : "))
        op = input("원하는 연산 입력(+, -, *, /) : ")
        # 연산자 분기점
        if op == "+":
            print(f"{n1}+{n2} = {add(n1,n2)}")
        elif op == "-":
            print(f"{n1}-{n2} = {sub(n1,n2)}")
        elif op == "*":
            print(f"{n1}*{n2} = {mul(n1,n2)}")
        elif op == "/":
            print(f"{n1}/{n2} = {div(n1,n2)}")
        else:
            print("잘못된연산자이다.")
    temp = input("계속하시겠습니까? (Y/N) : ")
