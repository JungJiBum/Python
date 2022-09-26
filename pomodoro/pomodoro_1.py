'''
pomodoro 타이머는 특수항 유형의 타이머로 생산성을 높이는데 쓰임

작동 방식
>25~30분의 근무 시간을 주고 일을 완성하면(pomodoro 1개 완성) 약 10분의 휴식 시간을 주고 타이머는 이 과정을 반복함
'''
import time
from plyer import notification

# 사용자가 완성한 pomodoro 수량과 pomodoro 타이머가 시작된 표시기를 나타내보자
count = 0
print("The pomodoro timer has started, start working!")

if __name__ == "__main__":
    while True:
        # notify()함수 사이 시간 초과 설정 및 포모도로 완성시 count 변수 증가
        # 첫 번째 알림을 표시하기 전 30분(1800초)을 기다린 다음에 알림을 표시하기 전에 카운트 변수가 30분이 지난 후 점차 증가
        time.sleep(1800)
        # -> 사용자가 포모도로를 완성했다는것을 의미
        count += 1
        notification.notify(
            # notify() 함수는 사용자에게 포모도로가 완성되었음을 알리고 지금까지 count 변수를 사용하여 포모도로가 얼마나 완성되었는지 알려준다.
            title="Good Work!",
            message="Take a 10 minute break! you have completed " + \
            str(count) + " pomodoros so far",
        )
        # 다음엔 10분 휴식 시간이 끝난 후 사용자에게 알릴 notify() 함수를 만들어 보자.
        time.sleep(600)     # 10분(600초)을 기다린 후 사용자에게 10분의 휴식이 끝났다고 알림
        notification.notify(
            title="Back to work!",
            message="Try doing another pomodoro...",
        )
