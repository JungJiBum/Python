# 반복문(iteration)에 대한 실습
# 아래와 같이 "hello"를 5번 출력하려면 print()를 5번 호출해야하는 번거로움 발생

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("="*10)

# for문을 이용하여 작성해보자.
# for문을 이용하여 출력한 코드로 x 는 루프변수라 칭함
# in 다음에 오는 것을 시퀀스 라고 칭함
# 시퀀스 다음에 올 수 있는 것은 리스트, 문자열이 존재함

# 1000번의 루프를 하게 만드려면 정수 리스트가 1000개의 값이 존재해야 하는 번거로움 발생

# for x in [0,1,2,3,4]:
#     print("Hello")

# print("="*10)

# range(x)를 이용하면 위 정수 리스트를 사용하는 것보다 훨씬 효율적이며 가독성이 좋다.
# range() 함수는 리스트 타입으로 변환해준다.
# range(x) : 0부터 시작하고 마지막 값(5-1)까지 정수 리스트 타입으로 반환을 해준다.

# for x in range(10):
#     print("hello")

# range() 함수의 타입은 range 객체이다.


#문자열 리스트를 시퀀스로 가질때 for 문
s = ['짱구','철수','맹구','훈이','유리']
for name in s:
    print("Nice to meet you " + name+"!")

# 줄바꿈 하지않게 하는 end 인자값 확인하기
for x in [0,1,2,3,4]:
    print(x, end=' ')


