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
