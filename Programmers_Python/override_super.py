#  오버라이드 super
class Animal():
    
    def __init__(self,name):
        self.name = name

    def walk(self):
        print("걷는다")
    
    def eat(self):
        print("먹는다")

    def greet(self):
        print("{}이 인사한다".format(self.name))

class Cow(Animal):
    '''소'''

class Human(Animal):

    def __init__(self,name,hand):
        super().__init__(name) #부모 클래스에서 처리할 수 있도록 함
        self.hand = hand        

    def wave(self):
        print("{}을 흔들면서".format(self.hand))
    
    def greet(self):
        self.wave()
        super().greet() # 부모클래스의 greet를 가져옴

person = Human("사람","오른손")
person.greet()