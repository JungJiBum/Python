#관계 연산자 만들어보기


# print(10>5) #T
# print(10>11) #F
# print('-' * 10)
# print(1==1) #T

# 논리 연산자 만들어보기
# a = True
# b = False
# print(a and b) #F
# print( a or b) #T
# print(a, not(a)) #T F
# print(b, not(b)) #F T

# if a and b:
#     print("T")
# else:
#     print("F")

# 할당 연산자 만들어보기
# a =100
# a =a*2
# print(a)

# b=200
# b= b*2
# print(b)

# 멤버쉽 연산자 만들기
# in 연산자
# is 연산자
# not 연산자

# lst = [1, 2, 3, 4, 5]
# print(lst, type(lst))

# a = 7 in lst
# print(a)
# a = 5 in lst
# print(a)

# tpl = 1, 2, 3
# print(tpl, type(tpl))
# b = 4 in tpl
# print(b)
# b = 2 in tpl
# print(b)

# 부울 연산자
print(bool(1))
print(bool(None))
print(bool(0))
print(bool(-1))

a = None
print(a,type(a))
print(bool(a))
