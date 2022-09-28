Dial_Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

x = input().upper()
cnt = 0


for i in range(len(x)): # 입력값의 길이만큼 x=abcde -> i = a b c d e
    for j in Dial_Number: # Dial_Number리스트의 J는 ABC, DEF, GHI .... WXYZ
        if x[i] in j:   # x[i]는 입력값 순서대로 x[i] -> a in j(ABC)
            cnt += Dial_Number.index(j)+3
print(cnt)