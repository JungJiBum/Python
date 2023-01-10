# 함수를 이용하여 딕셔너리 초기화 코드 실습
# 일반 딕셔너리 초기화 방법
from collections import defaultdict


def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열에 값을 하나가 키가 되고 그 키의 기본값으로 0을 설정
        if letter not in counter:
            counter[letter] = 0
    return counter

# setdefault() 메서드를 이용한 초기화 방법
def countLetters_setdefault(word):
    counter = {}
    for letter in word:
        # 위 함수 counterLetters() 보다 조건절은 줄었지만, 루프를 돌때마다,
        # setdefault()를 반복 호출하기에 비효율적인 코드임
        counter.setdefault(letter, 0)
    return counter

# defaultdict 모듈을 직접 이용하는 방법
def countLetters_defaultdict(word):
    # 이 함수에서는 defaultdict()만 한 번 호출이 일어남
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] += 1
    return counter
    


if __name__ == "__main__":
    dic = countLetters("가나다라마")
    print(dic.items())
    print("-"*50)
    dic = countLetters_setdefault("가나다라마")
    print(dic.items())
    print("-"*50)
    dic = countLetters_defaultdict("가나다라마")
    print(dic.items())

