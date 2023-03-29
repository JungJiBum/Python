import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

id_ls = ["muzi", "frodo", "apeach", "neo"]
# 랜덤 리스트 뽑아서 문자 비교하기
word = random.choice(id_ls)
word_length = len(word) # 문자 길이
print("선택된 문자는 {}, 길이는 {}".format(word, word_length))

lives = 6 # 목숨

# 문자열 길이만큼 빈 리스트 생성
display = []
for _ in range(word_length):
    display += '_'

end_of_game = False

while not end_of_game:
    key = input("단어 입력 : ").lower()
    for position in range(word_length):  # 문자열 길이만큼(0,1,2..n)
        text = word[position]  # 텍스트는 랜덤문자열[위치]값
        if text == key: # 입력값이 문자열 텍스트랑 같다면
            display[position] = text # 빈문자열에 텍스트 대입
    print(f"{' '.join(display)}")

    if key not in word: # 만약 입력값이 문자열에 없다면
      lives -=1 # 목숨감소
      if lives == 0: # 만약 목숨이 0이면
        end_of_game = True # 게임 종료
        print("You Lose!")


    if "_" not in display: # 빈문자열에 "_"가 없다면
        end_of_game = True 
        print("You Win!") # 게임 승리
    print(stages[lives])
'''
STEP 1.
랜덤으로 문자열 받기.
값 입력하기
문자열에서 입력한 값이 일치하는게 있는지 없는지 판단하기
STEP 2.
빈 문자열 리스트 만들기
입력한 값 과 랜덤 문자에 일치하는 단어의 위치를 빈 리스트에 표시
STEP 3.
목숨 만들기(lives=6)
입력값이 문자열에 없다면 목숨 차감


'''

# repo = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k=2
# answer = [0] * len(id_ls)
# # print(answer)
# # print(answer[id_ls.index('muzi')])
# test1 = {x: 0 for x in id_ls}

# print(test1)
# print(set(repo))
# for r in set(repo):
#     # test1[r.split()[1]] = test1[r.split()[1]] + 1
#     test1[r.split()[1]] += 1
#     print(f"0번 {r.split()[0]} / 1번 {r.split()[1]} ")
# print(test1)

# for r in set(repo):
#     print(r)
#     if test1[r.split()[1]] >=k:
#         answer[id_ls.index(r.split()[0])] +=1

#     print(answer)

# for _ in range(1,11):
#     print(_)
