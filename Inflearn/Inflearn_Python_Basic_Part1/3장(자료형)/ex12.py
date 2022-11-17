# 문자열에 대한 실습

# 큰따옴표(double quotation)로 묶으면 문자열이 된다.(권장)
welcome = "Happy New Year 2022"
print(welcome)
# 작은따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2022'
print(welcome)
# 문자열을 만들때 따옴표를 "로 시작하여 ' 로 끝낸다면 EOL(End Of Line)에러가 발생함.
#welcome = "happy new year 2022'
#welcome = "happy new year 2022

# ""안에 다른 ""이가 있으면 컴파일러가 에러 발생함
#msg = "은혁이가 "안녕하세요" 라고 인사 했다."
msg = "은혁이가 '안녕하세요' 라고 인사 했다."
print(msg)
# 파이썬에서는 따옴표를 출력하려면 \를 이용함
# \가 따옴표 앞에 있으면 '는 특수한의미를 잃어버리고 하나의 문자로 편승이됨
msg = 'doesn\'t'
print(msg)
msg = "\"Yes,\" I can do it"
print(msg)
# 특수자 형태인 \n은 개행(Enter)을 하는 문자임
msg = "First\nSecond\nThird"
print(msg)
# 특스문자 \t는 탭만큼 띄우는 문자이다.
msg = "c:\temp\name"
print(msg)
# 위 코드에 \t , \n 이러한 이스케이프 문자들의 기능을 제거하려면 문자열 앞에 r을 붙여줌으로써 이스케이프 기능을 제거시킴
msg = r"c:\temp\name\a.txt"
print(msg)
# 문자열 길이를 알고자 할때 len() 사용
msg = "World"
print(len(msg))
