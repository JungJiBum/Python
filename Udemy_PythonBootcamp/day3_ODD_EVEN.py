'''
Modulo Operation
% -> 표시
모듈로가 하는 일
ex) 7 % 2 = 몫 3 나머지 1
모듈로를 사용하면 나머지를 산출함
'''
print( 7 % 2)
print( 7 % 3)
number = int(input("숫자를 입력 하시오 : "))

if number % 2 == 0:
    print("입력한 숫자는 짝수다.")
else:
    print("입력한 숫자는 홀수이다.")