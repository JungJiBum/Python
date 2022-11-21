# 사용자로부터 임의의 개수의 성적을 입력받아 합계와 평균을 계산한 후
# 출력하는 프로그램 작성 단, 센티널은 음수 값을 사용

cnt = 0
hap = 0
score = 0
avg = 0.0

# 센티널(보초값)을 사용자에게 제시하는 코드
print("종료하려면 음수를 입력하시오.(예 : -1)")

while score >= 0:
    score = int(input(str(cnt+1)+ "번째 학생의 성적을 입력하세요 : "))
    # 음수값인지 검사하는 코드
    if score >= 0:
        hap += score    # 성적의 합계를 구하는 코드
        cnt +=1         # 학생의 수를 누적하는 코드

# 평균을 계산하는 코드
if cnt > 0 :
    avg = hap / cnt

# 합계와 평균을 출력하는 코드
print(f"{cnt}학생의 평균은 {avg} 이며 합은 {hap}이다.")
print(str(cnt)+"학생의 평균은 %.1f이다."%avg)