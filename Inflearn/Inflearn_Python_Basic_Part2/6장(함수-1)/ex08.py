# 디폴트 인수(default argument)
# 함수의 매개변수가 기본 값을 가지게 하는 방법

# 아래 hello()는 매개변수 2개를 가지지만 디폴트 인수가 있어서 함수 호출 시
# name에 대응되는 인수값만 가지고도 호출이 가능하다.

def hello(name,msg="반갑습니다."):
    print("안녕하세요" + name + ',' + msg)


# name에 대응되는 매개변수값을 하나만 가지고 함수 호출
hello("Mr.BOB")
# 매개변수 name, msg는 기본 인수 값이 존재하나, 아래처럼 매개변수를
# 인자값으로 입력하니 기본 인수 값은 무시가 된다.
hello("Mr.BOB","Good Bye.")
