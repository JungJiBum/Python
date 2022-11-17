# 사용자로부터 두 개의 수를 받아 더 큰 수를 출력하시오
a,b = map(int,input("숫자를 입력 하시오 : ").split())
max = 0

if a > b:
    max = a
else:
    max = b

print("둘중 {}가 더 크다.".format(max))