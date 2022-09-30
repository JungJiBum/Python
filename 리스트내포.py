'''
list comprehension
리스트명 = [표현식 for 변수 in 반복 가능한 객체 if 조건문]
리스트명 = [표현식 for 변수 in 반복 가능한 객체 for 조건문]
ex)
ls = [i*j for i in range(2,10) for j in range(2,10)]
'''
#기본 구조
rs = []
for i in range(1,11):
    rs.append(i)
# print(rs)

# 내포 활용
rs1 = [i for i in range(1,11)]
# print(rs1)

# 내포 조건
odd_rs = [i for i in range(1,11) if i % 2 !=0]
# print(odd_rs)
even_rs= [i for i in range(1,11) if i % 2 ==0]
# print(even_rs)

# 원소제곱
제곱_rs =[i*i for i in range(1,11)]
# print(제곱_rs)

# 이중 for 문
rs=[]
for i in range(1,5):
    for j in range(1,5):
        rs.append(i*j) # i가 1일때 j 는 1,2,3,4 / i가 2일때 j는 1,2,3,4 반복
# print(rs)

# 내포 활용
# 앞 for 문이 바깥쪽 / 뒤 for문이 안쪽 
rs = [i*j for i in range(1,5) for j in range(1,5)]
# print(rs)

rs = [i+j for i in range(1,5) for j in range(1,5)]
# print(rs)

# 이중 반복문 조건 걸기
rs = [i*j for i in range(1,10) if i % 2 ==0 for j in range(1,10)]
# print(rs)

