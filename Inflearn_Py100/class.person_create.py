#이름과 나이를 전달받아 객체를 생성하는 Person 클래스를 만들고 객체 정보 출력

# 클래스 생성
class Person:

    # 정보 생성
    def create_info(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("-"*30)
        print("Name : ",self.name)
        print("Age : ",self.age)
        # print("-"*30)

# 클래스 사용
p1 = Person()
p1.create_info("BOB",29)
p1.print_info()

p2 = Person()
p2.create_info("John",30)
p2.print_info()