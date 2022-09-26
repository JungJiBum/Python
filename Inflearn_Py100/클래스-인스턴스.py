#트정 클래스의 인스턴스 객체인지 아닌지를 확인하려면 어떻게 하는지 설명


#[1] 클래스 생성
# 특정 클래스의 인스턴스 유무 확인 -> instance()함수 사용 -> instance(인스턴스 객체명, 클래스명)

#----------------------
class Person:
    pass

class Monster:
    pass
#----------------------


#[2] 클래스 사용
p1 = Person()
result = isinstance(p1, Person) #--- p1 인스턴스(객체가) Person 클래스로부터 만들어진것이 맞는지
print(result)
print(isinstance(p1,Person))

rs = isinstance(p1,Monster)
print(rs)
print(isinstance(p1,Monster))