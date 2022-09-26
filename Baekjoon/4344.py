C = int(input())

for i in range(C):
    scores = list(map(int,input().split()))
    avg = sum(scores[1:])/scores[0] #scores[0] = 학생수 scores[1:] 점수
    cnt = 0

    for score in scores[1:]:
        if score > avg:
            cnt +=1 # 평균보다 높은 학생
    rate = cnt/scores[0] * 100
    print("{:.3f}%".format(rate))
