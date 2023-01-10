# 문자열에 대한 실습
# 슬라이싱이란 것은 문자열에서 부분문자열로 만드는 작업을 의미함
word = "Python"
word1 = word[0:3]
print(word1)
# 파이썬에서 슬라이싱 할때 시작 인덱스, 종료인덱스를 적절치 못한 값을 사용하더라도
# 파이썬 인터프리터가 자동으로 적절한 값으로 변경하여 실행 시켜줌.
print(word[0:100])
print(word[2:100])
print("-"*50)
# 문자열 비교하기(연산자)
print("apple" < "banana")
# ord()는 영문자를 아스키코드로 출력해주는 함수
print(ord("a")) #97
print(ord("b")) #98
# chr()는 아스키코드를 주면 해당하는 문자를 출력해주는 함수
print(chr(97))  #a
print(chr(65))  #A
# ascii()함수는 문자열이 알파벳이면 알파벳은 그대로 출력
# 알파벳이 아니면 유니코드로 변경해서 출력
print(ascii("a가나다라마"))

i = 65
while True:
    print(chr(i), end=" ")
    i+=1
    if i > 130:
        break