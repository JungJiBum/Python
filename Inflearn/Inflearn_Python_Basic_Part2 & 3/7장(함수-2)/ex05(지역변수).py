# 지역변수(local variable)와 전역변수(global variable)에 대한 실습
# 지역변수 : 함수 안에 정의된 변수를 지역변수라 한다. 지역 변수가 범위(scope)은
# 함수 내에서만 사용이 되고 함수가 호출이 종료가 되면 지역변수는 소멸된다.
# pythontutor.com

def test():
    text="python study"     # 지역변수 text에 문자열 할당, 범위는 test()내에서만 사용
    print(text)             # 출력함수를 이용하여 text를 출력

# test()를 호출 후, "python study"라는 문자열을 출력하면서 리턴값은 없다.
test()
# 아래 출력함수는 "text" is not defined 에러코드 발생
# 이유는 text 변수가 정의되지않았기 때문
# 아울러 test()에 있는 text 변수는 지역변수 이므로 함수 호출 후 소멸됨
# print(text)
