# 리스트에 대한 실습
'''
리스트 정의 :  여러 값을 모아서 하나의 변수에 저장할 수 있는 데이터 타입
'''

city=['서울','대전','대구','부산']

# 리스트의 길이를 알아내고 싶을때 len()함수 사용
print(len(city))
print(city)
# 리스트 인덱스 값 변경
city[1] = '수원'
print(city)

name = input("이름 : ")
age = int(input("나이 : "))
address = input("주소 : ")
tall = int(input("키 : "))
weight = int(input("몸무게 : "))

person = [name,age,address,tall,weight]
