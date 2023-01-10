# str 클래스 메서드 실습
# split() : 문자열에서 단어(토큰)을 분리하고자 할때 사용하는 메서드
# 인자값으로 구분자(seperator)를 주게 되면 주어진 구분자로 문자열 분리
# 기본 인자값 공백
string = "안녕 BOB 난 지금 학교 가고 있어"
li1 = string.split()    # 공백으로 분리
print(li1, type(li1))

# split()는 구분자를 하나밖에 받지 않는다.
string = "안녕,BOB,난,지금,학교,가고,있어"
li2 = string.split(",")    # 콤마로 분리
print(li2, type(li2))

# 정규표현식을 사용하기 위해 regex 모듈 인스톨
import regex
string = "안녕/BOB,난|지금&학교,가고,있어"
li3 = regex.split("[/,&|]", string)    # 정규표현식으로 분리
print(li3, type(li3))
print("-"*50)
# 문자열 검사
string = "abcd"
print(string.isalpha())     # 문자열이 영문인지 확인
print("-"*50)
string = "12345"
print(string.isdigit())     # 문자열이 10진수인지 확인
print(string.isdecimal())     # 문자열이 10진수인지 확인
print("-"*50)
string = "abcd12345"
print(string.isalnum())     # 문자열이 영문,숫자 인지 동시 확인 코드
print("-"*50)
string = "1.2"
# numeric 굉장히 넓은 의미이며 숫자값 표현에 문자열을 인정해준다.
print(string.isnumeric())
# str 클래스에서 음수, 실수 판별하는 메서드는 없다.
print("-"*50)
string = " "
print(string.isspace()) # 공백 확인

# 부분 문자열 검색 실습
print("-"*50)
# string = input("파이썬 소스를 입력해주세요 : ")
# endswith("문자열") 메서드는 인자값 문자열로 끝이나면 True 리턴
if string.endswith(".py"):
    print("올바른 파일 이름 이다.")
else:
    print("잘못된 파일 이름 이다.")

print("-"*50)
string = "2022-03-04.txt"
# startswith(문자열) 메소드는 인자값이 문자열로 시작하면 True로 리턴
if string.startswith("2022"):
    print("2022년 파일이다.")
else:
    print("2022년 파일이 아니다.")

print("-"*50)
# string = input("영단어를 입력하세요 : ")
print(string.upper())       # 전부 대문자
print(string.lower())       # 전부 소문자
print(string.capitalize())  # 앞문자만 대문자
print(string.title())       # 앞문자만 대문자

print("-"*50)
# format() 는 포맷 {} 을 만들어놓고 문자열 생성하는데 사용
string = "{}b{}"
print(string.format("a","c"))   # abc

print("-"*50)
# join()은 리스트 같은 반복(iterable) 인자를 전달받아 문자열로 연결하는데 사용
string = ["a","b","가"]
print("!".join(string)) # a!b!가 결과 나옴

print("-"*50)
# partition() 전달받은 인자값으로 문자열을 나눔, 리턴타입은 튜플.
string = "2377325@gmail.com"
print(string.partition("@"))    # ('2377325', '@', 'gmail.com') 결과

print("-"*50)
# count()는 인자값으로 들어오는 값을 문자열에서 몇 개 있는지 카운팅을 함
string = "aaaaabcc"
print(string.count("a")) # 인자값의 개수를 찾아냄, 찾는 인자값이 없다면 0으로 리턴

print("-"*50)
# find()메서드는 특정 단어를 찾아서 인덱스를 리턴하고 없다면 -1 리턴
# index() 차이점은 특정 단어를 찾으면 인덱스를 리턴하지만 없다면 에러 발생
string = "apple"
print(string.find("p"))
print(string.index("p"))
# print(string.find("z"))
# print(string.index("z"))

print("-"*50)
# 문자열에서 공백제거하는 방법
'''
strip() -> 양쪽 공백 제거, 탭문자, 줄바꿈(enter)도 제거
lstrip() -> 왼쪽 공백만 제거
rstrip() -> 오른쪽 공백만 제거
단 메소드로 문자열 중간에 존재하는 공백을 제거할 방법은 없다. 함수를 만들어 직접 사용해야함
'''
string = "        aaaaa    bbbbb    ccccc        ddddd        \t탭"
print(string.strip())
print(string.rstrip())
print(string.lstrip())