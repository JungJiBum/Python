# 값에 의한 호출(call by value), 값에 의한 전달(pass by value)
# 두가진 동일한 개념이다.
# 함수를 호출할 때, 값이 복사가 되어진다. (중요)
# 호출한 곳에 영향을 끼치지 아니한다.
# 숫자 객체는 변경될 수 없는 immutable object 이다.
def change(num):
    print(f"change()내 연산전 num 값 : {num}, 주소 값 {id(num)} ")
    num = num+10
    print(f"change()내 연산후 num 값 : {num}, 주소 값 {id(num)} ")
    return num

# 파이썬에서는 모든 값들이 객체로 이루어져 있다.
n = 100
print("호출 전 n의 주소(id) 값 : {}".format(id(n)))
print(f"호출 전 n의 값은 : {n}")
x = change(n)
print(f"호출 후 x의 값 : {x}")
print("호출 후 x의 주소(id) 값 : {}".format(id(x)))
print(f"호출 후 n의 값 : {n}")
print("호출 후 n의 주소(id) 값 : {}".format(id(n)))