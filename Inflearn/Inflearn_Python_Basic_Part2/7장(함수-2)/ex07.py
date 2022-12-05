# 지역변수 / 전역변수 실습

# def test():
#     #함수안에서 하나의 변수가 전역변수가 되었다가 다시 지역변수가 될수 없는것이다.
#     # print(text)     # -> 전역변수와 지역변수 중 어떤걸 출력해야할지 모르므로 에러 발생
#     # global text     # test()함수 안에서 전역 변수인 text를 사용하겠다라는 것을 인터프리터한테 알림
#     print(text)
#     text="파이썬 공부"
#     print(text)

# text="자바 공부"
# test()
# print(text)

# 전역변수를 함수안에서 값을 변경하고자 한다면 global 키워드를 명시적으로 함수 안에 적용

def test():
    global text     # test() 함수 안에 
    text="파이썬공부"
    print(text)

text="자바공부"
test()
print(text)