
id_ls = ["muzi", "frodo", "apeach", "neo"]
repo = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k=2
answer = [0] * len(id_ls)
# print(answer)
# print(answer[id_ls.index('muzi')])
test1 = {x: 0 for x in id_ls}

print(test1)
print(set(repo))
for r in set(repo):
    # test1[r.split()[1]] = test1[r.split()[1]] + 1
    test1[r.split()[1]] += 1
    print(f"0번 {r.split()[0]} / 1번 {r.split()[1]} ")
print(test1)

for r in set(repo):
    print(r)
    if test1[r.split()[1]] >=k:
        answer[id_ls.index(r.split()[0])] +=1
    
    print(answer)
