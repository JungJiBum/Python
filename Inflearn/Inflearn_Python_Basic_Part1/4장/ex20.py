# 중복(nested) if ~ else 구문
'''
사용자로부터 아이디를 입력받아 등록된 아이디인지 검사하는 프로그램
등록된 아이디를 리스트(list)에 저장하도록 한다.
아이디가 등록되어있으면 패스워드를 물어보도록 출력한다.
단, 패스워드는 '1234' 라고 가정하도록 한다.
'''

ID_ls = ['admin','root','']
pw = "1234"
userId = input("아이디를 입력하세요 : ")

if userId in ID_ls:
    userPw = input("패스워드를 입력하세요 : ")
    if userPw == pw:
        print("로그인 성공")
    else:
        print("비밀번호가 틀립니다.")
else:
    print("등록된 아이디가 아닙니다.")