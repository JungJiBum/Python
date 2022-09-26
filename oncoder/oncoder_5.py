# 13 구하기
# a가 주어진다.
# 1이상 a 이하의 정수 중 숫자에 13이 들어가는 숫자 개수를 리턴하라

ls = []
class Solution:
    def solution(self,a):
        cnt = 0
        for i in range(a+1):
            if '13' in str(i):
                ls.append(i)
                cnt +=1
        return cnt
a = 200
s = Solution()
t = s.solution(a)
print(t, ls)