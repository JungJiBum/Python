# 사용자로부터 2개의 정수 값을 입력 받고 첫 번째 입력받은 값부터 두번쨰 입력받은값 까지
# 범위에서 3의 배수이고 4의 배수를 제외하고 출력 하는 프로그램 작성

n1,n2 = map(int,input("두개의 수를 입력하세요 : ").split())


for i in range(n1,n2+1):
    # 3의 배수이면서 4의 배수는 제외
    if (i % 3) == 0 and (i%4) == 0:
        continue 
        # continuew는 조건식이 참이면 아래문장을 실행치 아니하고 for 문으로 이동하여 증가함
    print(i)

