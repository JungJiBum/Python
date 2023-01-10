# 함수(function)에 대한 실습
'''
1. 함수는 프로그램 안에서 중복된 코드를 제거한다.
2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
3. 함수는 한번 만들어두면 재사용이 얼마든지 가능하다.
4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.
'''

# 간단한 함수
# def 키워드 함수이름(매개변수)
# hello 파일의 내용을 전부 다 가져온다.
# from hello import *
# 파일명.함수명으로 접근해야 한다.
import hello

hello.say_hello_name("지범")
hello.say_hello_name("BOB")
# 함수가 호출 되어 10을 출력을 하긴 하지만 가독성이 좋지않다.
# 이유는 함수의 매개변수 명이 name 이니 매개변수 값에 맞게 주는것이 현명하다.
# say_hello(10)

# 파이썬에서는 오버로딩 개념이 없다. 같은 함수 이름이라면 마지막에 정의된
# 함수만 인식하게된다. 하여, 함수명은 유니크한 값으로 짓도록 한다.
hello.say_hello_name_msg("BOB", "반가워요")
hello.say_hello_name_msg("jack", "도와줘요")


# 값을 반환하는 함수 예제
# start 부터 end까지의 누적합을 구하는 함수
def  get_sum(start,end):
    hap = 0
    for i in range(start, end+1):
        hap += i
    return hap

# get_sum()을 이용하여 범위의 누적합을 구하는 코드
result = get_sum(1,10)
print(type(result))
print("1~10 누적합 : ", result)

result = get_sum(1,30)
print(type(result))
print("1~30 누적합 : ", result)

result = get_sum(1,50)
print(type(result))
print("1~50 누적합 : ", result)

result = get_sum(1,100)
print(type(result))
print("1~100 누적합 : ", result)


result = hello.get_sum(20,30)
print(type(result))
print(f"20~30 누적합 : {result}")