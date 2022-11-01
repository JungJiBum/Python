ls1 = [0,1,2,3,4,5]
ls1[1:3] = [11,22,33]
print(ls1)

ls2=[0,1,2,3,4,5]
del ls2[1:3]
print(ls2)
# s = [1,2,3,4,5]
# s.sort(reverse=True)

# a1,a2 = s[:2]
# print(a1,a2)
# print(a1*a2)
'''
최빈값
'''

'''
분수 표현
from fractions import Fraction

Fraction(3,1)
-> 3/1을 분수로 표현한다
t = Fraction(12,8)
-> 12/8을 3/2로 표현해준다.
print(t.numerator) -> 분자 -> 3
print(t.denominator) -> 분모 -> 2
'''

# n = 10
# def solution(n):
#     answer = 0
#     for i in range(0,n+1):
#         print(i)
#         if i % 2== 0:
#             answer +=i

#     return answer

# print(solution(n))


# strlist = ["We", "are", "the", "world!"]
# for i in strlist:
#     print(len(i))

# n=10
# def sol(n):
#     ans=[i for i in range(0,n+1) if i % 2 !=0]
#     return ans
# print(sol(n))


# array=[149,180,192,170]
# height=167

# def sol(array,height):
#     answer = 0
#     for i in array:
#         # print(i)
#         if i > height:
#             print(i, height)
#             answer +=1
#     return answer

# print(sol(array,height))


# array=[1,8,3]

# def solution(array):
#     answer = []
#     # answer = [max(array), array.index(max(array))]
#     answer.append(max(array))
#     answer.append(array.index(max(array)))
#     return answer

# print(solution(array))

# arr=[1,1,2,3,4,5]
# n = 1

# def sol(arr,n):
#     ans=0
#     for i in arr:
#         if i == n:
#             ans+=1
#     return ans

# print(sol(arr,n))

# before = "olleh"
# test = "".join(reversed(before))
# print(test)
# test_1 = before[::-1]
# print(test_1)

# numbers=[1,2,3,4,5,6,7,8,9,10]
# ans=0
# for i in numbers:
#     ans+=i
# print(sum(numbers))
# print(ans)
# print(len(numbers))
# print(ans/len(numbers))


# my_string = "hello"

# for i in my_string:
#     print(i)
