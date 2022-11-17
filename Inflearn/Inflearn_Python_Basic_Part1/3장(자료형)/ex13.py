# 문자열 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 함

first_name = "이름"
last_name = "성"

name = last_name + first_name
print(name)

# 데이터 타입이 서로 맞지않아 발생하는 문제함
# temp = "person" + 100
# str()을 사용하여 int형 값을 문자열로 변환함
# temp = "person" + str(100)

# 문자열 반복
arrow = "->" * 10
print(arrow)
arrow = "->"
print(arrow*10)

# %s(형식지정자)
# %s는 문자열, 숫자값을 변수에 대입해서 자주 변경이 있을 경우 이런 형식을 지정하여 상황에 맞게끔 출력함
# %s에 정수를 대입
price = 1000
print("가격 : %s" % price)

# %s에 문자열을 대입
time = "13:49"
print("현재 시간 : %s" % time)
# %s를 2개이상 사용하고자 할때 해당하는 %s 개수 만큼 소괄호로 묶어서 형식 지정자에 대입을 해줘야 함
temp = "현재 시간은 %s 시 %s 분 %s 초 입니다."
print(temp %(10, 38, 12))