'''
리스트 컴프리헨션(list comprehension)
파이썬 외에도 판다스, 넘파이 등 데이터 분석 분야에 괴장히 많이 사용되는 문법이다.
람다식과 같이 사용하는 방법도 있다.
'''

#[!]: comprehension
# 컴프리헨션 -> 개념은 보다 더 쉽게 만들어 쓰자는 의미를 나타낸달까.. --> list 또는 그 외의 것들도..(set, dict)
# 따라서 list관련 comprehension을 잘 알아두면 다른 타입의 comprehension도 쉽게 이해할 수 있다
# 수동 리스트 생성 방식과 반복문을 사용한 list comprehension 방식을 비교해보자.

#[1] : 수동 리스트 생성 --> 1~10
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"[1] 수동 리스트 생성--> {a}, {type(a)}")
# print('-'*140)

# #[!]: for 반복문
# for i in range(1, 11):
#     print(i, end=" ")
# print()
# print('-'*140)

# #[2]: for 반복문 --> empty list --> append
# b = []
# for i in range(1,11):
#     b.append(i)
# print(f"[2] 자동으로 리스트 생성 --> {b}{type(b)}")
# print('-'*140)

# #[3]: list comprehension
# c = [x for x in range(1,11)]
# print(f"[3] 자동으로 리스트 생성 list comprehension --> {c}")


#문제 다양한 list comprehension 문제 코드로 구현
# a = list()
# for i in range(1,11):
#     a.append(i)
# print(f"[1] {a}")
# #a = list(i for i in range(1,11))
# print('-'*140)

# b = [x**2 for x in range(1,11)] # x*x 도 가능
# print(f"[2] 1~10까지의 수를 제곱한 값{b}")
# print('-'*140)

# del b[4]
# c = b
# # c = [i * i for i in range(1,11) if i !=5]
# print(f"[3] 1~10까지의 수를 제곤한 값에서 5제곱 값은 제외한 리스트{c}")
# print('-'*140)

# d=[]
# #d = [x for x in range(1,51) if x % 2 !=0]
# for i in range(1,51):
#     if i % 2 !=0:
#         d.append(i)
# print(f"[4] 1~50까지의 수에서 홀수만 출력{d}")
# print('-'*140)

#[5] 함수 사용
# def myFunc(x):
#     x = x *2
#     return x

# e = [x for x in [1,2,-3,4,5,-6,7,8,-9,10]]
# print(e)
# e = [myFunc(x) for x in [1,2,-3,4,5,-6,7,8,-9,10]]
# print(e)
# e = [abs(x) for x in [1,2,-3,4,5,-6,7,8,-9,10]]
# print(e)
# e = [myFunc(abs(x)) for x in [1,2,-3,4,5,-6,7,8,-9,10]]
# print(e)


#문제
'''
a = [i,j for i in range(3) for j in range(3)]
중첨 이중 for 문에 대한 사용법과 진행 순서
'''
# a = [i for i in range(3) for j in range(5)]
# print(a)

a = [i*j for i in range(2,10) for j in range(1,10)]
print(a)

