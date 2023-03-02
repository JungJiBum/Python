'''
클래스 개념
1. OOP?
2. 클래스, 인스턴스
3. self 개념
4. 인스턴스 메소드
5. 클래스, 인스턴스 변수
'''

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도로 존재

# 예제1
class Dog1:  # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/ 인스턴스 속성
    def __init__(self, name, age):
        # self.a = name 도 가능 self.임의 = 임의불가
        self.name = name 
        self.age = age

''' Dog라는 클래스를 만들었고, 우리가 구현할, 우리가 눈에 보이는 개의 종류, 개 이런것을 통합하는 객체라 할 수 있다. '''
# 우리가 만들 소프트웨어로 구현할 대상을 객체라 한다.
# 클래스 형태로 틀을 만든것이며, 이걸 가지고 인스턴스화를 시킨다.
# 클래스 -> 붕어빵 틀 / 인스턴스 -> 틀을 가지고 찍어낸, 코드에서 사용하는 어떠한 객체라 생각하면 된다.

# 클래스 정보
# print(Dog)

# 인스턴스화
# a = Dog("mikky",2)
# b = Dog("baby",3)

''' 하나의 틀을 가지고 코드 상 a,b라는 변수로 할당해서 메모리에 올라가고 ID값을 갖는다. 실제 설계도를 바탕으로 구현된 것을 인스턴스화'''
''' 클래스 -> 인스턴스 -> 객체(object) '''
''' 인스턴스와의 차이 -> 코드로 직접 구현하여 메모리에 올라간 시점에 어떤 변수로 활용할 수 있는 대상'''

# 비교
# print(a==b, id(a), id(b))

# # 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# print('dog1', a.__dict__)
# print('dog2', b.__dict__)

# # 인스턴스 속성 확인
# print('{} is {} and {} is {}.'.format(a.name,a.age,b.name,b.age))

# if a.species == 'firstdog':
#     print('{0} is a {1}'.format(a.name, a.species))

# print(Dog.species)
# print(a.species,b.species)

print()
# 예제 2
# self의 이해 -> 나만의 인스턴스의 속성을 
class SelfTest:
    def func1(): # 클래스 메소드 -> 클래스로 직접호출함 매개변수가 없기때문에..
        print("Func1 called")

    def func2(self): # self는 인스턴스 메소드 -> 인스턴스를 넘기거나..인스턴스로 호출을 해야한다..
        print(self)
        print(id(self))
        print("Func2 called")

f = SelfTest()

# print(dir(f))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', 'func1', 'func2']  
'''

print(id(f))
# f.func1() 예외
f.func2()
SelfTest.func1()
SelfTest.func2(f) # 예외
print("=============================================================")
# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수 = 0
    stock_num = 0   #재고
    
    def __init__(self, name) -> None:
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num +=1
    
    def __del__(self):  #객체가 소멸할때 자동으로 호출되는 함수
        Warehouse.stock_num -=1

user1 = Warehouse("Lee")
user2 = Warehouse("Cho")

print(Warehouse.stock_num)
# Warehouse.stock_num=50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before',Warehouse.__dict__)
'''
before {'__module__': '__main__', 'stock_num': 2, '__init__': <function Warehouse.__init__ at 0x000001243CD15D80>, '__del__': <function Warehouse.__del__ at 0x000001243CD15E10>,
'__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}
'''
print(user1.stock_num)

del user1
print('after',Warehouse.__dict__)
'''
after {'__module__': '__main__', 'stock_num': 1, '__init__': <function Warehouse.__init__ at 0x000001243CD15D80>, '__del__': <function Warehouse.__del__ at 0x000001243CD15E10>,
'__dict__': <attribute '__dict__' of 'Warehouse' objects>, '__weakref__': <attribute '__weakref__' of 'Warehouse' objects>, '__doc__': None}
'''

#예제 4
class Dog:  #object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/ 인스턴스 속성
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old.'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}!'.format(self.name,sound)

# 인스턴스 생성
c = Dog('july',4)
d = Dog('marry',10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speak("woop woop"))
print(d.speak('wal wal'))