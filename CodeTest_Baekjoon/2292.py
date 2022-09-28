n = int(input())

nums_pileup = 1
cnt = 1

while n > 1:
    n-=(6*cnt)
    cnt+=1
print(cnt)