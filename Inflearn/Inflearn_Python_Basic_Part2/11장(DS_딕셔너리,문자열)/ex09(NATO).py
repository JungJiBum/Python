# 문제
# 머리 글자어(acronym)은 NATO(North Atlantic Treaty Organization)
# 각 단어 첫 글자를 모아서 만든 문자열. 사용자로부터 입력하면 해당되는 머리 글자어를 출력하는 프로그램 구현
'''
출력결과
문자열을 입력하세요 : North Atlantic Treaty Organization
머리문자열 : NATO
'''
def main():
    string = input("문자열을 입력하세요 : ")
    acronym = ""
    # 입력받은 문자열을 대문자로 변환 후 토큰으로 분리
    for word in string.upper().split():
        acronym += word[0]
    
    print(acronym)

if __name__ == "__main__":
    main()