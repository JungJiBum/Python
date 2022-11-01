ls=[]
for i in range(1,10):
    ls.append(int(input()))
print(max(ls))
print(ls.index(max(ls))+1)