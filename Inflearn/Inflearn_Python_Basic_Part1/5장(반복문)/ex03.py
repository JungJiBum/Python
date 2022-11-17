# 1부터 사용자가 입력하는 수(num)까지 더해서 합계 구하는 프로그램 작성
# for문 이용

num = int(input("숫자 입력 : "))
sum = 0
for i in range(num):
    sum +=i
print(sum)

