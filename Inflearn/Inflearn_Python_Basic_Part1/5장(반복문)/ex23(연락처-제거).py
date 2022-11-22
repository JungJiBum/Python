# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력받도록하고 출력할 떄는 "-" 삭제를 한 문자열을 출력하는 프로그램 작성

phone_num = input("당신의 전화번호를 입력하세요.(-포함) : ")
new_phone = ""

if len(phone_num) == 12 or len(phone_num) == 13:
    for i in phone_num:
        # 루프문자가 - 가 아니라면 참을 반환
        if i != "-":
            new_phone += i
    print(new_phone)
    
else:
    print("번호를 잘못 입력하셨습니다.")


