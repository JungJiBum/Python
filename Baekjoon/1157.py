str = input().lower() #입력을 소문자로만 받도록설정 Mississipi

word_list = list(set(str))  #입력값을 set함수를 사용해 중복 제거 후 리스트화  Mississipi-> m i s p

cnt=[]

for i in word_list: # i는 m i s p 값을 갖고있음
    count = str.count(i) # 입력받은 문자열 에서 i를 카운트함 -> 정수
    cnt.append(count) # count의 값을 cnt 리스트에 추가함 -> 정수형 리스트 생성


if cnt.count(max(cnt)) >=2: # cnt 리스트에서 max(cnt)의 개수가 여러개인경우를 확인
    print("?")
else:
    # print(word_list) #셋함수 적용된 리스트 zZa -> ['z', 'a']
    # print(cnt) # 워드 카운트 된 리스트 zZa -> ['z', 'a'] -> [2,1]
    # print(max(cnt)) # 카운트된 리스트에서 큰값 zZa -> ['z', 'a'] -> [2,1] -> 2
    # print(cnt.index(max(cnt))) #카운트된 리스트에서 큰값이 cnt 리스트에서 몇번째 인덱스인지 zZa -> ['z', 'a'] -> [2,1] -> 2 -> 0
    # print(word_list[cnt.index(max(cnt))]) #셋함수 적용된 워드리스트 ['z'.'a'] 에서 큰값이 cnt 리스트에 몇번째 인덱스 인지 확인하여 문자 출력
    print(word_list[(cnt.index(max(cnt)))].upper()) #중복을 제거한 word_list에서 cnt.index(max(cnt))
