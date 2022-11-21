# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 만들어보자.
'''
    *
   ***
  *****
 *******
*********
'''

for i in range(1,6):    # i = 1,2,3,4,5
    #공백을 찍는 내부 루프
    for j in range(5-i): # j = 4,3,2,1,0
        print(" ",end="")
    # 별표를 찍는 부분
    for k in range(1, i*2): # k = 1,2 / 1,4 / 1,6 / 1,8 / 1,10
        print("*",end="")
    print()

# 2번째 방법 format() 이용 풀이
for i in range(1,11,2):
    # ^ 는 중앙 정렬 기호 숫자는 자릿수
    print("{:^10}".format("*" * i))

'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''
print("="*30)
#상단 삼각형
for i in range(1,6):    
    for j in range(5-i):
        print(" ",end="")
    for k in range(1, i*2):
        print("*",end="")
    print()
#하단 역삼각형
for i in range(5):    
    for j in range(i):
        print(" ",end="")
    for k in range(10, (i*2)+1, -1):
        print("*",end="")
    print()