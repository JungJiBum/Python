#M 이 점수중 최대값
#모든 점수를 점수 / M*100
#ex 최고점 70, 수학점수 50점 수학점수는 50/70*100이 되어 71.43점이나옴


from numpy import append


N = int(input())

score_list = list(map(int,input().split()))
max_score = max(score_list)

ls = []
for score in score_list:
    ls.append(score/max_score * 100) #점수/최고점 * 100

avg = sum(ls)/N
print(avg)