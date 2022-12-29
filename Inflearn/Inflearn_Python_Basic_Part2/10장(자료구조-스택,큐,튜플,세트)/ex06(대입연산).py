# 튜플 대입 연산에 대한 실습
# 튜플 패킹(packing) -> 튜플에다 값을 저장하는 과정
# 튜플 언패킹(unpacking) -> 튜플에서 값을 추출해서 변수에 대입하는 과정

# 값을 교환할 때 : 일반적 방법
x = 10
y = 20
temp = 0 # 빈 컵 역할
print("값 변경 전(x,y) : ",x,y)
temp = x
x = y
y = temp
print("값 변경 후(x,y) : ",x,y)
print("-"*40)
# 값을 교환할 때 : 튜플 이용하는 방법
(a,b) = 100,200
print("값 변경 전 : ",(a,b))
(c,d) = (b,a)       # 튜플에서 값 변경 시 빈 컵은 필요없다.
print("값 변경 후 : ",(c,d))

# 인자값들이 서로 맞게 줘야한다. 안그러면 not enough values to unpack -> valueError 발생함
# (x,y,z) = (10, 20)

# 여러개 변수를 한번에 할당하는 방법
person = ('지범',29,'직딩')
(name, age, job) = person
print(person)
print(f"name = {name} / age = {age} / job = {job}")

