import random
from turtle import pos

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list) # 문자열 리스트에서 인덱스값 하나 랜덤으로 뽑음
print(f"Pssst, the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range(word_length): # 랜덤 문자열 기준 만큼 반복함
    display += '_' # 자릿수 만큼 리스트에 '_'문자 입력
print(display)
guess = input("Guess a letter: ").lower() # 입력값을 비교

for position in range(word_length): # 랜덤으로 산출된 문자열의 길이만큼 범위 지정 이때 position 값은 숫자 ex) 0~n
    letter = chosen_word[position] # letter은 랜덤으로 산출된 문자열을 가지고 있는 chosen_word의[position]값 즉 letter = chosen_word[0] 부터 ~ chosen_word[n]까지 반복된다.
    if letter == guess: #입력값과 랜덤 문자열의 단어가 일치할 경우
        display[position] = letter # 디스플레이 리스트의[position] 위치에 letter 값 대입

print(display)