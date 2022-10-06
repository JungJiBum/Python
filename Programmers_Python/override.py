# 단순 오버라이드


class Animal():

    def walk(self):
        print("걷는다")
    
    def eat(self):
        print("먹는다")

    def greet(self):
        print("인사한다")

class Cow(Animal):
    '''소'''

class Human(Animal):

    def wave(self):
        print("손을 흔든다")
    
    def greet(self):
        self.wave()

class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다")
    
    def greet(self):
        self.wag()

person = Human()
dog = Dog()
cow = Cow()

person.greet()
dog.greet()
cow.greet()

