# python thread 예제 1
import threading

def execute(number):
    ''' 쓰레드에서 실행할 함수'''
    print(threading.currentThread().getName(),number)


if __name__ == "__main__":
    for i in range(1,8):
        my_thread = threading.Thread(target=execute, args=(i,)) # execute함수 할당
        my_thread.start()   # start 메소드 호출