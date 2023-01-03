# collections 모듈이란 기존에 배웠던 자료구조(리스트, 큐, 스택, 튜플, 딕셔너리)
# 좀 더 확장하여 제작된 파이썬 내장 모듈이다.
# 1) deque(데크, double-ended queue) 모듈은 스택과 큐를 모두 지원하는 모듈
# -> 양방향으로 데이터를 입출력 할 수 있는 자료 구조

from collections import deque
# 아무 요소가 없는 데크 생성
deque_list = deque()
print(deque_list)
# 아래 코드는 기존 리스트와 같이 데이터가 추가됨을 알 수 있음
for i in range(5):
    deque_list.append(i)
print(deque_list)
# deque 에 있는 요소 삭제하기
# print(deque_list.pop(0)) -> deque에서는 pop(0) 지원 안됨
# deque에서는 스택도 지원하는 모듈이므로 pop()을 사용하면 늦게 들어간 데이터부터 삭제
print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)
print("-"*50)
# appendleft() 메소드 사용 -> 새로운 요소들을 왼쪽부터 입력하여
# 먼저 들어간 값부터 출력될수 있도록 함, 양방향으로 데이터 입력이 가능한 것
deque_list.clear()
print(deque_list)
for i in range(5):
    deque_list.appendleft(i)
    print(deque_list)
print(deque_list)

print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)
print("-"*50)

# deque 모듈은 원형 연결 리스트(Linked List)의 특성을 지원한다.
# 연결리스트는 데이터 저장을 할 때, 요소의 값을 한 쪽으로 연결 후 
# 요소의 다음 값의 주소값을 저장하여 연결하는 기법이다.
deque_list.clear()
print(deque_list)
for i in range(5):
    deque_list.appendleft(i)
print(deque_list)
# rotate() -> 요소들을 n만큼 회전해주는 메소드이다.
# 단, 양수이면 시계방향(오른쪽) / 음수이면 반시계방향(왼쪽)으로 이동
deque_list.rotate(-1)
print(deque_list)
deque_list.rotate(1)
print(deque_list)
print("-"*50)
# reversed() -> 메소드는 기존 요소를 반대로 저장할 수 있게 하는것
print(deque(reversed(deque_list)))
print("-"*50)
# extend() ->리스트를 우측에 통째로 붙임
# extendleft() -> 리스트를 좌측에 통째로 붙임
deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([7,6,5])
print(deque_list)
print("-"*50)
deque_list.clear()
print(deque_list)
basedata = ["a","b","c","d","e"]
# maxlen 매개변수는 deque의 사이즈를 고정을 시켜버리는 인자값이다.
deque_list = deque(basedata, maxlen=3)
print(deque_list)
# popleft() 메소드는 deque에서 요소의 왼쪽에 있는 것을 삭제함
print(deque_list.popleft())
print(deque_list)