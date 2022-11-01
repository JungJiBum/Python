# 정수 5개를 원소로 갖는 리스트를 매번 실행할 때마다 다른 난수로 지정
# random 모듈 사용
# 난수 생성 범위 와 난수 결과를 리스트로 출력

#[1] : 모듈 임포트
import random

# #[2] : 랜덤 정수 변환
# n = random.randint(1,100)
# print(n, type(n))

# #[3] : 랜덤 정수 생성 --> 리스트로 반환
# lst = random.sample(range(1,10),5)
# print(lst, type(lst))

'''
난수 모듈
'''
# #[1] : 랜덤 정수 1개
# a = random.randint(1,10)
# print(a)
# #[2] : 랜덤 정수 10개
# try:
#     b = random.sample(range(1,10),10)
#     print(b)
# except ValueError as e:
#     print(e)
# #[3] : 랜덤 정수 10개
# c = random.sample([1,2,3,4,5,6,7,8,9,10],10)
# print(c)
# #[4] : 랜덤 정수 10개
# d = random.sample((1,2,3,4,5,6,7,8,9,10),10)
# print(d)


'''
문자열에서 임의의 문자 하나를 화면에 출력
choice() 함수 사용법
random.choice(). 함수는 매개변수로 시퀀스 자료형을 받는다.
시퀀스 자료형 --> 리스트,튜플,range,문자열 --> 여기서 랜덤으로 요소 하나를 뽑아 반환
빈 리스트 --> X
'''
a = random.choice('koreaKOREA')
print(a)
b = random.choice('korea KOREA')
print(b)
c = random.choice(['k', 'o', 'r', 'e', 'a', 'K', 'O', 'R', 'E', 'A'])
print(c)
d = random.choice([])
print(d)
