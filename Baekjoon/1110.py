n = int(input()) #입력값
num = n #num 변수는 n과 같은 값
count = 0

while True:
    a = num//10     #2  #6  #8  #4
    b = num%10      #6  #8  #4  #2
    c = (a+b)%10    #8  #4  #2  #6
    num = (b*10)+c  #68 #84 #42 #26

    count+=1
    if(num==n): #1차 num=68 n=26 #2차 num=84 #3차 42 #4차 26
        break

print(count)
