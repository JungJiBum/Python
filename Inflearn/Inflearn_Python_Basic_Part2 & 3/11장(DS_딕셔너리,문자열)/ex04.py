# 사용자가 지정하는 파일을 읽어서 파일에 저장된 각각의 단어가 몇 번이나 나오는지 계산하는 프로그램 작성
# 출력 결과
# 파일 이름 입력 : words.txt
# {"asia":3, "do":2, "정지범":2}

f_name = input("파일 이름 입력 : ")
file = open(file=f_name, mode="r", encoding="UTF-8")

word_count = dict() # 빈 딕셔너리 생성
for line in file:   # 파일로부터 한 줄씩 읽음
    words = line.split()    # 읽어온 한줄의 문장을 split()을 통해 단어(토큰)로 나눔
    for word in words:      # 단어 리스트에서 해당하는 단어 만큼 반복 수행
        if word not in word_count:  # 단어가 딕셔너리 내 존재하지않으면
            word_count[word] = 1    # 단어를 딕셔너리에 추가
        else:                       # 단어가 딕셔너리 내 존재한다면
            word_count[word] += 1   # 단어의 value값을 증가함
print(word_count)
file.close()
