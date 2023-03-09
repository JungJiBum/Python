# https://niceman.tistory.com/138
# https://scribblinganything.tistory.com/563
# https://docs.python.org/ko/3.7/library/multiprocessing.html

# python Thread 예제 2
import logging
import threading

def get_logger():       #logger 함수 선언 : 쓰레드 정보 상세 출력
    logger = logging.getLogger("Thread Example")
    logger.setLevel(logging.DEBUG)
    #fh = logging.FileHandler("Thread.log") #로그 파일 출력
    fh = logging.StreamHandler()
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger

def execute(number, logger):        # 쓰레드로 실행할 함수 선언 : logger 함수 출력
    ''' 쓰레드에서 실행 할 함수(로깅사용)'''
    logger.debug('execute function executing')
    result = number * 2
    logger.debug('execute function ended with : {}'.format(result))

if __name__ == "__main__":
    # 로거 생성
    logger = get_logger()
    for i, name in enumerate(['Kim','Lee','Park','Cho','Hong']):
        my_thread = threading.Thread(target=execute,name=name ,args=(i,logger))
        my_thread.start()