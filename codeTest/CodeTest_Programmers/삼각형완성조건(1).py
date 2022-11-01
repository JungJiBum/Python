# 내풀이
def sol(sides):
    n = max(sides)
    p = sides.index(n)
    sides.remove(n)
    side = sum(sides)
    if n < side:
        return 1
    else:
        return 2

t1 = [1,2,3]
t2 = [3,6,2]
t3 = [199,72,222]
# print(sol(t1))
# print(sol(t2))
# print(sol(t3))


def solution(sides):
    # print(max(sides))
    # print(sum(sides))
    # print(sum(sides)-max(sides))
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2
    
print(solution(t1))
print(solution(t2))
print(solution(t3))