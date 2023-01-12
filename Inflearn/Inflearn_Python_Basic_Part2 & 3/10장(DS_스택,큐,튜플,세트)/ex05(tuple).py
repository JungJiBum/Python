# 튜플(tuple)에 대한 실습
'''
튜플 특징 -> 리스트에 반하여 변경이 불가능한 객체이다. 리스트에 비해 속도가 빠르다. 튜플도 시퀀스 일종이다.
+, *, min(), max(), len(), cmp(), tuple() 연산과 내장함수가 사용가능하다.
리스트는 대괄호 [] 요소를 감싸지만 튜플은 () 요소를 감싼다.
'''

colors = ("red", "blue", "yellow")
print(colors)
print(type(colors))

numbers = (1, 2, 3, 4, 5)
print(numbers)

# 튜플로 리스트와 마찬가지로 여러가지 자료형을 섞어서 생성 할 수 있다.
tuple1 = (1, 2.2, "HI")
print(tuple1)

# 공백 튜플 만들기
tuple2 = ()
# 튜플은 한번 생성되어지면 더이상 추가, 삭제, 수정이 불가능 하다.
# tuple2[0] = 100

# 하나의 값만 가지는 튜플을 생성할 때는 반드시 요소 뒤에 ,(콤마)를 적어줘야 한다.
# 그렇지 아니하면 그냥 일반 정수나 문자열로 인식한다.
tuple3 = (10)
print(tuple3, type(tuple3))
print(tuple2)

li = [1, 2, 3, 4, 5]
tuple4 = tuple(li)
# 리스트를 내장함수인 tuple()로 tuple로 만들수가 있다.
print(li)
print(tuple4)

print("-"*40)
# 튜플도 리스트와 마찬가지로 내장 튜플을 가질 수 있다.
t1 = (1, 2.2, "Hello")
t2 = (3.3, 4.4, 5.5)
t3 = t1, t2
print("t1의 주소 : ", id(t1))
print("t2의 주소 : ", id(t2))
print("t3의 주소 : ", id(t3))
print("t3[0]의 주소 : ", id(t3[0]))
print("t3[1]의 주소 : ", id(t3[1]))
print(t2, type(t2))

t4 = (1, 2.2, 3, "안녕")
t5 = (1, 2.2, 3)
print("t4의 길이 : ", len(t4))
# 서로 다른 데이터 타입이 튜플의 요소로 존재한다면 비교가 되질않는다.
# print("t4의 가장 큰 값 : ", max(t4))
print("t5의 가장 큰 값 : ", max(t5))
print("t5의 가장 작은 값 : ", min(t5))

t6 = (1, 2.2, 3, "안녕")
t7 = (1, 2.2, 3)
t8 = t6, t7     # tuple은 + 연산이 가능함(접합)
print(t8)
t9 = t7 * 2     # tuple은 * 연산이 가능함(반복)
print(t9)

if 2.2 in t6:   # 존재 여부를 알아봄
    print("t6에는 2.2가 존재")

# tuple은 시퀀스의 일종이니 반복문도 가능함
for x in t6:
    print(x, end=" ")

print()

# 인덱싱
t10 = (1, 2.2, 3, "안녕", "철수", 5.5)
print(t10[4])
print(t10[-1])
# 슬라이싱
print(t10[:4])
print(t10[4:6])
print(t10[-3:-1])

# cmp() 함수 미지원
t1 = (1, 2.2, 3)
t2 = (1, 2.2, 3)
# x = cmp(t1,t2)

# dir() 함수는 사용할 수 있는 함수들을 출력해준다.
print(dir(t1))
# tuple을 비교 하고자 한다면 __eq__()를 사용하자
print(t1.__eq__(t2))


