# 부울(bool) 변수 알아보기
# 부울변수 용도는 플래그 변수 형태로 사용을 많이 함
# 타 언어에서는 부울변수의 값은 소문자로 시작하는 true, false를 사용하지만
# 파이썬은 대문자로 시작하는 Ture, False로 시작함 잊지말기

flag = False
print(type(flag))
print(flag)
# 부울 변수 값을 바꾸기 위해 not 연산자 이용
flag = not flag
print(type(flag))
print(flag)

if flag:
    print("참이라 출력")
else:
    print("거짓이라 출력")
    flag = not flag

if flag:
    print("참이라 출력")
else:
    print("거짓이라 출력")