# 사용자로부터 10진수를 입력받아 2진수로 문자열로 변환하여 반환하는
# 함수 decTobin(num)을 작성하라.

def decTobin(num):
    binary = ""

    while num != 0: # num이 0이 아닐때까지 반복한다.
        value = num % 2 # num 값을 2로 나누었을때 나머지 -> 1
        if value == 0: # 나머지 값이 0일때 
            binary = "0" + binary
        else:          # 나머지 값이 1일때
            binary = "1" + binary
        num = num // 2
        # print("num : ", num)
    return binary

# decNum = int(input("10진수를 입력하세요 : "))
decNum = 10
print("10진수 ", decNum,"을 2진수로 변경한 값 : ",decTobin(decNum))

print("="*30)
# 파이썬에서 제공하는 진법변환 함수들
print(bin(10))      # 0b1010 -> 0b는 2진수를 의미함
print(oct(10))      # 0o12 -> 8진수
print(hex(10))      # 0xa -> 16진수


print(int("0b1010",2))  # 2진수의 값을 10진수로 변환
print(int("0o12",8))    # 2진수의 값을 8진수로 변환
print(int("0xa",16))    # 2진수의 값을 16진수로 변환

