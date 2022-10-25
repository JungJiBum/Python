# 사용자로부터 태어난 년도를 입력받아 초,중,고,대 학생 분류 중 어디에 해당하는지 출력하는 프로그램
# -> 8 ~ 13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생) 이외는 일반인
from datetime import datetime

this_year = datetime.today().year
birth = int(input("태어난 년도를 입력하세요 : "))
age = (this_year - birth)+1

if age >=8 and age <=13:
    print("초등학생")
elif age >=14 and age<=16:
    print("중학생")
elif age >=17 and age<=19:
    print("고등학생")
elif age>=20 and age<=27:
    print("대학생")
else:
    print("일반인")