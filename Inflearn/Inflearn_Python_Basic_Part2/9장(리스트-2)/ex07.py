# 일반적인 리스트 연산 실습
# 최소, 최대값 구하는 알고리즘

# 내장 함수를 이용하여 min, max값을 구하는 코드
# num = [1,5,-9,100]
# print(f"min : {min(num)}")
# print(f"max : {max(num)}")

# max, min 값을 구하는 알고리즘은 상당히 중요한 개념이므로 아래 코드를 이해하자.
prices = [1000,3000,500,10000,20000,700]
# prices[]에 있는 0번째 인덱스 값을 변수에 저장을 한다.
low_price = prices[0]
# 이후 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 low_price 변수에 재저장

for i in range(1, len(prices)):
    # prices[i]가 low_prices보다 작으면 참
    # 조건절에서 부등호를 수정하면 최대값을 구할 수 있음
    if prices[i] < low_price :
        low_price = prices[i]
print(f"가장 싼가격 : {low_price}")
print("-"*40)

# 문자열에서 가장 짧은 문자열 구하는 알고리즘
words = ["dog",'cat',"horse","lion","tiger",'elephant','bi']
k_words = ["안녕","하이","반갑습니다","가세요","오랜만임다"]
# 문자열 리스트에서 min()은 제일 첫 글자가 아스키 코드중 가장 작은 단어를 반환
print(f"min word: {min(words)}")
print(f"max word: {max(words)}")
print(f"min word: {min(k_words)}")
print(f"max word: {max(k_words)}")

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
ls_word = []
for i in range(1, len(words)):
    # words[i]가 shortest_word보다 작으면 반환
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            ls_word.clear()
            ls_word.append(words[i])
        else:
            ls_word.append(shortest_word)
            shortest_word = words[i]
            ls_word.append(shortest_word)


print(f"가장 짧은 단어이거나 같은 단어 들 : {shortest_word}")
print(f"가장 짧은 단어이거나 같은 단어 들 : {ls_word}")

for i in range(len(ls_word)):
    print("가장 짧은 단어 목록 : {}".format(ls_word[i]))