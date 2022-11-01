# 숫자 추측 게임 만들기

from random import *
# 1~100까지 난수 발생
rand_num = randint(1,100)
user_num = int(input("숫자를 맞춰보세요 (1~100) : "))
cnt = 0
while True:
    if user_num == rand_num:
        print(f"정답! 게임을 종료합니다.(시도 횟수 : {cnt})")
        break
    elif user_num > rand_num:
        print("입력한 숫자가 큽니다.")
        cnt+=1
    else:
        print("입력한 숫자가 작습니다.")
        cnt+=1
    user_num = int(input("다시 입력해보세요 :" ))
    
    
    
