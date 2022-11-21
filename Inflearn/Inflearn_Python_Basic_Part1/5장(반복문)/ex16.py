'''
플래그 변수를 사용한 무한 루프 문제
1.증속, 2.감속, 3.중지를 출력하고 사용자의 입력을 1,2,3 으로 받아서
증속을 하면 속도를 10씩 증가
감속을 하면 속도를 10씩 감소
중지를 하면 플래그 변수를 이용하여 무한루프를 빠져나간다.
'''

run = True
speed = 0
keyCode = 0

while run:
    print("="*20)
    print("1.증속 | 2.감속 | 3.중지")
    print("="*20)
    keyCode= int(input("입력 : "))
    if keyCode == 1:
        speed +=10
        print("Current Speed : ", speed)
    elif keyCode == 2:
        speed -=10
        if speed < 0:
            print("The speed cannot be negative. Shall we go back?")
            speed=0
        else:
            print("Current Speed : ", speed)
    elif keyCode == 3:
        run = False
        print("Current state : ", run)
    else:
        print("Wrong input")

print("Program Exit")