# 리스트 실습
'''
리스트 정의 : 대량의 데이터를 저장할 수 있는 공간을 만들어야하고 이 데이터들을
손쉽게 처리할 수 있는 형태의 데이터의 저장 구조를 의미한다.
'''

# 리스트 선언
scores = []
print("리스트 초기화 값 : ",scores)

# append() 메서드를 사용하여 값 추가
scores.append(30)
print(f"리스트에 30 추가함 : {scores}")

scores.append("Hello")
print(f"리스트에 문자열 추가함 : {scores}")

scores.append(10.1123)
print(f"리스트에 실수 추가함 : {scores}")
print(f"리스트의 크기 : {len(scores)}")

# 리스트 값 변경해보기
# scores[index]은 변수와 동일하다 (중요)
scores[0] = "hello"
print(f"리스트 값 : {scores}")
print(f"리스트 크기 : {len(scores)}")

# 리스트 순회 출력하기
# for 문은 리스트와 궁합이 잘맞다
print("-"*30)
for i in range(len(scores)):
    print(i, scores[i])

print("-"*30)
for i in range(len(scores)):
    # scores[i] = "안녕"
    scores[i] = i +10
    print(i, scores[i])

# 리스트 순회해서 출력하기(두 번째 방법 for 문과 리스트 시퀀스 이용)
print("-"*30)
for i in scores:
    print(i)

# 사용자로부터 입력을 받아서 리스트에 값을 저장하는 코드
print("-"*30)
# nums=[]
# for i in range(5):
#     nums.append(int(input("정수 입력 : ")))
# print(nums)

# list 클래스(속성(멤버변수), 기능(멤버메서드), 생성자) 생성자를 이용한 리스트 만들기
li1 = list()    # 매개변수가 없는 생성자를 호출(붕어빵을 만드는 형태)
print(f"li1 : {li1}")

# 아래와 같이 생성자의 매개변수가 문자열이라면 리스트를 생성할 때 문자 하나하나씩 요소로 가짐
li2 = list("안녕")
print(f"li2 : {li2}")

li3 = list(range(0,5,2))
print(f"li3 : {li3}")

# 내장리스트에 대한 실습
li1 = [12,12.777, "안녕"]
print(f"li1 = {li1}")
print(f"li1[1] = {li1[1]}")
li2 = [["서울",10],["뉴욕",50],["파리",70]]
print(f"li2 = {li2}")
print(f"li2[0][0] : {li2[0][0]}")
print(f"li2[1][1] : {li2[1][1]}")
print(f"li2[2][2] : {li2[2][1]}")
print("-"*30)

# 내장리스트를 더블 루프로 출력하기
for i in range(len(li2)): # li2는 주소의 주소를 가지고 있다. len(li2) = 3이다.
    for j in range(len(li2[i])): # li2[0], li2[1], li2[2]도 주소 값을 지니고있다.
        print(li2[i][j])