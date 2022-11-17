'''
BMI 계산기
몸무게와 키를 입력받고 BMI가 20.0이상 ~ 25 미만이면 표준이라 출력
아니면 체중관리 필요하다 출력
BMI = 몸무게 / (키 * 키)
'''

weight = float(input("몸무게(Kg) 입력 : "))
height = float(input("키(Cm) 입력 : "))
height /= 100.0
BMI = weight / (height * height)
print(BMI)
if BMI >=20.0 and BMI <25.0:
    print("표준")
else:
    print("체중관리 필요")