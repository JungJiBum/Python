# 5000원이 있다. 사탕 가격이 120원이다. 최대로 살수 있는 사탕의 개수는?

myMoney = 5000
candyPrice = 120

# 최대로 살 수있는 사탕 개수는

# / 는 실수 // 는 정수
numCandies = myMoney//candyPrice

print("최대 개수는 : ", numCandies)

# 최대로 살 수 있는 사탕을 구입하고 남은 돈
changeMoney = myMoney % candyPrice

print("남은 금액은 : ", changeMoney)
