import turtle
# 펜의 기능을 t라는 변수에 저장
t = turtle.Pen()

#무한루프를 돌려서 if 구문을 이용하여 방향 제어 코드 작성
#반드시 탈출하는 코드가 있어야함(중요)

while True:
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit >>>")
    # break는 무한루프 탈출 하기위해 작성
    if direction == 'quit':
        print("종료")
        break
    
    if direction == 'left':
        t.pencolor("red")
        print("left 입력")
        t.left(60)
        t.forward(50)
    
    if direction == 'right':
        t.pencolor('blue')
        print("right 입력")
        t.right(60)
        t.forward(50)

# 터틀 그래픽 창이 클릭되어야 화면에서 사라지는 코드
turtle.exitonclick()