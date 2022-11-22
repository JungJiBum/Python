# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램 작성

statements = input("문자열을 입력하세요 : ")
result = ""


for ch in statements:
    # 루프 문자가 공백이 아니라면..
    if ch != " ":
        result += ch

print(f"입력한 문자열은 : {statements}")
print(f"공백을 제거한 문자열은 : {result}")