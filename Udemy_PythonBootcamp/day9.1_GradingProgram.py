student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
'''
91 ~ 100점 -> Outstanding
81 ~ 90점 -> Exceeds Expectations
71 ~ 80점 -> Acceptable
70점 ~ lower -> Fail
'''
#TODO-1 Create an empty dictionary called student_grades
student_grades ={}

#TODO-2 Write your code below to add the grades to student_grades.
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)