from day9_art import logo
import os

new_d={}
def start():   
    name = input("이름이 무엇인가요? : ")
    pay = int(input("제시 가격은 어떻게되나요? : %"))
    new_d[name]=pay

    peoples = input("뒤에 누가 더있나요 ? 'yes' or 'no' > ")
    if peoples == 'yes':
        os.system('cls')
        start()
    else:
        a = max(new_d.values())
        for k,v in new_d.items():
            if v == a:
                print(f"당첨자는 {v}원의 금액으로 낙찰이된 {k}님 입니다. 축하드립니다.")

print(logo)
print("비밀 경매 프로그램에 오신걸 환영합니다.")
start()


'''
bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner=""
    #bidding_record = {"name":price,"name1",price1,"name2",price2}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == "yes":
        os.system('cls')


'''