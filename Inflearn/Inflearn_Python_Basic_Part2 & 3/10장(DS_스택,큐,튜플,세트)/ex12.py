'''
문제 : 텍스트 파일을 읽어서 단어를 얼마나 다양하게 사용하여 문서를 작성하였는지 계산하는 프로그램

출력 결과
입력 파일 이름 : words.txt
사용된 단어의 개수 : 18
{'travels','half','that','news','alls','well','fast','feather',
'flock','bad','together','ends','is','a','done','begun','birds','of'}

'''
# 단어에서 마침표를 제거하고 소문자로 만들어주는 역할
def process(word):
    out_str = ""
    for ch in word:
        if ch.isalpha():        # 영문자라면..
            out_str += ch
    return out_str.lower()      # lower()를 사용하여 소문자로 변환


if __name__ == "__main__":
    words = set()       # 빈 세트 생성
    f_name = input("입력 파일 이름 : ")
    file = open(f_name, mode="r")       # 파일 열고 읽기 모드 설정

    # 파일의 모든 줄에 대해 반복
    for line in file:
        lineWords = line.split()        # 한 라인을 읽어와서 단어(토큰)별로 분리 함
        for word in lineWords:
            words.add(process(word))             # 단어를 세트에 추가함


print("사용된 단어의 개수 : ",len(words))
print(words)
file.close()
