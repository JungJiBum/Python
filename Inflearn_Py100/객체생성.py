#생성자를 이용하여 객체를 생성하는 코드.

#[1] : 클래스 생성
print("[1] : 클래스 생성")
#--------------------------------------
class SmartPhone:
    #생성자
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(self.name + "객체가 생성 되었다.")
        print("-"*40)
        print(self.name + "가격은 " + str(price) + "원 입니다.")
        print("-"*40)
#--------------------------------------
s1 = SmartPhone("LG",500000)

