# defaultdict 모듈은 딕셔너리 요소를 생성할 때, 키에 기본 값을 지정하는 방법

# 일반적인 딕셔너리 생성, 키의 값으로 값을 알아낼 수 있음
dic = dict()
print(dic)
# 빈 딕셔너리에 "a"라는 키가 없다는 오류 발생
# print(dic["a"])
print(dic.get("a")) #.get() 메소드는 기본값이 None

from collections import defaultdict
# defaultdict 의 아직 모르는 모든 키에 대해서 기본 값을 0으로 정하겠다.
dic = defaultdict(lambda : 0)   # lambda를 이용하여 0을 리턴하게 만듬
# print(dic["a"])
# print(dic["b"])
# print(dic["c"])
# print(dic[519])
# print(dic)
# print(dic.get("b"))
# print(dic.get("c"))
# print(dic.get("a"))
# print(dic.get(519))

print("-"*50)
dic.clear()
dic = defaultdict(int)      # 키에 대한 값을 int형으로 설정하였다.
dic["a"] += 100             # 해당 키에 대한 값에다가 연산을 할 수도 있다.
print(dic["a"])
print(dic["b"])
print(dic["c"])
print(dic[519])
print(dic)

print("-"*50)
dic.clear()
dic = defaultdict(float)      # 키에 대한 값을 float형으로 설정하였다.
print(dic["a"])
print(dic["b"])
print(dic["c"])
print(dic[519])
print(dic)

print("-"*50)
dic.clear()
dic = defaultdict(str)      # 키에 대한 값을 str형으로 설정하였다.
print(dic["a"])
print(dic["b"])
print(dic["c"])
print(dic[519])
print(dic)