# 제곱구하는 함수
def square(num):
    temp = num * num
    return temp # return값 처리

# 두 수 중 큰 값 반환
def get_max(x,y):
    temp = 0
    if x > y:
        temp  = x
    else:
        temp = y
    return temp

# 두 수 중 작은 값 반환
def get_min(x,y):
    temp = 0
    if x > y:
        temp = y
    else:
        temp = x
    return temp


# 거듭제곱 구하여 값을 반환하는 함수
def power(x,y):
    result = 1
    for i in range(y):
        result *=x
    return result

