# 임의의 숫자를 발생시켜 사용자로부터 입력을 받아 숫자를 맞추는 게임을 만들어보기
from random import *

cnt = 0
num = randint(1,100)
print("발생된 난수의 값은 : {}".format(num))

print("1~100사이의 숫자를 맞추어 보시오.")
print("기회는 10번 입니다.")

while cnt <10:
    guess = int(input("숫자를 입력하시오 : "))
    cnt +=1

    if guess == num:
        print("정답입니다.")
        print(f"{cnt}회 만에 맞추셨습니다.")
        # 게임을 계속 진행할지 파악하기위한 조건문
        code = input("게임을 계속 하시겠습니까?(y/n) : ")
        if code  == "n":
            print("게임 종료.")
            break
        else:
            print("======================")
            print("게임을 재시작 합니다.")
            #게임을 재시작하면서 난수와 카운트를 초기화
            num = randint(1,100)
            print("발생된 난수의 값은 : {}".format(num))
            cnt=0

    elif guess > num:
        print("입력한 수가 큽니다.")
        print(f"{10-cnt}회 남았습니다.")

    else:
        print("입력한 수가 작습니다.")
        print(f"{10-cnt}회 남았습니다.")

print("기회를 모두 소진되었습니다. 게임이 종료되었습니다.")