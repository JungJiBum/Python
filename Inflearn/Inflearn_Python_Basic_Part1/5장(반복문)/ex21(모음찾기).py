# 반복문으로 문자열 관련 처리하기 실습

# fruit = "Apple"

# fruit 문자열 변수에 값을 하나씩 문자 형태로 가져와서 출력
# for letter in fruit:
#     print(letter, end="")

print("="*30)
# 사용자로부터 문자열(영문)을 입력받아 모음을 전부 없애는 코드
s = input("문자열 입력(영문만) : ")
# 영문자 모음의 문자열
vowels = "aeiouAEIOU"
result = ""

for letter in s:
    # 하나씩 반복하는 문자가 모음 문자열에 존재하지 않는다면 result에 추가
    if letter not in vowels:
        result += letter
    
print(f"입력한 결과 중 자음만 뽑아 냈을 때 : {result}")
print("="*30)

# 문자열을 입력받아 자음과 모음의 개수를 집계하는 코드
origin = input("문자열을 입력하세요(영문자) : ")
# 입력받은 문자열을 소문자로 변경
word = origin.lower() # 대문자로 변경하고 싶으면 upper()사용
vowels = 0
consonants = 0

# 문자열의 길이가 0보다 크고 알파벳이라면 '참'으로 반환
if len(origin) > 0 and origin.isalpha():
    for ch in word:
        # 루프 변수의 값이 모음에 해당한다면
        if ch in "aeiou":
            vowels += 1
        else:   # 자음일 경우
            consonants += 1

print(f"모음의 개수 : {vowels}\n자음의 개수 : {consonants}")
