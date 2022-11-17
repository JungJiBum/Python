# 논리 연산자(logical operator)는 두 개 이상의 조건을 조합해서 참인지 거짓인지 계산할때 사용함
''' 논리연산자 종류 
    and(논리곱)
    or(논리합)
    not(부정)
'''
# and 논리 연산자
name= "BOB"
age = 14
height = 160
# and 연산자는 여러 조건 중 처음 조건이 거짓이라면 다른 조건은 검사x (단축 계산)
# and 연산자는 모든 조건이 참이어야 참(True)
if (age >= 14) and (height >=150) and (name == " jack"):
    print(f"{name}님은 OK")
else:
    print(f"{name}님은 No")
print("-"*20)
# or 논리 연산자
# or 연산자는 모든 조건 중 하나라도 참이면 참(True)
if (age >= 25) or (height >=170) or (name == "BOB"):
    print(f"{name}님은 OK")
else:
    print(f"{name}님은 No")
print("-"*20)
# not 부정 연산자
# not 연산자는 조건이 참이면 전체 조건식의 결과를 반대로 거짓으로 만든다.
# 결과가 거짓이면 참으로 바꾼다(True -> False / False -> True)
if not(1 == 0):
    print("1과 0은 다르다")