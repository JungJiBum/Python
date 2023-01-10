# deque와 list의 성능 테스트 비교
from collections import deque
import time     # 성능 테스트를 하기위해 time 모듈 호출
# 아무런 요소가 없는 deque를 생성함
deque_test = deque()
start = time.time()     #시작 시간 저장(second 단위)
for i in range(100000000):
    deque_test.append(i)
end = time.time()
print("deque append 시간 : ", end - start)

# 빈 리스트 생성
list = list()
start = time.time()     #시작 시간 저장(second 단위)
for i in range(100000000):
    list.append(i)
end = time.time()
print("list append 시간 : ", end - start)

print("-"*50)
# 추출 기능 테스트

# start = time.time()     #시작 시간 저장(second 단위)
# for i in range(100000000):
#     deque_test.pop()
# end = time.time()
# print("deque pop time : ",end-start)

# start = time.time()     #시작 시간 저장(second 단위)
# for i in range(100000000):
#     list.pop()
# end = time.time()
# print("list pop time : ",end-start)

start = time.time()     #시작 시간 저장(second 단위)
for i in range(100000000):
    deque_test.pop()
end = time.time()
print("deque popleft() time : ",end-start)

start = time.time()     #시작 시간 저장(second 단위)
for i in range(100000000):
    list.pop(0)
end = time.time()
print("list pop(0) time : ",end-start)

# 결론은 list, deque를 성능 테스트해보니 데이터를 추가할때는 deque가 훨씬 좋은 성능
# 또한 대용량일수록 더욱더 많은 차이를 나타냄 삽입 역시 deque가 훨씬 빠름
# 추출 역시 deque가 list보다 훨씬 빠른 성능을 보임.
# 데이터 용량이 크면 클수록 deque를 사용하는것을 고려해봐야 함

