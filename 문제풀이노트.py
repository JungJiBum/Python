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

def solution(arr, k):
    t = sum(arr,[])
    t.sort(reverse=True)
    print(t[k])
    
    answer = 0
    return answer

print(solution([[5,12,4,31],[24,13,11,2],[43,44,19,26],[33,65,20,21]],4))