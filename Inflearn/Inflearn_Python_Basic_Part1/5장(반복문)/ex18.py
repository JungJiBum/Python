# 더블 루프를 사용하여 아래와 같이 출력하는 프로그램 작성
'''
출력결과
*
**
***
****
*****
'''
# 싱글 루프
# for i in range(1,6):
#     print("*"*i)

# 1번째 방법 (더블 루프)
for i in range(5):          # 5행 만들기
    # i가 0이기에 +1하여 1개만큼  별을 찍게함
    # 이후 i 값이 증가가 되기 때문에 2번째 루핑 시 별표를 2개 찍게 됨.
    for j in range(i+1):
        print("*", end="")  # *을 찍고 end=""를 통해 줄바꿈을 뺌
    print()

# 2번째 방법 (format함수 이용)
# format 함수는 {} 이용하고 숫자도 같이 이용됨
# format 함수도 인덱스를 활용하여 해당하는 값을 출력할 수 있음
print("int : {}, str : {}, float : {}".format(10,"Hello",10.1))
print("int : {0}, str : {1}, float : {2}".format(10,"Hello",10.1))
print("int : {2}, str : {1}, float : {0}".format(10,"Hello",10.1))

# format() 는 공간 확보 및 0으로 채우는 기능도 지원함.
# 콜론(:)을 기준으로 우측에 > 혹은 < 부등호를 사용해 방향 지정 가능
# 0을 추가하면 0으로 빈칸을 채워주는 기능도 지원함
print("숫자 '{:>5d}'".format(300)) # '  300' 결과로 우측으로 밀어서 5자리를 만듬
print("숫자 '{:<5d}'".format(300)) # '300  ' 결과로 좌측으로 밀어서 5자리를 만듬

for i in range(5):
    print("{:<5}".format("*" * (i+1))) # 좌측으로 밀어서 i+1 만큼 *찍기

# 더블 루프를 사용하여 아래와 같이 출력하는 프로그램 작성
'''
출력결과
*****
****
***
**
*
'''
print("="*20)
# 1번째 더블 루프 방법
for i in range(5,0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 2번째 방법(format함수)
for i in range(6,0,-1):
    print("{:<5}".format("*" * (i-1)))