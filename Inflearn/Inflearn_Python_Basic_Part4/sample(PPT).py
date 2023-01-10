# 클래스 개념
class Car:
    # 자동차의 필드
    color = ""  # 색상
    speed = 0   # 현재속도
    # 자동차 메서드
    def upSpeed(self,value):    #(증가할 속도량)
        self.speed +=value
        # 현재 속도에서 증가할 속도량 만큼 +
    def downSpeed(self,value):  #(감소할 속도량)
        self.speed -=value
        # 현재 속도에서 감소할 속도량 만큼 -
# 출력결과 : 아무것도 없다. 위 코드는 Car 클래스의 설계도이다.
# 붕어빵 틀과 같은 존재.
'''
self 단어는 간단히 설명하면 자기 자신의 주소를 가지고 있는데,
self.speed는 speed를 의미함. 즉 자신의 클래스에 있는 speed 멤버변수(필드)라고 해석하자.
self.speed를 사용하려면 매개변수로 self를 받아야한다.
주의할 점! 매개변수 self를 실제로 전달받지않으며, value만 전달받는 것이다.
즉 upSpeed() 메서드의 매개변수는 value 하나뿐
self 라는 단어는 객체를 생성해야지만 활성화가 이루어진다.
'''
class Car:
    color = ""  # 색상
    speed = 0   # 현재속도

    # #기본 생성자
    # def __init__(self):
    #     self.color = "red"
    #     self.speed = 0
    
    # 매개변수가 있는 생성자
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    # 자동차 메서드
    def upSpeed(self,value):
        self.speed +=value
    def downSpeed(self,value):
        self.speed -=value
    # 추가된 메서드
    def printMessage(self):
        print("시험 출력")

# self를 사용하는 이유는 메서드 안에서 필드에 접근하기 위함
# 매개변수로 보기보단 메서드 안에 무조건 써야하는것으로 이해하자
# 메서드 안에서 필드에 접근할 일이 없다면 self는 생략이 가능함
# 메서드나 멤버 변수(필드)는 추가, 삭제가 가능함

#메인 코드 부분
'''인스턴스 생성'''
# myCar1 = Car()
# myCar2 = Car()

myCar1 = Car("빨강",30)     # 매개변수가 있는 생성자 호출
myCar2 = Car("파랑",60)     # 매개변수가 있는 생성자 호출
'''필드에 값 대입'''
myCar1.color="red"
myCar1.speed=0
myCar2.color="blue"
myCar2.speed=0
'''메서드 호출'''
myCar1.upSpeed(30)
myCar2.downSpeed(60)

print(f"자동차1 색상은 {myCar1.color}이며 현재속도 {myCar1.speed}km입니다.")
print(f"자동차1 색상은 {myCar2.color}이며 현재속도 {myCar2.speed}km입니다.")


class Car:
    name = ""
    speed = 0

    # 매개변수가 있는 생성자
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    # 아래 2개의 메서드는 getter() 메서드라 한다.
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed

#변수 선언 부분
car1 , car2 = None, None

#메인 코드 부분
car1 = Car("Audi",0)
car2 = Car("Benz",30)
print("{}의 현재속도는 {}km 입니다".format(car1.getName(),car1.getSpeed()))
# print("{}의 현재속도는 {}km 입니다".format(car2.getName(),car2.getSpeed()))
print("%s의 현재속도는 %skm 입니다" % (car2.getName(),car2.getSpeed()))

'''
클래스 변수 count를 선언하고 0으로 초기화.
생성자 안에서 클래스 변수에 접근하려고 클래스명.count를 1증가시킴
즉 생성자는 인스턴스를 생성할 때 작동하므로, 자동차 총 생산 대수를 1씩 증가시킨것.
메인코드 부분에서 클래스 변수를 사용하려고 Car.count나 myCar2.count를 모두 이용할 수 있다.
둘다 클래스 변수에 접근한다.

중요한 것은 여기서 객체지향 개념으로 따져볼때 클래스 변수는 메모리 상단에 클래스 정보와 함께
같이 공간을 잡는다. 하여 접근할 때는 웬만하면 클래스명.클래스변수명으로 접근하는 것이 올바른 표현.

클래스 안에서 필드에 접근할 때 앞에 self를 붙이면 인스턴스 변수가 되고, 앞에 클래스명을 붙이면 클래스 변수를 생성함

'''
# 클래스 선언 부분
class Car:
    color = ""  # 인스턴스 변수
    speed = 0   # 인스턴스 변수
    count = 0   # 클래스 변수

    def __init__(self):
        self.speed = 0
        Car.count +=1

# 변수 선언 부분
myCar1, myCar2 = None, None
# 메인 코드 부분
myCar1 = Car()
myCar1.speed = 30
print("자동차 1의 현재속도는 %dkm, 생산된 자동차는 총 %d대 이다."%(myCar1.speed,Car.count))

myCar2 = Car()
myCar2.speed =60
print("자동차 2의 현재속도는 %dkm, 생산된 자동차는 총 %d대 이다."%(myCar2.speed,myCar2.count))

myCar3 = Car()
print("자동차 31의 현재속도는 %dkm, 생산된 자동차는 총 %d대 이다."%(myCar2.speed,myCar3.count))