# call by reference에 대한 실습
# 함수를 호출할 때, 실질적인 주소 값이 넘어가서 호출한 곳에 영향을 끼치는 형태
# 파이썬에서는 함수의 매개변수 값이 전부 객체인데 list, dictionary와 같은
# mutable object 즉 변경이 가능한 객체이므로 call by objective-reference라고 한다.


def change(li):
    print(f"change()함수 내의 연산 전의 li의 값 {li} / 주소값 {id(li)}")
    li += [100,200]
    print(f"change()함수 내의 연산 후의 li의 값 {li} / 주소값 {id(li)}")

list = ['안녕',1,3,1,1.1]
print(f"change()함수 호출 전 list의 값 {list} / 주소값 {id(list)}")
change(list)
print(f"change()함수 호출 후 list의 값 {list} / 주소값 {id(list)}")


