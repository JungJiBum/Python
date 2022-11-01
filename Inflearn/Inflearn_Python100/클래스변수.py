# #클래스 변수란 무엇인가

# #[1] : create class
# #--------------------------
# class MyClass:

#     # 클래스 변수
#     a_var = 1250

#     # 클래스 메서드
#     def a_method(self):
#         MyClass.a_var = 3000



# #--------------------------

# #[2] : using class
# # 클래스 변수 호출 --> 클래스 변수는 클래스 외부에서 "클래스명.변수명"으로 접근이 가능
# print(f"[1] 최초 클래스 변수의 초기 값 --> {MyClass.a_var}")

# # 클래스 변수 값 수정
# MyClass.a_var = 1500
# print("[2]클래스 변수의 초기값을 1500으로 변경 --->",MyClass.a_var)

# # 클래스 메서드 호출을 통해서 수정
# m1 = MyClass()
# m1.a_method()
# print("[3] 클래스내 메서드를 호출해서 변수값 수정",MyClass.a_var)
# #  print(MyClass.a_method()) # Err 발생


#[1] : 클래스 생성
#--------------------------
class MyClass:

    #class var
    a_var = 0

    #class method
    def a_method(self):
        self.a_var = 300
        # MyClass.a_var=300 #이면 값이 변경됨

#--------------------------

#[2 : 클래스 사용
print('[1] 최초 초기값 --> ', MyClass.a_var)
MyClass.a_var=100
print('[2]초기 값을 100으로 변경 --> ',MyClass.a_var)
m1 = MyClass()
m1.a_method() #--> self값으로 m1을 받아옴 m1.a_var=300 문법상에러도없고 결과에 영향도없음
print('[3] 변수 값을 300으로 변경 -->',MyClass.a_var)
print(m1.a_var) # --> 300이라는 값을 가지고 있음
