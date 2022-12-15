# 무명함수(익명함수, anonymous function)에 대한 실습
'''
무명함수는 함수명이 없고, 구현부만 존재
파이썬에서는 lambda 키워드로 무명함수를 만듦
무명함수는 print()등과 같은 일반함수를 호출할 수 없다. 오직 계산만 가능
전역변수를 참조할 수 없음
'''
# lambda 인수1, 인수2 : 수식 <-- 문법
# lambda x = 10, y : x+y --> 람다함수는 변수에다 값을 할당할 수 없음

def main():
    print("두 정수의 합 : ",get_sum(10,50))
    print("두 정수의 합 : ",get_sum(100,500))
    
    # lambda 키워드를 이용한 sum() 만들기
    # 람다 함수는 코드안에 함수를 포함하는 어느 곳이든 다 사용 가능하다.
    # 가장 많이 사용되는 곳은 GUI 프로그램에서 이벤트를 처리하는 콜백 함수 형태로 많이 쓰임
    sum = lambda x, y : x+y
    print("람다식을 이용한 함수명 sum() 결과 : ",sum(10,50))
    print("람다식을 이용한 함수명 sum() 결과 : ",sum(10,500))
    # 람다식으로 구성되어진 리스트 데이터
    li = [ lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4  ]
    for f in li:
        print(f(10))

    print(lambda x,y : x + y) # --> 람다 함수를 출력하면 결과론으로 함수객체를 출력하는 형태가 됨
    print((lambda x,y : x + y)(60,50)) # --> 실질적 람다식을 이용한 무명함수를 직접 호출한 형태

# 일반적인 함수
def get_sum(x,y):
    return x+y

main()