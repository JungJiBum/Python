# 홀수 짝수 판별
# 주어진 a가 짝수일 경우 EVEN 홀수일 경우 ODD를 리턴하라

class Solution:
    def solution(self,a):
        if a % 2 == 0 :
            return "EVEN"
        else:
            return "ODD"

s = Solution()
t = s.solution(10)
print(t)