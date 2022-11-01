import numpy

def sol(n,k):
    if str(k) in str(n):
        print(str(n).index(str(k))+1)
    else:
        print(-1)


t1=29183
t2=232443
t3=123456
k1=1
k2=4
k3=7

print(sol(t1,k1))
print(sol(t2,k3))
print(sol(t2,k3))