# def solution(s):
#     s_lst = list(s)
#     n = len(s)
#     for i in range(n):
#         if s_lst[i] == 'a':
#             s_lst[i] = 'z'
#         elif s_lst[i] == 'z':
#             s_lst[i] =  'a'
#     return (s_lst)

# s="abz"
# print(solution(s))

# def sol(price,money):
#     print(sum(price))
#     print(money)
#     ans= abs(sum(price) - money)
#     return ans

# print(sol([2100,3200,2100,800],10000))

# def solution(arr, k):
#     t = sum(arr,[])
#     t.sort(reverse=True)
#     print(t[k])
    
#     answer = 0
#     return answer

# print(solution([[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]],4))

'''에라토스테네스의 체'''
# n=10
# a = [False,False] + [True]*(n-1)
# primes=[]

# for i in range(2,n+1):
#     print(i)
#     print(a[i])
    # if a[i]:
    #     primes.append(i)
    #     for j in range(2*i, n+1, i):
    #         a[j] = False
# print(primes)

'''배열 유사도'''
# set().intersection()
