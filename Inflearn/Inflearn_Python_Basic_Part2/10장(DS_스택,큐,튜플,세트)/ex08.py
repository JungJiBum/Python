# 문제 : data_list = [(90,80), (85,75), (90,100)] 튜플을 원소로 하는 리스트를 활용
# 학생 총점과 평균(소수 첫째자리) 출력하는 프로그램 작성
# enumerate()함수 사용
'''
출력 결과
1번 학생 총점은 170점이고, 평균은 85.0이다.
2번 학생 총점은 160점이고, 평균은 80.0이다.
3번 학생 총점은 190점이고, 평균은 95.0이다.
'''

data_list = [(90,80), (85,75), (90,100)]

for index, data in enumerate(data_list):
    # score  = sum(data)
    # avg = score / 2
    print("{}번 학생의 총점은 {}점이고, 평균은 {}이다.".format(index+1, sum(data), (sum(data)/2)))
    # hap=0
    # # 학생 1명씩 점수 누적
    # for score in data:
    #     hap += score
    # print("%d번 학생 총점은 %d이고, 평균은 %0.1f이다." %(index+1, hap, hap/2.0))



