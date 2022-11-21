# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램을 작성하시오


s = input("입력하세요 : ")

alpha_cnt = 0
digit = 0
spaces = 0
for i in s:
    if i.isalpha():     #알파벳이라면
        alpha_cnt += 1
    elif i.isdigit():   #숫자라면
        digit +=1
    elif i.isspace():   #그외라면(공백)
        spaces +=1
    else:
        print("해당하는 문자는 알파벳,숫자,공백이 아닙니다.")

print(f"알파벳 숫자는 : {alpha_cnt}\n숫자는 : {digit}\n공백은 :{spaces}")