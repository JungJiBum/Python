N = int(input()) #크기 입력
numbers=input() #숫자 입력
rs=0
for i in range(N): # 크기만큼 i가 반복
    rs += int(numbers[i]) # numbers 숫자의 i번째 더하기
print(rs)