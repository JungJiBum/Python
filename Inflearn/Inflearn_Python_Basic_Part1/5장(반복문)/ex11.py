# 터틀 그래픽을 이용하여 사각형 3개를 그려보자. 단 조건은 사각형은 20도씩 기울어져있음
import turtle

def square():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)

t = turtle.Pen()

for i in range(18):
    t.speed(0)
    t.left(20) #좌측으로 20도 회전

    square()

turtle.exitonclick()