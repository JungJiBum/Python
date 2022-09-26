student_heights = input("학생들의 키를 입력하세요 : ").split()
# 156 178 165 171 187

print("학생들의 키 : ", student_heights)
total_height = 0
for i in student_heights:
    total_height += int(i)
print("학생들의 키 합계 : ", total_height)
avg = total_height / len(student_heights)
print("학생들의 평균 키 : ", avg)
