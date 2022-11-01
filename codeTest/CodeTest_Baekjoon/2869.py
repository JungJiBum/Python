#달팽이는 올라가고싶다.
# V미터인 나무 막대를 올라갈거다
# 낮에 A미터 올라간다 / 자는동안 B미터 미끄러진다 / 정상에 올라간 후에는 미끄러지지 않는다.

import math


A, B, V = map(int, input().split())
# cnt = 0
# height = 0
'''======================'''
# while True:
#     cnt += 1
#     height += A
#     if height == V:
#         print(cnt)
#         break
#     height-=B
'''========================'''
day = (V-B)/(A-B)
print(math.ceil(day))
