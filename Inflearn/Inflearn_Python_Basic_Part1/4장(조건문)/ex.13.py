'''
대학교 졸업을 위해 140학점을 이수 / 평점 2.0은 되어야 한다.
이것을 프로그램으로 만들자.
사용자에게 이수학점 / 평점을 입력받아 졸업 가능 여부를 확인해보자
'''

hakjum = float(input("학점을 입력하세요 : "))
grade = float(input("평점을 입력하세요 : "))

if (hakjum >= 140) and (grade >= 2.0):
    print("졸업 가능")
else:
    print("졸업 불가")
    