# 매개변수는 함수의 선언부에 존재하며 함수가 호출될 때 메모리에 할당됨
# 함수가 종료되면 매개변수도 소멸됨
# 매개변수도 지역변수의 일종이다.

def list_test(my_list):
    print(f"함수 내 매개변수 my_list 의 주소 값 : {id(my_list)}")
    # 매개변수로 넘어온 my_list에 새로운 리스트 할당
    # 매개변수로 넘어온 메모리 주소를 버리고 새롭게 할당된 리스트 주소를 가짐
    # 값을 추가하면 주소값이 바뀌지않지만 새롭게 할당하게되면 주소값이 바뀜
    my_list += [1, 2, 3, 4]
    print(f"함수 내 매개변수 my_list에 할당 후 주소 값 : {id(my_list)}")
    print("함수 내부에서의 my_list 값 출력 : ",my_list)
    return

# my_list 타입은 list 이므로 변경가능객체(immutable object)
my_list= [100, 200, 300, 400]
print("함수 호출 전 my_list 의 주소값 : ", id(my_list))
list_test(my_list)
print("함수 호출 후 my_list 의 주소값 : ", id(my_list))
print("함수 외부에서의 my_list 값 출력 : ",my_list)

