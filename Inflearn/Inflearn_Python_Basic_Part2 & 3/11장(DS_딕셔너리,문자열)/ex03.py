# 영한 사전 만들기
'''
공백 딕셔너리 생성 -> 영단어 키 / 설명 값으로 저장
출력 결과
단어 입력(종료하려면 'q') : one
하나
단어 입력 : python
해당하는 단어가 없습니다.
-------------------------------
'''
eng_dict = dict()       # 빈 딕셔너리 생성
# 딕셔너리에 데이터 추가
eng_dict["one"]="하나"
eng_dict["two"]="둘"
eng_dict["three"]="셋"
eng_dict["four"]="넷"
eng_dict["five"]="다섯"

while True:
    eng = input("단어 입력(종료하려면 'q') : ")
    if eng == 'q':
        break
    if eng not in eng_dict:
        print("해당하는 단어가 없음")
    else:
        # dict.get(key, default=None) get()메소드는 첫번째 인자로 하나의 키를 넣어주면 해당 키의 값을 반환 해준다. 없으면 None 반환 0을 반환하고싶다면 .get('키',0)
        print(eng_dict.get(eng))        
