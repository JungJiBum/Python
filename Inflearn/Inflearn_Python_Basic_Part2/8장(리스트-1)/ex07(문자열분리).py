# 리스트 일치 검사 실습
# 2개의 리스트가 동일한 자료형이여야 한다.
li1 = [10,20,30]
li2 = [10,20,30]
print(li1 ==li2)

# == 연산자는 2개의 리스트가 길이가 서로다르면 무조건 False
li1 = [10,20,30]
li2 = [10,20]
print(li1 ==li2)

li3 = [4,5,2]
li4 = [4,5,0]
print(li3 >li4)

# 아래 리스트는 >, < 를 비교할 때 아스키코드를 가지고 비교한다.
li5 = ["a","b","c"]
li6 = ["a","b","d"]
print(li5 < li6)
print(ord("c")) #c의 아스키코드는 99
print(ord("d")) #d의 아스키코드는 100
print(chr(99))  #아스키코드 99값은 c
print(chr(100)) #아스키코드 100값은 d

print("="*30)
# 리스트 정렬
# 2가지 방법
# 1번째 방법 : 리스트 객체의 sort() 메소드 이용
# 원본 리스트의 값이 변경된다.
li = [80,90,100,-70,-50]
a = li.sort() # sort()는 리턴값이 없음.
print(a)

# 내장함수 sorted() 메소드를 이용하는 방법
# 원본 리스트 그대로 유지하고 정렬된 리스트를 반환
li = [80,90,100,-70,-50]
c_li = sorted(li)
print("기본 리스트 : ",li)
print("정렬 리스트 : ",c_li)
print("="*30)
li = [80,90,100,-70,-50]
li.reverse()
print("리스트 뒤짚기",li)
print("="*30)
li = [80,90,100,-70,-50]
li.sort(reverse=True)   #리버스 매개변수의 값을 True로 사용하면 내림차순이 정렬이 이루어짐
print("리버스 매개변수 : ",li)
print("="*30)

# 문자열 정렬하기(유니코드 기준)
li = ["하와이","폭포","가나","한국"]
li1 = sorted(li, key=str.lower)
print(li1)

# 긴 문자열 분리하는 방법(split()), split() 문자열을 분리해서 리스틑 타입으로 반환
statement = "나는 한국에서 살고있는 프로그램 교사이다, 만나서 반갑다."
li = statement.split(",")
print(li)


