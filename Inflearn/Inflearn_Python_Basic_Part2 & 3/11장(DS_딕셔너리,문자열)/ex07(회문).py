# 회문이란 것은 앞으로 읽으나 뒤로 읽으나 동일한 문장을 의미함
# ex) mom, civic, dad 등
# 사용자로부터 문자열 입력받아 회문인지 아닌지 검사하는 프로그램을 작성해보자.
'''
출력결과
문자열을 입력하시오 : dad
회문입니다.
---------------------------------------
'''

def main():
    string = input("문자열을 입력하시오 : ")
    string = string.replace(" ","") #replac()자리바꿈 -> 공백으로 들어왔다면 공백이없는것으로 변경

    if check(string) == True:
        print(string + "은 회문입니다.")
    else:
        print(string + "은 회문이 아닙니다.")

def check(s):
    # 단어의 처음 인덱스와 마지막 인덱스를 저장하는 코드
    low = 0
    high = len(s)-1

    while True:
        #회문이라면 아래 조건문에 해당함
        if low > high:
            return True

        s1 = s[low]
        s2 = s[high]
        print(s1,s2)

        if s1 != s2:
            return False
        # 인덱스를 증가시켜 서로 비교항목을 바꾸도록 한다.
        low +=1
        high -=1


if __name__ == "__main__":
    main()
    