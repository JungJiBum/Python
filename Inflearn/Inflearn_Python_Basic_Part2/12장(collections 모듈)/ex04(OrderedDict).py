# 일반 딕셔너리를 정렬을 하여 OrderedDict로 포장하기
dic = {}
dic["b"] = 100
dic["a"] = 200
dic["d"] = 300
dic["c"] = 400
dic["e"] = 500
dic["f"] = 500
dic["g"] = 500
dic["h"] = 500
dic["1"] = 500
dic["6"] = 500
dic["3"] = 500
# 키, 값으로 정렬
print(dic, type(dic))
print(sorted(dic),type(sorted(dic)))
li1 = sorted(dic.keys())
li2 = sorted(dic.values())
print(li1, type(li1))
print(li2, type(li2))
print(dic["3"])
print(dic["a"])
print("-"*50)
from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리 요소
# 하여 0 인덱스는 키값이 될것이다
# 딕셔너리를 정렬하면 타입이 list로 변환
def sort_by_key(t):
    return t[0]

dic1 = {}
dic1["z"] = 500     # z : 100
dic1["a"] = 800
dic1["e"] = 100
dic1["d"] = 400
# 일반 딕셔너리 내용을 sorted()를 이용하여 정렬을 하면 키를 기준으로
# 정렬된 리스트가 리턴된다. OrderDict()로 포장(wrapping)을 함
# 기존 딕셔너리나 리스트 순서를 지키면서 딕셔너리 형태로 관리할 수 있음
for k,v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
    print(k,v)

# li3 = sorted(dic1.items(), key=sort_by_key)
# print(dic1, type(dic1))
# print(li3, type(li3))

# 딕셔너리 동등성 비교
# 동등성은 논리적 동등이라는 것을 의미함. 논리적 동등이란 주소는 다르지만
# 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라 본다.
dic1 = {"가":1, "나":2, "다":3}
dic2 = {"가":1, "다":3, "나":2}
print(id(dic1))
print(id(dic2))
print(dic1 ==dic2)
print("-"*50)
from collections import OrderedDict
# OrderedDict는 두개의 OrderedDict 를 비교할 때 해당하는 값들의
# 순서와 해당하는 키, 값이 같아야지만 동등하게 바라봄
orderded_dic1 = OrderedDict({"가":1, "나":2, "다":3})
orderded_dic2 = OrderedDict({"가":1, "다":3, "나":2})
orderded_dic3 = OrderedDict({"가":1, "나":2, "다":3})
print(id(orderded_dic1))
print(id(orderded_dic2))
print(orderded_dic1 == orderded_dic2)
print(orderded_dic1 == orderded_dic3)

# 결론
# 1. OrderedDict 모듈은 딕셔너리 순서대로 저장하지 않는 방식을 순서대로
# 저장하는 방식으로 개선됨 (파이썬 버전 3.6이후로 저장과 출력이
# OrderedDict 와 동일하게 작동하고 있지만 2.x 버전에서는 문제점이 발생한 것을 봄)
# 2. 딕셔너리 동등성 비교에서 일반적인 딕셔너리는 순서를 유지하지 않아도
# 해당 키와 값이 동등하다면 True 리턴하지만, OrderedDict 에서는 순서, 키, 값이 동등해야 True를 리턴
# 좀 더 깐깐한 동등성 비교로 개선
# OrderedDict를 사용하면 정확한 데이터 순서나 값을 유지하는데 일반 딕셔너리에 비해서는 엄청 좋은면이 존재함


