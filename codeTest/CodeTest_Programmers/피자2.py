t1 = 6
t2 = 10
t3 = 4


def solution(n):
    #한판당 6조각
    #n = 인원수
    pizzabox=6

    if pizzabox %n !=0:
        pizzabox+=6

    print(pizzabox/6)    

solution(t1)
solution(t2)
solution(t3)