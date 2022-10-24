# 사용자로부터 두개의 정수를 입력받아 두수의 합을 구하는 프로그램

# x = input("first number : ")
# y = input("second number : ")
# 이렇게하면 둘다 str형태임 아래 처럼 형변환을 해준다.
x = int(input("first number : "))
y = int(input("second number : "))

sum = x + y
print("두 수의 합은 ", x, "+", y, "=", sum)
