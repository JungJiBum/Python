'''
파이썬 함수 및 중요성
파이썬 함수식 및 람다(lambda)

함수 정의방법
def func_name(parameter):
'''

# # 예제1
# def first_func(w):
#     print("Hello, ", w)

# word = "Good day"

# first_func(word)


# # 예제2
# def return_func(w1):
#     value = "Hello, " + str(w1)
#     return value

# w1 = "python"
# x = return_func("Good day2")
# print(x)

# # 예제3(다중반환)
# def func_mul(x):
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return y1, y2, y3

# x, y, z = func_mul(10)
# print(x, y, z)

# # 튜플리턴
# def func_mul2(x):
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return (y1, y2, y3)
# q = func_mul2(20)
# print(type(q), q, list(q))

# def func_mul3(x):
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return [y1, y2, y3]

# p = func_mul3(30)
# print(type(p), p, set(p))


# def func_mul4(x):
#     y1 = x * 10
#     y2 = x * 20
#     y3 = x * 30
#     return {'v1':y1, 'v2':y2, 'v3':y3}

# d = func_mul4(30)
# print(type(d), d, d.get('v2'), d.items(), d.keys())

# 중요
# *args, **kwargs

# *args(언패킹)
def args_func(*args):  # 매개변수 명은 자유 가변 인자를 사용하게 해주는 어떤 언패킹의 *이 붙은 args
    for i, v in enumerate(args, start=1):
        print("result : {}".format(i), v)
    print("===================")


args_func("Lee")
args_func("Lee", "Park")
args_func("Lee", "Park", "Kim")


# **kwargs(언팩킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print("=====================")


kwargs_func(name1="Lee")
kwargs_func(name1="Lee", name2="Park")
kwargs_func(name1="Lee", name2="Park", name3="Cho")

# 전체 혼합

def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10,20,'Lee','Kim','Park',age1=20, age2=30, age3=40)



# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In fuce")
    func_in_func(num + 100)

nested_func(100) 
# 실행불가 
# func_in_func(1000) -> 부모함수가 호출되고 해당 함수가 호출될때 사용할수 있으므로, 일반적으로 사용할순 없다.

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Healp 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(x,y):
    # return x * y

#lambda x, y:x*y

# 일반적 함수 -> 할당
def mul_func(x,y):
    return x * y

print(mul_func(10,50))

mul_func_var = mul_func
print(mul_func_var(20,50))

# 람다 함수 -> 할당
lambda_mul_func = lambda x,y : x*y
print(lambda_mul_func(50,50))

def func_final(x,y,func):
    print('>>>>>>',x * y * func(100,100))

func_final(10, 20, lambda_mul_func)
func_final(10, 20, mul_func_var)

# print(input()) 합치기
print("이름 : {0}, 성 : {1} ".format(input("이름 입력 : "),input("성 입력 : ")))