def solution(array):
    answer = sorted(array)  # 배열 정렬
    # print(len(answer))
    Index = len(answer)//2
    print(answer[Index])
    return answer[Index]


t1 = [1, 2, 7, 10, 11]
t2 = [-9, -1, 0]


print(solution(t1))
print(solution(t2))
