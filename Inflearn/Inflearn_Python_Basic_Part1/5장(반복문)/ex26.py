statements = "    안녕!"
# 왼쪽 공백만 제거하는 함수 lstrip()
print(f"원본 : {statements}")
print("왼쪽 공백 제거 : " +statements.lstrip())
# 오른쪽 공백만 제거하는 함수 rstrip()
statements = "안녕!                       "
print("오른쪽 공백 제거 : "+statements.rstrip()+"공백제거")

# 양쪽 공백 제거하는 함수 strip()
statements = "     안녕!     "
print("양쪽 공백 제거 : "+ statements.strip()+"제거")
print("="*50)
# 문자열 나누기

statements = "나는 열심히 파이썬 공부를 합니다."
print(statements.split())
