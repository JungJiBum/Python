'''
(1) 리스트 - list
(2) 튜플 - tuple
(3) 집합 - set
(4) 딕셔너리(사전) - dict
'''
'''
#[1] 리스타가 없다면...
person1_name= '홍길동'
person1_age = '33'
person1_address= '대한민국'
person1_tel = '010-1234-5678'

print(person1_name)
print(person1_address)
print(person1_age)
print(person1_tel)
# 일일이 해줘야함
#[2] 리스트가 있다면...
person1 = ['홍길동',33,'대한민국','010-1234-5678']
print(person1)
'''

#[1] 정수,실수,문자형 리스트 생성
# int_ls = [1,2,3,4,5]
# flo_ls = [1.0,2.0,3.0,4.0,5.0]
# str_ls = ['a','b','c','d','e']
# print(int_ls,type(int_ls))
# print(flo_ls,type(flo_ls))
# print(str_ls,type(str_ls))

#[2] 리스트 생성 서로 다른 데이터 자료형 값 사용
# INT_LS = [1,2,3,4,5,['a','b''c']]
# INT_FLO_STR = [100,3.14,'korea',[1,2,3]]
# INT_LS_TUP = [1,2,3,[1,2,3],(1,2,3)]
# ALL_LS = [100,3.14,'korea',[1,2,3],(1,2,3),{1,2,3},{'a':100,'b':200,'c':300}]
# print(INT_LS,type(INT_LS))
# print(INT_FLO_STR,type(INT_FLO_STR))
# print(INT_LS_TUP,type(INT_LS_TUP))
# print(ALL_LS,type(ALL_LS))


#[3] 빈 리스트 생성 코드 2가지
# a = [1,2,3,3]
# b = list()
# c = set(a)
# print("빈 리스트 생성 방식 :",a,type(a))
# print("빈 리스트 생성 방식 :",b,type(b))
# print("빈 리스트 생성 방식 :",c,type(c)) #set 함수는 중복값을 가질수 없음

#[4] 인덱스 이용하여 리스트 요소 접근 및 출력
# a = [100,200,300,400,500]
# print("인덱스를 이용한 a 리스트 요소 출력 :",a[0],a[1],a[2],a[3],a[4])
# print(a[-1])

#[5] 리스트에서 특정 요소만 출력
# a = [100,3.14,'korea',[1,2,3,365],(100,200,300,400,500)]
# print(a[2])
# print(a[3][3])
# print(a[4][3])

#[6] 역인덱스 사용하기
# a = [100,200,300,400,500]
# print("인덱스를 이용한 출력 : ",a[:])
# print("역 인덱스를 이용한 출력 : ",a[::-1])

#[7] 반복문 사용하여 인덱스 리스트 값 출력
# a=[100,200,300,400,500,[1,2,3,],(4,5,6)]

# num=0
# for i in a:
#     print(f"{num} = {i}", end="\t")
#     num+=1

#[8] 영어점수를 오름 차순 출력
# eng_scores= [100,40,70,90,60]
# print(eng_scores)
# eng_scores.sort(reverse=True)
# print(eng_scores)
# print(sorted(eng_scores))

# for i in range(len(eng_scores)):
#     print(eng_scores[i], end="\t")
# print()

#[9] 역 인덱스 사용하여 영어 점수를 오름 / 내림 차순으로 출력
# '''점수'''
# eng_scores = [100, 40, 70, 90, 60]
# '''정렬->sort/sorted'''
# eng_scores.sort(reverse=True)

# for i in range(-5, 0):
#     print(eng_scores[i],'(',i,')',end="\t")

#[10]리스트에 새 영어 점수 추가
# eng_scores = [90, 60, 75, 100, 88]
# print(f"원본 : {eng_scores}")
# eng_scores.append(99)
# print(f"추가 : {eng_scores}")
# # eng_scores[5] = 37
# eng_scores[-1] = 37
# print(f"수정 : {eng_scores}")
# # eng_scores.remove(37)
# del eng_scores[-1]
# print(f"삭제 : {eng_scores}")

#[11] 2개의 리스트 하나로 합치기
# a=[0,1,2,3,4]
# b=[5,6,7,8,9]
# c = a+b
# print(f"a+b 병합 리스트 : {c} {len(c)}개 요소")
# d = a*3
# print(f"a*3 병합 리스트 : {d},{len(d)}개 요소")

#[12] 동물의 케이지를 찾아서 출력
# animals=['elephant','hippo','lion','tiger','alligator']
# que = input("케이지를 알고 싶은 동물의 이름을 입력하세요 : ")
# for i in range(len(animals)):
#     if que == animals[i]:
#         print(f"{que} 동물의 케이지는 {i}번 위치에 있습니다.")

# ani_name = input("케이지를 알고 싶은 동물의 이름을 입력하세요 : ")
# ani_index = animals.index(ani_name)
# print(f"{ani_name} 동물의 케이지는 {ani_index}번 위치에 있습니다. {ani_index}번 케이지 약도를 출력하시겠습니까?")

#[13] 리스트에 들어있는 동물 중 중복 제거
# lst = ['dog','hippo','elephant','lion','tiger','alligator','hippo','lion']
# print(set(lst),type(lst))

#[14] 자료구조에 접근시 에러 나는것과 이유
# a=['dog','hippo','elephant','lion','tiger','alligator','hippo','lion']
# print('[1] lion 출력하기 :',a[3])

# b = set(a)
# print(b)
# print('[2] lion 출력하기 :',b[3])

