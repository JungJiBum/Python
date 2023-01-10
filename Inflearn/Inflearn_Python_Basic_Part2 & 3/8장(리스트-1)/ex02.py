# 학생 성적 처리 프로그램 
# 조건 : 사용자로부터 입력받아 리스트에 저장
# 성적의 평균을 구하고 해당 점수 80점 이상 성적을 받은 학생 수 출력

scores=[]
avg=0
for i in range(1,6):
    score = int(input("성적 입력 : "))
    scores.append(score)
    avg += score
avg = avg / len(scores)
print(f"성적 평균은 {avg} 입니다.")
high=0
for i in scores:
    if i >= 80:
        high+=1
print(f"80점 이상 성적을 받은 학생은 {high}명 입니다.")


# STUDENT = 5         # 전역 상수
# scores = []         #성적 저장 리스트
# score_sum = 0       #성적 합계 저장
# score_aver = 0.0    # 성적 평균 저장
# cnt_80 = 0          # 80점 이상

# for i in range(STUDENT):
#     score = int(input("성적을 입력하세요 : "))
#     scores.append(score)
#     score_sum +=score
#     if score >= 80:
#         cnt_80 +=1

# score_aver = score_sum / len(scores)
# print(f"average is {score_aver}.")
# print(f"80 score is {cnt_80}")