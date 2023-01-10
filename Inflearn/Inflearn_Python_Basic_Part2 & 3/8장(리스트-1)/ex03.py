# 리스트는 다양한 데이터 저장할 수 있음
# 현업에서는 같은 종류 같은 타입의 데이터를 저장하며 사용함

# 리스트는 문자열도 저장 / 강아지를 많이키우는 사람이 있다고 가정하자
# 사용자로부터 강아지들의 이름을 저장하였다 출력하는 프로그램
# 조건 : 무한루프를 돌면서 엔터키가 입력되면 무한루프 탈출

dogNames = []
flag = True

while flag:
    name = input("강아지의 이름을 입력하세요(종료는 엔터키)")
    if name == "":
        flag = False
    dogNames.append(name)
print(f"강아지 이름은 {dogNames} 입니다.")

