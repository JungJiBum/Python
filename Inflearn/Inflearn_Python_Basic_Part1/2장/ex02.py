'''
사용자로부터 참석하는 인원의 수를 받아 해당하는 인원 수에 따라
치킨은 인당 1마리, 맥주는 인당 2병, 케익은 인당 4개 출력하는
프로그램 작성
'''

# input은 문자 타입으로 받는다는것 잊지말고 형변환 해주기.
number = input("입력하는 인원 수 : ")
# number = int(input("입력하는 인원 수 : "))


chicken = number * 1
beer = int(number) * 2
cake = int(number) * 4

print(f"참가하는 인원은 {number}명 이며, 치킨은 {chicken}마리, 맥주는 {beer}병, 케익은 {cake}개 이다.")
