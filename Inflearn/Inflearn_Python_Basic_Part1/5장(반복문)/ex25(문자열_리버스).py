# 입력받은 문자열을 거꾸로 출력하는 프로그램 작성

statements = input("문자열을 입력하세요 : ")

s_reverse = ""

# for문을 활용한 방법
for ch in statements:
    s_reverse = ch + s_reverse

print("입력한 문자열은 : "+statements)
print("역순 문자열은 : "+s_reverse)

# list() 함수는 문자열을 리스트 타입으로 바꾸는 함수이다.
print("-"*30)
s_list = list(statements)
# reverse() 는 리스트 타입을 역순으로 전환
s_list.reverse()
print("".join(s_list))

s1 = statements
# reversed() 는 문자열을 역순으로 하는 함수
print("".join(reversed(s1)))

# 파이썬에서는 [::-1]를 사용해서 문자열을 역순으로 출력할 수 있다.
print("-"*30)
print(statements[::-1])
# 문자열 3번째 인덱스 부터 역순으로 출력하는 방법
print(statements[3::-1])