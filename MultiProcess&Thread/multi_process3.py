#멀티프로세스의 프로세스 객체를 활용해 10만단위 4회 반복(40만)
from multiprocessing import Process
import time
import os

#시작시간
start_time = time.time()

# 멀티쓰레드 사용(40만카운트출력)
def count(cnt):
    proc = os.getpid()
    for i in range(cnt):
        print(f"Process ID : {proc} -- {i}")

if __name__ == "__main__":
    # 멀티쓰레딩 Process 사용
    num_arr = [100000, 100000, 100000, 100000]
    procs = []

    for index, number in enumerate(num_arr):
        #Process 객체 생성
        proc = Process(target=count, args=(number,))
        procs.append(proc)
        proc.start()
    
    #프로세스 종료 대기
    for proc in procs:
        proc.join()
#종료시간
print("-----{} seconds -----".format(time.time() - start_time))