# 5만단위로 4회 반복하는 코드(20만)
import time
# 시작시간
start_time = time.time()

# 멀티쓰레드 사용하지않고 20만 카운트
def count(name):
    for i in range(1,50001):
        print(name, " : ", i)

num_list= ['p1','p2','p3','p4']
for num in num_list:
    count(num)
print("----- {} -----".format(time.time() - start_time)) # 176초 걸림