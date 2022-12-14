# 기본적인 파일 입출력 실습
data = []
# 파일의 경로를 지정하고 읽기모드로 문자셋 UTF-8로 설정
# 해당 파일을 열고 메모리에 로딩된 파일 주소 반환
fp = open("C://Temp//test.txt", mode='r', encoding='UTF-8')
# print(fp, type(fp))
# readlines() 메서드는 파일의 저장된 내용을 한번에 다 읽는다.
for line in fp.readlines():
    # strip()메서드는 원래 문자열 양쪽 공백을 제거하는 역할을 하지만, 파일을 읽어들일때는 엔터키 제거를 해준다.
    # print(line.strip())
    data.append(line.strip())
# 프로그램에서 리소스를 다 사용했으면 반드시 close() 메서드를 호출 하도록 한다.
print("파일에서 읽은내용이다.")
print(data)
fp.close()

# 파일에 내용 쓰는 방법
# 파일의 모드가 w 인 경우에는 기존 파일의 내용을 덮어쓴다.
fp = open("C://Temp//test.txt", mode='w', encoding='UTF-8')
fp.write("우리는 파이썬을 공부합니다.")
fp.write("저희도 파이썬을 공부합니다.")
print("쓰기완료")
fp.close()

# 기존 파일의 내용에 추가를 해준다.
fp = open("C://Temp//test.txt", mode='a', encoding='UTF-8')
fp.write("11.우리는 파이썬을 공부합니다.")
fp.write("22.저희도 파이썬을 공부합니다.")
print("추가완료")
fp.close()

# csv파일 읽는 방법
import csv
fp = open("C://Temp//sample1.csv", mode='r')
reader = csv.reader(fp)
for txt in reader:
    print(txt)

fp.close()
