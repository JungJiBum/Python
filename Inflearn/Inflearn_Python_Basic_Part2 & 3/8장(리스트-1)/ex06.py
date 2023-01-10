# 리스트 기초 연산 실습

# 리스트 요소 삽입
# append() : 리스트.append(추가할 요소)리스트 요소의 항상 마지막 끝에 추가됨
# inser() : 리스트.insert(인덱스, 추가할 요소) 원하는 인덱스에 요소를 추가할 수 있음

li1 = ["TV","audio","PC","Keyboard"]
print(f"li1 주소 : {id(li1)} / li1 : {li1}")
# append() 사용
li1.append("Mouse")
print(f"li1 주소 : {id(li1)} / li1 : {li1}")
# insert() 사용
li1.insert(1,"Phone")
print(f"li1 주소 : {id(li1)} / li1 : {li1}")
'''  리스트는 변경 가능한 객체기때문에 하나의 객체를 가지고 주소값이 바뀌지않고 사용함'''

# 리스트 요소찾기
# in, not in 연산자들은 리스트에 요소가 존재하는지 확인
print("="*50)
hero = ["스파이더맨","아이언맨","배트맨","슈퍼맨","홍당무"]
if "배트맨" in hero:
    print("배트맨 존재")
else:
    print("배트맨은 존재안함")

# 리스트에서 요소를 찾을때 해당 요소의 인덱스를 알고자 한다면 index()를 사용하면 된다.
# list에 해당하는 값이 없으면 index()는 에러가 발생한다 하여 조건절과 in, not in 연산자 이용하여 존재 유무 우선 확인

if "홍당무" in hero:
    index = hero.index("홍당무")
    print("홍당무의 인덱스 : ",index)
else:
    print("홍당무가 없다.")

# 리스트에서 요소를 삭제하는 방법
# 1번째 : 리스트.pop(인덱스), 리스트에서 인덱스에 해당하는 요소 삭제 후 반환
# 2번째 : 리스트.remove("요소"), 리스트에서 해당하는 요소가 있으면 삭제 후 반환 안함
# 3번째 : del 리스트[인덱스], 리스트에서 인덱스에 해당하는 요소를 삭제 후 반환 안함
print("="*50)
hero = ["스파이더맨","아이언맨","배트맨","슈퍼맨","태권도","배트맨"]
element = hero.pop(0)
print(f"element : {element} / hero : {hero}")

# remove() 메서드는 리스트의 요소중 중복된 요소가 존재한다면 인덱스가 작은 요소 먼저 제거함
element = hero.remove("배트맨") # remove는 리턴값이없다.
hero.remove("배트맨") # remove는 리턴값이없다.
print(f"element : {element} / hero : {hero}")
value =  "배트맨"
while value in hero:
    hero.remove(value)
print(hero)

# 리스트 모든 요소를 삭제한다면 리스트.clear() 사용
hero = ["스파이더맨","아이언맨","배트맨","슈퍼맨","태권도","배트맨"]
element = hero.clear()
print(element)

# 리스트에 포함된 요소의 갯수를 알고자 할때 count() 사용
hero = ["스파이더맨","아이언맨","배트맨","슈퍼맨","태권도","배트맨"]
cnt = hero.count("배트맨")
print(cnt)

# extend(list 타입의 매개변수)는 리스트를 더하는 함수( += 와 동일)
li1 = [1,2,3]
li2 = [10.1, 20.2]
li1.extend(li2)
print(li1)