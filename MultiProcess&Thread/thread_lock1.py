# python Thread Synchronization(동기화) 예제 1
import threading

tot = 0 # 쓰레드에서 참조할 변수 선언

def add_total(amount):  # 쓰레드에서 참조할 함수 선언
    '''
    쓰레드에서 실행 할 함수
    전역변수 tot에 amount 더하기
    '''
    global tot
    tot += amount
    print(threading.currentThread().getName()+'Not Synchronized : ',tot)

# 동기화가 되어있지 않은 쓰레드 예제
if __name__ == "__main__":
    for i in range(10000):
        my_thread = threading.Thread(
            target=add_total,args=(1,))
        my_thread.start()