class Solution:
    def solution(self, a):
        cnt = 0
        for i in range(a+1):  # 0부터 입력한 파라미터 숫자까지
            if '13' in str(i):  # 인덱스 i에 '13'이라는 값이 있다면
                cnt += 1  # 카운트
        print(cnt)


a = Solution()  # 객체 생성
print(a.solution(200))  # 함수호출


'''
피보나치 수열
'''


def fibo(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b

    return b


for n in range(1, 11):
    print(n, fibo(n))
'''
n 이 2 미만일 때는 아까와 같이 그대로 반환한다. 그 다음이 재밌는데 n 이 2 이상일 때는 n-1 번만큼 반복문을 시행한다. 그 이유는 우리가 0번째 값 a 와 첫 번째 값 b 를 계속 반복하면서 원하는 값을 만들텐데, n 이 2일 때는 단 한 번(n-1)만 계산하면 원하는 값을 만들 수 있기 때문이다.

그리고 한 번의 반복마다 ‘a, b = b, a + b’를 시행한다. 파이썬에서 이와 같이 대입을 사용하면, ‘a = b’, ‘b = a + b’와 같이 대입이 이루어지는데 이는 파이썬의 packing & unpacking과 관련이 있다. 새로 만든 b 에 이전의 a, b 값을 더해 새로운 피보나치 값을 만들어 나간다. 반복문이 끝나면 b 가 우리가 고대하던 n 번째 피보나치 수가 되며 이를 반환하면 된다.

앞선 재귀에 비해 매우 효율적인 방법이며 시간 복잡도는 O(n)이 된다.
'''
