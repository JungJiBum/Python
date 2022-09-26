# Person클래스를 만들고 객체정보를 출력
# 생성자 메서드 사용

# 클래스 생성
class Person:

    #생성자
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    #출력
    def print_info(self):
        print("-"*30)
        print("Name : ",self.name)
        print("Age : ",self.age)

# 클래스 사용
'''
#__init__ 메서드 사용 안할 경우
p1 = Person()
p1.create_info("BOB",29)
p1.print_info()
'''
p1 = Person("BOB",29)
p1.print_info()

p2 = Person("John",30)
p2.print_info()
