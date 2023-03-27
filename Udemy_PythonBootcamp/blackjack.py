import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# card_logo= ['♥' '♣' '♠' '◆']
'''
블랙잭
게임 설명 : 
시작하면 카드를 2장 받음 -> 받고나서 합 체크(카드의 합이 21을 넘기면 패배)
유저가 먼저 카드를 받을거면 y 아니면 n
카드를 받았을때 21이거나 가까우면 승리, 

'''


def val_check(card):
    value = sum(card)
    if value >= 22:
        # print(value)
        print("Bust")
    if value == 21:
        # print(value)
        print("Blackjack")


print("Let's go to the blackjack")
''' 카드 할당 '''
user = random.sample(cards, 2)
dealer = random.sample(cards, 2)

print(f"user cards = {user} / dealer cards = {dealer}")

''' 숫자 체크 '''
val_check(user)
val_check(dealer)

choose = input("Hit or Stay? : ")
if choose == "hit":
    card = random.choice(cards)
    print(card)
    user.append(card)
val_check(user)
if choose == "stay":
