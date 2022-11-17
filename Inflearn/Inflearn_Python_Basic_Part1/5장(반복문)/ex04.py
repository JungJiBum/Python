# 1 ~ 100 까지 누적값을 구하는데 누적값 2000이상이 되면 for문 빠져나오는 프로그램

sum = 0
for i in range(1,101):
    if sum >= 2000:
        print("마지막 더해지는 i 값",i)
        break
    else:
        sum= sum+i
print(sum)