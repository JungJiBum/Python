import turtle

t = turtle.Pen()
t.shape("turtle")
t.pencolor("red")
# t.speed(0)


def move():
    i=0
    for i in range(0,100):
        for j in range(0,50):
            t.forward(10+j)
            t.right(90)
            t.forward(10+j)
            t.right(90)
            t.forward(10+j)
            t.right(90)
            t.forward(10+j)
            j+=1
        t.forward(10)
        t.right(90+i)
        t.forward(10)
        t.right(90+i)
        t.forward(10)
        t.right(90+i)
        t.forward(10)
        i+=1

move()