# 자동 판매기 시뮬레이션 프로그램
'''
사용자는 1000원 권 지폐, 500원, 100원짜리 동전을 사용할 수 있다.
물건값을 사용자로부터 입력받아 각각 지폐와 동전 개수를 입력하여 거스름돈을 계산하여
동전으로 반환하는 프로그램을 만들어보자
'''

itemPrice = int(input("물건값을 입력하세요. : "))
bills_1000 = int(input("1000원 지폐 개수 입력 :  "))
coins_500 = int(input("500원 동전 개수 입력 :  "))
coins_100 = int(input("100원 동전 개수 입력 :  "))

# 거스름돈 구하기
nod_money = ((bills_1000 * 1000) + (coins_500 * 500) + (coins_100 * 100)) - itemPrice
print(f"거스름돈 {nod_money}")

# 거스름돈 500원 동전 계산
nCoin500 = nod_money // 500
nod_money = nod_money % 500 

# 거스름돈 100원 동전 계산
nCoin100 = nod_money // 100
nod_money = nod_money % 100 

# 거스름돈 50원 동전 계산
nCoin50 = nod_money // 50
nod_money = nod_money % 50 

# 거스름돈 10원 동전 계산
nCoin10 = nod_money // 10
nod_money = nod_money % 10 

# 거스름돈 1원의 동전 계산
nCoin1 = nod_money // 1
nod_money = nod_money % 1

print("500원 개수 : {}, 100원의 개수 : {}, 50원의 개수 : {}, 10원의 개수 : {}, 1원의 개수 : {}".format(nCoin500,nCoin100,nCoin50,nCoin10,nCoin1))