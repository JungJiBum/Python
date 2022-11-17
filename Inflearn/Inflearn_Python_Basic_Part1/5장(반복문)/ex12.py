# while 실습
# while 문은 조건을 정해놓고 반복하는 구조

i = 0
while i < 5 :
    print("Hello")
    i +=1 # 해당 코드가없다면 while문은 무한 루프를 돌것
print("While is done")

# 숫자 0~9까지 줄바꿈 없이 출력해보기
i = 0
while i < 10:
    print(i, end=" ")
    i +=1

# 1~10 까지 누계합을 구하는 프로그램 작성
i=0
hap=0
while i <= 10:
    hap+=i
    i+=1
print()
print(hap)

# while문을 사용하여 팩토리얼 구하는 예제
# f(1) = 1

i=1
fa = 1

while i <= 5:
    fa *= i
    i+=1

print("5! is %d"%fa)


# while 문을 사용하여 3단 출력하는 예제
i=1
while i <=9:
    print("3 * %d = %2d" %(i, 3*i))
    i+=1