'''
소멸자란
[1] : 클래스 생성 -> 생성자, 소멸자
생성자는 객체가 생성될때 실행되고, 소멸자는 객체가 소멸될 때 실행된다.
생성자는 __init__ 속성을 사용하고, 소멸자는 __de__ 속성을 사용하여 정의한다.
'''
#-----------------------------------------------------------------------------


class SmartPhone:

    #생성자
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(self.name + " 스마트폰 객체가 생성되었다.")
        
        print(self.name + " 스마트폰의 가격은 " + str(self.price)+"이다.")
        print('-'*40)

    def a_method(self):
        print("a_method가 사용되었다.")

    #소멸자
    def __del__(self):
        print(self.name + " 스마트폰 객체가 소멸되었다.")
#-----------------------------------------------------------------------------

#[2] : using class
s1 = SmartPhone('LG',500000)    #객체 생성
s1.a_method()   # 함수 호출
# del s1
s1.a_method() # 함수 호출
#-----------------------------------------------------------------------------
s2 = SmartPhone('sk',5000)  #객체 생성
s2.a_method()   #함수 호출
del s2  #소멸자 
s2.a_method()   #소멸로 인해 함수 호출 할 수없음




