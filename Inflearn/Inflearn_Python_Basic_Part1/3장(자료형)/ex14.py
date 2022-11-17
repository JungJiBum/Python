# 문자열 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각 해당하는 문자에 번호가 존재함
# 인덱스는 무조건 0부터 시작이 되며, 마지막 인덱스는 n-1이 성립됨

word = 'python'
# print(len(word))
# print(word[0])
# print(word[5])
# print(word[-1])
# print(word[len(word)-1])

item1 = input("첫번째 단어 입력 : ")
item2 = input("두번째 단어 입력 : ")
item3 = input("세번째 단어 입력 : ")

word = item1 + item2 + item3
print(word)
word = item1[0] + item2[0] + item3[0]
print(word)