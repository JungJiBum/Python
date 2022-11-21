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
print("="*10)
# while문을 사용하여 팩토리얼 구하는 예제
# f(1) = 1

i=1
fa = 1

while i <= 5:
    fa *= i
    i+=1

print("5! is %d"%fa)
print("="*10)

# while 문을 사용하여 3단 출력하는 예제
i=1
while i <=9:
    # % 뒤에 오는 숫자들은 출력할 때 자릿수 차지하게끔 만들어 준다.
    # %.1f나 %0.1f나 동일한 자릿값을 출력한다.(소수점 첫째자리만 나타내도록 한다.)
    print("3 * %d = %2d" %(i, 3*i))
    i+=1

print("="*10)
# 1 ~ 100 까지의 3의 배수만 누적값을 구하는 예제
i = 1
hap = 0

while i <=100:
    # 3의 배수인지 판별하는 조건
    if (i % 3) == 0:
        hap +=i
    i +=1

print("1부터 100 사이의 모든 3의 배수의 합은 %d이다." %hap)


# 정수 안의 각 자리수 합을 계산하는 예제
# ex) 1234라면(1+2+3+4)를 계산하는 것
num = 1234
hap = 0
while num > 0:
    digit = num % 10    # 해당하는 자릿수의 값을 구하는 코드
    hap += digit
    num = num // 10

print("1234 정수의 자릿수의 합은 %d 이다." %hap)

