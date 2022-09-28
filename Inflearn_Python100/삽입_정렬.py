# 삽입 정렬 알고리즘
lst = [4,8,1,5,7]

print(f"리스트 초기 값{lst}")

for i in range(1,len(lst)): #리스트 요소가 5개면 4번만 반복
    print("반복문=",i)
    print("인덱스위치에 따른 값=",lst[i])
    # 첫 번째 요소까지 역으로 진행하면서 삽입 위치 찾기
    while i > 0 and lst[i-1] > lst[i]: #i-1이 i보다 클 경우
        print("i-1=",lst[i-1])
        print("i=",lst[i])
        print(f"swap 전 i-1={lst[i-1]}, i={lst[i]}")
        lst[i-1],lst[i] = lst[i],lst[i-1]
        i -=1
        print(f"swap 후 i-1={lst[i-1]}, i={lst[i]}")

print(f"리스트 변환 값{lst}")