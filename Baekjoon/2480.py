one,two,three = map(int,input().split())

if one==two==three:
    print(10000+one*1000)
    exit(0)
if one==two:
    print(1000+one*100)
elif two==three:
    print(1000+two*100)
elif one==three:
    print(1000+one*100)
elif one!=two and two!=three and one!=three:
    m = max(one,two,three)
    print(m*100)


