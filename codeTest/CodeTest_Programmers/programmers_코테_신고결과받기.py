'''
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다.
무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
'''

#--------------------------------------
def solution(id_list, report, k):
    #id_list -> 이용자 ID
    #report -> 각 이용자가 신고한 이용자의 ID정보가 담긴 문자열 배열
    # k -> 정지 기준이 되는 신고 횟수
    
    answer = [0] * len(id_list) #빈 리스트를 id_list길이만큼 곱함
    reported = {x:0 for x in id_list}
    # print(reported)
    
    for r in set(report): # 신고자 / 신고당한자 배열 값
        # print(r)
        a,b = r.split() # 신고자 / 신고당한자 분리
        # print(f"report : {a} / {b}")
        reported[b] +=1
        # print(reported)
    
    for r in set(report):
        a,b = r.split()
        print(f"a : {a} / b : {b}")
        # print(f"a : {a} / b : {b}")
        # print(reported[b])
        if reported[b] >= k:
            answer[id_list.index(a)] +=1
            print(id_list.index(a))
    return answer

# https://suminig.tistory.com/11
#--------------------------------------

id_ls=["muzi", "frodo", "apeach", "neo"]
repo=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
print(solution(id_ls,repo,k))


