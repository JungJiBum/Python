# 큐(Queue) -> FIFO(First In First Out), 선입선출, 수도호스, 파이프
'''
먼저 들어간 데이터가 먼저 나오는 방식
큐에서는 삽입할 때 offer(), 추출시 poll() 사용
'''

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

print(queue)
# 인덱스가 제일 빠른 데이터를 추출해야 되기 때문에 인덱스를 매개변수로 준다.
# 인덱스를 안넣어주면 pop()는 맨 마지막 인덱스 데이터를 추출함
print(queue.pop(0))
print(queue.pop())
print(queue)
