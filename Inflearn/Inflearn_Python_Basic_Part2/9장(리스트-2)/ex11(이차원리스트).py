# 2차원 리스트에 대한 실습

double_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
# # 해당 값 출력해보기
# print(double_list)
# print(double_list[0])
# print(double_list[1])
# print(double_list[2])
# # 해당  ID 출력해보기
# print(id(double_list))
# print(id(double_list[0]))
# print(id(double_list[1]))
# print(id(double_list[2]))
# # 해당 리스트 길이 출력해보기
# print(len(double_list))
# print(len(double_list[0]))
# print(len(double_list[1]))
# print(len(double_list[2]))

for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j], end='\t')  #tab 만큼 띄운다.
    print() # 줄바꿈

# 2차원 리스트는 정적 보다 동적으로 생성하여 사용하는 경우가 많다.
# rows = int(input("행 입력 : "))
# cols = int(input("열 입력 : "))
# dbl_list = []
# 일반적인 2차원 리스트 동적 생성 방법
'''
for row in range(rows):
     dbl_list += [[0] *  cols]
'''
# 리스트 함축을 이용한 방법
'''
dbl_list = [([0] * cols ) for row in range(rows)]
print(dbl_list)
'''
# 1차원 리스트에서는 list1[0]값이 바로 변수와 동일함
# 2차원 리스트에서는 list2[1][1]값이 바로 변수와 동일함
li1 = [1,2,3]
li1[0] = 10     #1차원 리스트에 값을 저장하는 형태
print(li1)
li2 = [[1,2,3],[4,5,6],[7,8,9]]
li2[0][0] = 10  #2차원 리스트에 값을 저장하는 형태
print(li2)
