# if ~ elif # else(옵션) 실습
score = int(input("성적을 입력하세요 : "))
# 다중 조건 중 하나만 만족하면 그 이후 조건은 검사하지않는다.
if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else: # else 구문은 옵션이지만 다중 조건을 설정할 때는 절대 조건을 명기하면 안된다.
    print("F")
