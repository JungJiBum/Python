# 일회용 패스워드 생성기를 이용하여 3개의 패스워드를 생성하여 출력해보자.
# 패스워드 길이는 6자리로 한정
# 난수가 발생되는 범위값을 아래와 같이 지정한다.
# 난수발생 문자열 : "0123456789"
import random


def get_password():
    num_str = "0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(num_str))
        password = password + num_str[index]
    return password

for i in range(3):
    print("본인 인증을 위해 발송한 숫자를 입력하세요 : {}".format(get_password()))

