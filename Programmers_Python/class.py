'''
특수한 메소드
__init__ / __str__
'''
class Human():
    '''사람'''

    def __init__(self,name,weight):
        '''초기화 함수'''
        self.name = name
        self.weight = weight

    def __str__(self):
        '''문자열화 함수'''
        return "{} (몸무게 {}kg)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print(f"{self.name}가 먹어서 {self.weight}가 되었다.")
    
    def walk(self):
        self.weight -= 0.1
        print(f"{self.name}가 걸어서 {self.weight}가 되었다.") 
    
    def speak(self,message):
        print(message)

person = Human("사람",60.5)
# print(person.name, person.weight)
print(person)