'''중앙값'''
# import numpy as np
# ls = [1, 2, 7, 10, 11]
# ls2 = [9, -1, 0]
# size = len(ls)

# for i in range(0, size):
#     print(f"{i}번째 요소 {ls[i]}")


# print(np.median(ls))
# print(np.median(ls2))

'''최빈값'''

# from collections import Counter
# def sol(arr):
#     ans = Counter(arr)
#     a = [k for k, v in ans.items() if max(ans.values()) == v]
#     # print(a)
#     # print(len(a))
#     if len(a) >= 2:
#         print(-1)
#     else:
#         print(a)
#     return ans


# print(sol([1, 2, 3, 3, 3, 4]))
# print(sol([1, 1, 2, 2]))
# print(sol([1]))

'''피자 나눠먹기'''

# print(15/7)  # 나누기 2.142857142857143
# print(15 % 7)  # 나머지 1
# print(15//7)  # 정수 몫 2


# def sol(n):
#     ans = 0
#     if n % 7 != 0:
#         return (n//7)+ans + 1
#     else:
#         return int((n/7))


# print(sol(7))


# dict ={
#     "a":1,
#     "b":{1:['a','b'],2:['ste']},
#     "c":3,
# }
# print(dict['b'][2][0])

# i=0
# while i<=5:
#     print("*"*i)
#     i +=1

# for i in range(5):
#     print("*"*i)