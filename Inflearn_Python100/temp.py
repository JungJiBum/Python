# a,b 각각의 벼수에 들어있는 값을 교환 해보자
# a,b에 값은 100, 200 이다

a = 100
b = 200
print("a,b의 값은 =",a,b)

temp = a
a = b
b = temp

print("a,b의 값은 = ",a,b)

#swap 사용
c = 100
d = 200
print("swap 전 c,d 값 = ",c,d)
c,d = d,c
print("swap 후 c,d 값 = ",c,d)