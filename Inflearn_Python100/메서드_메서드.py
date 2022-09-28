# 클래스 메서드 안에서 다른 메서드 호출
# self를 이용한 메서드 호출 형식
# self 없이 메서드를 호출하면 --> 클래스 외부 함수 호출

#[1] 클래스 생성
#----------------------------------
class Person:
    def a_method(self):
        print('a_method 호출')

    def b_method(self):
        self.a_method() # --self 사용해서 a_method 함수 호출--
        a_method() # -- self없이 클래스 외부의 메서드를 호출--
#----------------------------------

def a_method():
    print("클래스 외부에 정의된 a_method 이다.")



#[2] 클래스 사용
p1 = Person()
p1.a_method() # --> 바로 a_method 호출
p1.b_method() # --> b_method를 통해 a_method 호출

