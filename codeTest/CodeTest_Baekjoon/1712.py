a,b,c = map(int,input().split())

if b>=c:
    print(-1)
else:
    print(int(a/(c-b))+1)

'''
손익분기점이란?
-> 최초로 총 수입이 총 비용보다 많아져 이익이 발생하는 지점
'''