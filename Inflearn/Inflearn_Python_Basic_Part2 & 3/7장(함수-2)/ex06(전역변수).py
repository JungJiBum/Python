# 전역변수(global variable) : 함수의 외부에 정의된 변수를 전역변수라고 칭한다.
# 파이썬에서 전역변수를 다루는 형태가 타 언어들에 비해서 접근방식이라는 측면에서는
# 융통성이 떨어진다.
# 파이썬에서의 위와 같은 부분은 오히려 좋은 프로그래밍 습관을 장려하기 위한 한 방법론적이다.

# def test():
#     #test()함수 내 text라는 지역변수가 없을때는 전역변수를 가져와서 사용함
#     print(text) 

# text="파이썬 공부"  # 전역변수인 text 변수에 문자열 할당
# test()


# def test():
#     #test()함수 내 text라는 지역변수가 없을때는 전역변수를 가져와서 사용함
#     # NameError: name 'text' is not defined 에러 발생
#     # 이유는 test()를 호출한 시점에는 전역변수 text가 할당이안되있기때문
#     print(text) 

# test()
# text="파이썬 공부"  # 전역변수인 text 변수에 문자열 할당


def test():
    # 전역변수 tet도 할당이 되어 있지만
    # 함수 내에서는 지역변수가 무조건 출력된다.
    # 함수 내에서는 지역변수가 default 이기 떄문이다.
    text="Python study"     #지역변수 text변수에 문자열 할당
    print(text)             #지역변수 text 값 출력

text="java stduy"           #전역변수 text에 문자열 할당
test()
print(text)                 #전역변수 text 값 출력
