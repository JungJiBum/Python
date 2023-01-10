# 인덱싱 : 리스트에서 하나의 요소를 인덱스를 통하여 참조하는 것

li = ["안녕","테스트",10,100,-10]
print(li[2])
# 음수 인덱스는 뒤에서부터 계산. 시작값은 -1
# 아래 두 코드는 동일한 출력을 함
print(li[-2])
print(li[-2+len(li)])

# 슬라이싱(slicing) : 리스트 범위 안에서 범위를 지정하여 원하는 요소들을 선택하는 연산
li1 = ["안녕","테스트",10,100,-10, False, True]
print(id(li1))
#인덱스 값을 통해 부분 리스트를 새로만든다.(끝 인덱스는 제외)
s_li1 = li1[:6]
print(f"s_li1 : {s_li1} / s_li1_ID : {id(s_li1)}")
# 슬라이싱 연산을 할 때, 앞의 인덱스가 생략되면 0부터 시작함
s_li2 = li1[1:]
print(f"s_li2의 주소 값 : {id(s_li2)} / s_li2 : {s_li2}")
# 아래코드는 li1의 값 전부 출력함
print(li1[:])

# 슬라이싱을 통해 값을 변경하는 내용 실습
# 변경시에는 리스트는 하나의 리스트를 가지고 함으로 주소값의 변경이 없다.
words= ["a", "b", "c","d","e"]
print(words)
print(f"words 주소 값 : {id(words)}")
words[1:3] = ["B","C","D"]
print(words)
print(f"words 주소 값 : {id(words)}")
# 아래코드는 요소가 전부 삭제된다.
words = []
print(words)
print(f"words 주소 값 : {id(words)}")
