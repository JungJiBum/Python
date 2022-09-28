# 가위바위보 게임
'''
바위 - 0
보 - 1
가위 - 2
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# 사용자 입력
user_choice = int(input("너는 무엇을 고를것이냐(0-바위,1-보,2-가위) : "))
# 입력한 숫자에 맞는 표시
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)
# 컴퓨터 입력
computer_choice =  random.randint(0,2)
print(f"Computer chose {computer_choice}")
# 랜덤 숫자에 맞는 표시
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("User Win!")
elif (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    print("Computer Win!")
elif computer_choice == user_choice:
    print("Draw!")
else:
    print("Wrong choice")