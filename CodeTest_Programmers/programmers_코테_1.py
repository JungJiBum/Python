'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다
ex_1 "abcde"
ex_2 "qwer"
'''
# def solution(s):
#     answer = ''
#     if len(s) % 2:
#         answer = (s[len(s)//2])
#     else:
#         answer = (s[len(s)//2-1:len(s) // 2 + 1])
#     return answer


# print(solution("qwer"))


'''
임의의 양의 정수 n에 대해,
n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항

n은 1이상, 50000000000000 이하인 양의 정수입니다

입출력 예 설명

입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
'''

def solution(n):
    answer=0
    num = n ** 0.5

    if num == int(num):
        answer = (num+1) ** 2
    else:
        answer = -1

    return answer
# print(10)
# print(10**0.5)
# print(3**0.5)
print(solution(144))