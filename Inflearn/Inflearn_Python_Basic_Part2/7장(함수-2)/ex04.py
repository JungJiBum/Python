# mutable object 중 dictionary 라는 타입이 있다.
# 딕셔너리의 형태는 키 와 값이 쌍으로 이루어져 있다.
# 딕셔너리의 키 값은 유니크한 값이 되어야 한다. 하지만 값은 변경이 가능하다.
# 딕셔너리의 call by reference가 성립되는 이유는 변경 가능한 mutable object이기 때문
# call by objective-reference라고도 칭한다.

def change(dic):
    print(f"change()함수 내 연산 이전 값 {dic} / 주소 값 {id(dic)}")
    dic["몸무게"] = 80
    print(f"change()함수 내 연산 이후 값 {dic} / 주소 값 {id(dic)}")


dic = {"name" : "BOB","age":29,"height":173}
# print(dic)
# 키를 주고 값을 얻어온다.
# print(dic["name"])
print(f"호출 전 dic 값{dic} / 주소값 {id(dic)}")
change(dic)
print(f"호출 후 dic 값{dic} / 주소값 {id(dic)}")