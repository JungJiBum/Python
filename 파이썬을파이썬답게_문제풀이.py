myls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print("기본 : ",myls)
# print("언패킹 : ",*myls)
# print("기본 맵 함수 : ",list(map(list,zip(myls))))
# answer = list(map(list, zip(*myls)))
# print("언패킹 맵 함수 : ",answer)

# ls=[[], [], []]
# for i in range(len(myls)):
#     # i = 0,1,2
#     for j in range(len(myls[i])):
#         #myls[0]번(0,1,2) / myls[1]번(0,1,2) / myls[2](0,1,2)
#         # print(myls[j][i])
#         ls[i].append(myls[j][i])
# print(ls)

'''zip함수'''
# mylist = [1, 2, 3]
# new_list = [40, 50, 60]
# for i in zip(mylist, new_list):
#     print(i)

# list1 = [1, 2, 3, 4]
# list2 = [100, 120, 30, 300]
# list3 = [392, 2, 33, 1]
# answer = []
# for number1, number2, number3 in zip(list1, list2, list3):
#     print(number1, number2, number3)

# animals = ['cat', 'dog', 'lion']
# sounds = ['meow', 'woof', 'roar']
# answer = dict(zip(animals, sounds))
# print(answer)

ls=[83,48,13,4,71,11]
answer=[]
# for i in range(len(ls)):
    
#     if i ==len(ls)-1:
#         pass
#     else:
#         answer.append((abs(ls[i] - ls[i+1])))
# print(answer)

# for ls1,ls2 in zip(ls,ls[1:]):
#     answer.append(abs(ls1 - ls2))
# print(answer)

ls=['1','100','33']
# def sol(ls):
#     # ans=[list(map(int,ls))]
#     ans=list(map(int,ls))
#     return ans
# print(sol(ls))

# ls2=[]
# for i in ls:
#     ls2.append(int(i))
# print(ls2)

# ls=[[1],[2]]
# ls2=[[1,2],[3,4],[5]]
# def sol(ls):
#     ans = list(map(len,ls))
#     return ans
# print(sol(ls))
# print(sol(ls2))

str = 'ABC'
str1 = 'xy'
# for v in str:
#     for v1 in str1:
#         print(v,v1)
# import itertools
# print(list(itertools.product(str,str1)))

'''2차원 리스트 1차원 리스트 만들기'''
ls=[[1],[2]]
ls1=[['a','b'],['x','y'],['1']]
# print(sum(ls,[]))
# print(sum(ls1,[]))

# t=[]
# for i in ls1:
#     t += i
# print(t)

# from itertools import permutations
# ls = [2,1]
# ls1= [1,2,3]

# print(list(permutations(ls,2)))
# print(list(permutations(ls1,3)))
# print(list(permutations(ls1,len(ls1))))

'''알파벳 찾기'''
'''사전 오름차순/내림차순'''
'''collections 라이브러리'''
# import collections
# str = 'dfdefdgf'
# ans = collections.Counter(str)
# # print(ans)
# print(max(ans,key=ans.get))
# print([k for k,v in ans.items() if max(ans.values()) == v])

# for k,v in ans.items():
#     if v == max(ans.values()):
#         print(k,end='')

# ls = [1,2,3,4,5,6,7,8,9,10]
# print([x*x for x in ls if x % 2== 0])

