#학생 5명의 수학점수를 입력받아 60점 이상만 합계를 구하는 코드 구현

#[1] 사용자 입력
scores = list(map(int,input("학생 5명의 수학점수를 입력하시오 : ").split()))
sum = 0
scores_num = len(scores)

#[2] socres 리스트 반복돌리면서 60점 이상인 i만 sum 합계
for i in scores:
    if i >= 60:
        sum +=i

print(f"학생{scores_num}명의 입력 점수 중 60점 이상의 합계는 {sum}입니다.")

