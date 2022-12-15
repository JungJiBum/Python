# 원의 면적과 원의 둘레를 구하는 프로그램 작성
# PI = 3.141592 > 대문자로 선언하면 상수라 인식하고 변경하지않는 값
# 전역상수 선언하고 상수를 활용하도록 한다.

# 전역 상수 선언
PI = 3.141592

# 프로그램 시작하는 함수
def main():
    radius = float(input("원의 반지름을 입력하세요 : "))
    print(f"원의 반지름은 {radius}, 원의 면적은 {circle_area(radius)}")
    print(f"원의 반지름은 {radius}, 원의 둘레는 {circleCircumference(radius)}")

# 원의 면적을 구하는 함수
# 원의 면적 공식 -> PI * 반지름의 제곱
def circle_area(radius):
    return PI * radius * radius

# 원의 둘레를 구하는 함수
# 원의 둘레 공식 -> 2 * PI * radius
def circleCircumference(radius):
    return 2 * PI * radius

# 프로그램의 시작을 알리는 함수 호출
main()