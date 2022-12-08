# import turtle

# t = turtle.Pen()
# t.shape("turtle")
# t.pencolor("red")
# # t.speed(0)


# def move():
#     i=0
#     for i in range(0,100):
#         for j in range(0,50):
#             t.forward(10+j)
#             t.right(90)
#             t.forward(10+j)
#             t.right(90)
#             t.forward(10+j)
#             t.right(90)
#             t.forward(10+j)
#             j+=1
#         t.forward(10)
#         t.right(90+i)
#         t.forward(10)
#         t.right(90+i)
#         t.forward(10)
#         t.right(90+i)
#         t.forward(10)
#         i+=1

# move()


from turtle import *

color('pink','pink')
pensize(3)
begin_fill()
hideturtle()

def curve():
    for i in range(100):
        right(2)
        forward(2)

left(140)
forward(111)
curve()

left(120)
curve()
forward(111)
end_fill()
mainloop()
