# namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔 저장하는 자료구조

# 일반적 튜플 경우
person1 = ("김두한",14,"남")
person2 = ("시라소니",17,"남")
# %n 들어가면서 튜플의 값들을 각 형식지정자에 맞게 적용
for n in [person1,person2]:
    print("%s은(는) %d살이며 %s성이다." % n )
# 일반적인 튜플 .(접근연산자) 사용을 하지못하고, 인덱스로만 접근이 된다.
print(person1[0])
# 일반적인 튜플은 값의 수정이나 변경이 이루어지지않는다.
# person1[0]="김최"

print("%s은(는) %d살이며 %s성이다." % (person1[0], person1[1], person1[2]))

print("-"*50)

# namedtuple 인 경우
from collections import namedtuple
# Person 이라는 namedtuple 을 정의함
Person = namedtuple(typename="Person",field_names=('name age gender addr'))
P1 = Person(name="BOB",age=20,gender="남", addr="미국")
P2 = Person(name="JACK",age=22,gender="남", addr="대전")
for n in [P1, P2]:
    print("%s은(는) %d살이며 %s성이다. 그리고 %s에 산다." % n )


# Person 이라고 정의를 해놓았고 그의 필드들이 3개가 존재하고 있기 때문에
# namedtuple은 .(접근연산자)를 사용할 수 있지만, 인덱스로도 접근이 가능하다.
print(P1.name, P1.age, P1.gender)
print(P2[0], P2[1], P2[2])

print("-"*50)
# namedtuple의 _make() 메소드 : 기존에 생성된 namedtuple에 새로운 인스턴스를 생성해주는 메소드
# _make() 안의 매개변수로 들어가는것은 시퀀스 자료형이어야 한다.
P3 = Person._make(["구마적",30,"남","서울"])

for n in [P1,P2,P3]:
    print("%s은(는) %d살이며 %s성이다. 그리고 %s에 산다." % n )
print("-"*50)
# namedtuple 에서는 인덱스를 통한 값변경은 되지 않지만 _replace() 메소드로 값의 변경이 가능하다.
P1 = P1._replace(name="장거한")
P2 = P2._replace(age=90)
P3 = P3._replace(addr="부산")

for n in [P1,P2,P3]:
    print("%s은(는) %d살이며 %s성이다. 그리고 %s에 산다." % n )

print("-"*50)

#생성 되어진 Person 이라는 namedtuple의 _fields로써 Person에 있는 필드명 tuple() 형식으로 리턴을해줌.
print(P1._fields)       #('name', 'age', 'gender', 'addr')

# getattr()는 필드명으로 그 값을 출력할 때 사용한다.
print(getattr(P1, 'name'))
print(getattr(P2, 'name'))
print(getattr(P3, 'name'))

# **(double-star-operator)은 namedtuple() 딕셔너리 자료구조를 namedtuple() 변환하여 반환함
dic = {"name":"BOB", "age":15, "gender":"남", "addr":"대전"}
print(dic, type(dic))
P4 = Person(**dic)
print("%s은(는) %d살이며 %s성이다. 그리고 %s에 산다." % (P4.name,P4.age,P4.gender,P4.addr))
print(type(P4))