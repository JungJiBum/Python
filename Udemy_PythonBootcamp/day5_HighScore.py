student_score = input("학생들의 점수를 입력하세요 : ").split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print("학생들의 점수는 : ", student_score)

high_Score = 0
for i in student_score:
    if high_Score < i:
        print("high_Score값", high_Score)
        high_Score = i
        print("변경된 high_Score 값", high_Score)
print("최종 높은 점수 : ", high_Score)
