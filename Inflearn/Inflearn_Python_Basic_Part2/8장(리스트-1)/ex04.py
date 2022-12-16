# 시퀀스 자료형 : 순서를 가지는 요소들로 구성된 자료형
# 문자열, 바이트 시퀀스, 바이트 배열, 리스트, 튜플, range() 객체가 존재함
'''
# 시퀀스 자료형 특징
1. 요소들이 순서를 가지고 있음
2. 인덱스를 이용하여 요소들을 참조할 수 있음
'''

words = "Nice To Meet You!"
print(words[0],words[4],words[-1])

li = ["사과","바나나","배","포도","참외"]
# IndexError : list index out of range -> 범위 에러로 리스트 크기만큼 인덱스를 잡아서 사용해야함
print(li[0],li[2],li[-1])

# 시퀀스 길이 구하는 코드
print('words 의 길이 : ',len(words))
print(f"li의 길이 : {len(li)}")

# 시퀀스에서 가능한 연산과 함수
li1 = [1,2]
print(f"li1 주소값 : {id(li1)}")
li2 = [3,4,5]
print(f"li2 주소값 : {id(li2)}")
#시퀀스 자료형은 + 연산이 가능하다.
li3 = li1+li2
print(f"li3 주소값 : {id(li3)}")
print(li3)
# * 연산자는 시퀀스 자료형에서 해당하는 값을 반복시켜서 요소의 수가 증가가 됨
print(['Hello','hi']*3)

# in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 True 없다면 False 반환
print(10 in [10,2,3])
#not in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 False를 반환
print(10 not in[10,2,3])

# 시퀀스 자료형 최대 값
print(max([1,7,-5,15]))

# 자료형 최소 값
print(min([1,7,-5,15]))
# 문자열 리스트에서 max, min 함수는 의미가 없다.
print(max(['Hello',"hi",'가나','안녕']))

# 반복문 시퀀스 자료형이 올 수 있다.
for i in "일이삼" :
    print(i)