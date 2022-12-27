'''
자료구조 : 데이터 특징을 고려하여 데이터를 저장하는 방법
특징 : 최대한 메모리를 효율적으로 저장 및 반환하는 방법, 데이터를 관리하는 것
대용량일수록 빨리 저장하고, 빨리 검색하고, 메모리를 최대한 효율적으로 사용하면 유저들에게 실행결과를 빨리 돌려주는 방법
'''

# 스택(stack) : 택시기사님 동전통, LIFO(Last In First Out)
# 데이터를 저장 -> push, 데이터 추출 -> pop
stack_data = []
# 스택에 값을 push 하고 있음
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)
# 스택에서 추출할때는 pop() 메서드 사용 -> return 타입
print(stack_data.pop())
print(stack_data.pop())
print(stack_data)

# 입력받은 텍스트를 역순츠로 추출하는 프로그램
word = input("문자열 입력 : ")
# list()메소드를 사용하여 문자열을 리스트로 변환
word_list = list(word)

result=[]
# _ 라는 기호는 파이썬에서 상당히 많이 사용되는 기호인데, for문 루핑시킬때
# 루프 변수에 값을 사용하지 않을 때, _ 로 할당 받는 것이다.

for _ in range(len(word_list)):
    # 입력받은 문자리스트의 마지막 부분부터 result[]에 담고 있다.
    result.append(word_list.pop())
print(result)