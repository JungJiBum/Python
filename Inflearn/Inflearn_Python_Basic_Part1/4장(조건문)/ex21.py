# 학점을 세부적으로 나누는 프로그램을 작성하기
'''
조건
1. 사용자로부터 점수를 입력받는다.
2. 점수가 95 이상/ 100이하라면 A+을 출력한다.
3. 점수가 90이상 / 94 이하라면 A0를 출력한다.
다른 B,C,D 학점도 위와 같이 출력한다.
단 F는 그냥 출력하도록하자
'''

score = int(input("학점을 입력하세요. : "))
grade = ""

if score >= 90:
    if score >=95:
        grade = "A+"
    else:
        grade = "A0"
elif score >= 80:
    if score >=85:
        grade = "B+"
    else:
        grade = "B0"
elif score >=70:
    if score >=75:
        grade = "C+"
    else:
        grade = "C0"
elif score >=60:
    if score >=65:
        grade = "D+"
    else:
        grade = "D0"
else:
    print("당신의 점수는 ",score,"이며, 학점은 F입니다.")

print("당신의 점수는 ",score,"이며, 학점은 ",grade, "입니다.")
