# 소수를 2부터 계속 더할 때, 2000까지 루프를 돌리고, 소수와 합계
# 그리고 마지막 더해지는 소수는 얼마인지 출력하는 프로그램
'''소수는 1보다 큰 정수, 자기자신으로만 나누어지는 수를 의미함'''
# 더블루프, 조건식


start_num = 0
num = 0
hap = 0
lastData = 0

for num in range(2,2001):   #2,3,4....1998,1999,2000
    for start_num in range(2,num+1):  # 2,3 / 2,4 / 2,5 / .... 2,1999 / 2,2000 / 2,2001
        # 배수이거나 소수인지 걸러내는 조건식
        if num % start_num == 0: 
            break # 내부 루프를 빠져나오는 것
    

    # 아래 조건이 참이다 라는 것은 자기자신으로 나누어서 나머지가 0이 나온
    # 것은 바로 소수를 의미하므로 아래 코드를 실행함
    if num == start_num:
        print("소수 : " , start_num)
        hap += start_num
        print("합계 : " , hap)
        lastData = start_num
        print("마지막 소수의 값 : ", lastData)
        print("="*20)