# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램 만들기

num = int(input("구구단 몇단? : "))

for i in range(1,10):
    # 잘못된 입력 걸러내는 법
    if (num<2) or (num>9):
        print("Wrong input value")
        break
    print(f"{num} * {i} = {num*i}")