dict_ = {}

dict_['ID'] = 'hong'
dict_['name'] = '홍길동'
dict_['age'] = 20
dict_['hp'] = '010-1234-5678'
dict_['address'] = 'korea'

# print(dict_)
# #키값은 중복되지 않는다
# dict_['name']='김길동'
# print(dict_)

# # 데이터 값에 접근할 때는 key를 참조항여 접근해야한다.d
# print(dict_['address'])
# # print(dict_[1])

# print(dict_['ID'])
# print(dict_['name'])
# print(dict_['hp'])
# print(dict_['age'])


#반복운을 사용한 데이터 출력 -Key
# for i in dict_.keys():
#     print(i, end =" ")
# print()
# print('-'*140)

# # value값 출력
# for i in dict_.values():
#     print(i, end = " ")
# print()
# print('-'*140)


# #key,values 모두 출력 -->(key, value) 하나의 쌍으로 출력 --> tuple
# for i in dict_.items():
#     print(i, end = " ")
# print()
# print('-'*140)


# emmty dict 만들기
# a = dict()
# b = {}
# print(a, type(a))
# print(b,type(b))
# print('-'*140)

# # 가독성
# dict1 = {
#     'name' : '홍길동',
#     'id' : 'hong',
#     'age' : 20
# }
# print(f"가독성 :{dict1}")
# print(f"가독성 :{dict1['name']}")


#중첩 딕셔너리 Nested Dictionary

# dict2 = {
#     'name':'을지문덕',
#     'age':  30,
#     'pasttime':{
#         'reading':30,
#         'walking':60
#     },
#     'address':'Korea'
# }
# print(dict2)
# print(dict2['pasttime'])
# print(dict2['pasttime']['walking'])

#삽입 , 수정 , 삭제
dict3={
    'name':'홍길동',
    'id':'hongkildong'
}
print(f"기본 dict3 : {dict3}")
print('-'*140)
dict3['age']=22
print(f"딕셔너리 삽입 {dict3}")
print('-'*140)
dict3['age']=33
print(f"딕셔너리 수정 :{dict3}")
print('-'*140)
del dict3['age']
print(f"딕셔너리 삭제 {dict3}")
print('-'*140)