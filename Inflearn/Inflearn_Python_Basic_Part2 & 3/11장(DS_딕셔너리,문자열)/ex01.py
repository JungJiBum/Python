# 딕셔너리(Dictionary) : 사전과 매우 유사함
# 사전에는 단어와 단어의 설명이 저장되어있음
# 파이썬에서는 키(Key)와 값(Value)의 쌍을 저장할수 있는 객체를 딕셔너리라 함

# 딕셔너리 생성 방법 -> {} "키:값" 같은 형태로 요소를 넣어준다.
dict1 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dict1)
# 딕셔너리 키값은 변경 불가능한 객체이어야한다. 문자열이나 숫자를 권장한다.
# 아래는 키값을 리스트로 주니 TypeError 발생
# dict2 = {[1]:"사과", 2:"토마토", 3:"오렌지"}

# 딕셔너리 키값의 자료형은 혼합되어도 된다.(권장하지 않음)
dic2 = {1:"사과", "2":"토마토", (3,):"오렌지"}
print(dic2)

# 공백 딕셔너리 만드는 방법
dic3 = {}
print(dic3)
# set 객체도 역시 {} 사용하기 때문에 혼돈이 있을 수 있다. 하여 set을 생성할땐 내장함수 set() 사용 해야 함
set1 = {1,2,3,4,5}
print(set1)

# 딕셔너리 항목을 추출하는 방법
dic4 = {1:"사과", 2:"토마토", '3':"오렌지"}
# 첫 번째 방법은 [] 안에 키 값을 주면 값을 얻을 수 있다.
print(f"dic4[1]의 값은 : {dic4[1]} / dic4[2]의 값은 : {dic4[2]} / dic4[3]의 값은 : {dic4['3']}" )
# 두 번째 방법은 get()을 사용하는 방법
print("dic4[1]키의 값은 : ",dic4.get(1))
# 만약 키가 딕셔너리에 존재하지 않느면 KeyError가 발생한다.
# print("dic4[5]키의 값은 : ", dic4.get(5)) # 리턴값이 get() 사용하면 None발생
# print("dic4[5]키의 값은 : ", dic4[5])     # 에러발생


a = dic4.get(5, "파인애플")
print(a)

# 키가 딕셔너리에 존재하는지 알아보는 방법
print(1 in dic4)
print(5 not in dic4)

print("-"*40)
# 딕셔너리 항목 추가하는 방법 딕셔너리는 변경 가능한 객체이다. 하여 값을 추가,삭제 해도 동일한 주소값을 가지고있다.
dic5 = {1:"사과", 2:"토마토", '3':"오렌지"}
print("추가 전 : ",id(dic5))
dic5[4] = "파인애플"
print(dic5)
print("추가 후 : ",id(dic5))

print("-"*50)
# 딕셔너리 항목 삭제하는 방법
# pop()을 이용하여 키를 주면 키에 해당하는 항목이 삭제가 됨
dic6 = {1:"사과", 2:"토마토", '3':"오렌지"}
a = dic6.pop(2)
print(a)
print(dic6)
# 또 다른 삭제방법은 del 키워드를 이용한다.
dic7 = {1:"사과", 2:"토마토", '3':"오렌지"}
del dic7[1]
print(dic7)

# 딕셔너리의 모든 항목을 삭제하고자 할 때는 clear() 사용
a = dic7.clear()
print(a)
print(dic7)