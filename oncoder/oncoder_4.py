# 짝수 개수 구하기
# 양의 정수가 들어있는 arr이 주어진다
# arr에 있는 정수 중 짝수인 정수의 개수를 리턴하라

class Solution:
    def solution(self, arr):
        cnt = 0
        for i in arr:
            if i % 2 == 0:
                cnt +=1
        return cnt

arr = [2,4,5,6,7,8,9,12,15,18,20]
s = Solution()
t = s.solution(arr)
print(t)