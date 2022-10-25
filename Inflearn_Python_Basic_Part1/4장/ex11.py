# 문자열 중앙에 있는 문자를 추출해서 출력을 하는 프로그래 만들기
# 예를 들어 문자열 'weekday'라면 문장의 주는 'k'가 된다.
# 하지만, 만약 문자열이 짝수 개의 문자를 가지고 있다면 중앙에 문자를 2개를 출력한다.
# 예를 들어 'monday'라면 'nd'를 출력하도록 한다.

str_1 = input("문자열을 입력해주세요 : ")
length = len(str_1)

if length % 2 == 1:
    ch = str_1[length//2]
    print("중앙에 있는 한 글자는",ch,"이다.")
else:
    ch1 = str_1[length//2 - 1]
    ch2 = str_1[length//2]
    print(f"중앙에 있는 두 글자는 {ch1}{ch2} 이다.")