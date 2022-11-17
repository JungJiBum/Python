# 피보나치 수열을 구하는 프로그램
# 피보나치 수열이란 앞의 2개의 수를 더해서 다음 수를 결정짓는 수열이다.
# ex) 사용자로부터 13을 입력 받고 난 뒤 피보나치 수열의 값 : 1 1 2 3 5 8

n1 = 1
n2 = 1
n3 = 1

fi = int(input("피보나치 수열을 만들 정수 입력 : "))

for i in range(1, fi):
    if i < 3: # i가 3보다 작을때 n3 는 1이다.
        n3 = 1
    else: # i가 3보다 클때 n3는 n1+n2 이며, n1은 n2값을 가지고 n2는 n3의 값을 가지고있다.
        n3 = n1 + n2 # n3 = 1+1
        n1 = n2 # n1 = 1
        n2 = n3 # n2 = 2
    # 사용자로부터 입력받은 값보다 작은 수만 출력
    if n3 < fi: # n3 값이 fi 값보다 작을때 n3값 출력
        print(n3, end=" ")
