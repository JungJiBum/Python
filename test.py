from deepl import deepl

file = open('test.txt',"r",encoding='utf-8') # -> 번역할 텍스트 파일
t = deepl.DeepLCLI("ko","en") # -> 한국어에서 -> 영어로 
strings = file.readlines() # -> 텍스트파일 읽어오기
file.close() # -> 파일 닫기

f = open('translate.txt','w') # -> 번역결과 저장할 파일 열기 위 파일이랑 다른거
for line in strings:        # -> 텍스트파일 읽어온 strings를 한줄씩 반복
    line = line.strip("\n") # -> 읽어오면서 \n이거 때문에 에러나서 제거함
    f.write(t.translate(line)) # -> write를 통해 한줄씩 번역된 결과를 저장
    f.write('\n')           # -> 저장결과가 줄바꿈이 안되서 추가함

f.close()                   # 번역 결과 파일 닫기
