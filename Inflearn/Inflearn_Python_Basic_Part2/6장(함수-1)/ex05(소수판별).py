# 사용자로부터 숫자를 입력 받아 소수 판별하는 is_prime()을 구현하라
# 소수면 T 아니면 F
# 1과 자기자신과 나누어지는 수를 소수라 한다.

# 함수 선언 및 구현
def is_prime(num):
    for i in range(2, num+1):
        temp = True
        if (num%i) == 0:
            temp = False
        else:
            temp = True
        return temp

# 함수 호출
num = int(input("숫자를 입력하세요 : "))
print(is_prime(num))