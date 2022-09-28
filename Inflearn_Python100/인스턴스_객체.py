#클래스의 인스턴스 객체가 생성될 때 마다 객체 카운트를 1씩 증가시키는 클래스 구현
#이때 카운트 증가 함수는 클래스내 메서드를 통해 구현

#[1] 클래스 생성
#--------------------------
class Person:

    #클래스변수
    count_class_var = 0

    #생성자
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power
        self.increase_obj()
        

    #클래스 메서드
    def increase_obj(self):
        Person.count_class_var +=1
#--------------------------

#[2] 클래스 사용
print("현재까지 생성된 인스턴스 생성 개수 --> ", Person.count_class_var )
p1 = Person('BOB',29,100)
print(p1.count_class_var)
print("현재까지 생성된 인스턴스 생성 개수 --> ", Person.count_class_var )
p2 = Person('John',28,99)
print(p2.count_class_var)
print("현재까지 생성된 인스턴스 생성 개수 --> ", Person.count_class_var )
p3 = Person('Jack',27,98)
print(p3.count_class_var)
print("현재까지 생성된 인스턴스 생성 개수 --> ", Person.count_class_var )