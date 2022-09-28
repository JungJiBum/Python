#N개의 숫자중 X보다 작은 숫자를 모두 출력
N,X = map(int,input().split())
#N과 X는 입력받는다.
num = list(map(int,input().split()))
#N개의 숫자만큼 num 리스트에 입력한다.

for i in range(N):
    #N만큼 반복한다.
    if num[i] < X:
        #만약 num리스트의 i번째 숫자가 X보다 작을때
        print(num[i], end = " ")
        #num리스트의 i번째 값을 출력해라