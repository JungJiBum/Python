# 탐색하기
# 주어진 데이터 내에서 어떠한 특정값을 찾는 행위가 탐색
 # index()를 이용하여 일반적 탐색이 가능

# ls_word = ["gold","blue","red","yellow","green"]

# search_word = input("찾고자하는 단어를 입력하세요 : ")

# if search_word in ls_word:
#     index = ls_word.index(search_word)
#     print(f"찾고자하는 단어는 {index} 번째 인덱스에 존재한다.")
# else:
#     print("찾고자 하는 단어가 없습니다.")


# 직접탐색을 하는 알고리즘을 구현해야 하는 경우도 상당히 많다.
# 탐색의 가장 기본적인 방법은 순차 탐색
# 순차 탐색은 리스트의 요소를 순서대로 하나씩 꺼내서 탐색키 값과 비교
# 성공하면 루프를 빠져나오고 루프를 다했음에도 없다면 탐색키 존재하지않음

def number_search(ls,key):
    cnt = 0
    for i in range(len(ls)):
        if key == ls[i]:
            cnt += 1        # 같은 값이 존재하면 갯수를 증가하는 코드
    return cnt               

# 같은 수가 존재 한다면 그 갯수도 몇개인지 출력
num_ls = [10,20,30,40,50,50,50,50,50,50,50,60,70,80,90,100, 100, 100]
# key = int(input("사용하고자 하는 정수 입력 : "))
# cnt = number_search(num_ls, key)

# if cnt == 0:        #cnt 가 0이라면 찾고자하는 값이 존재하지 않음.
#     print(key,"은 존재 하지않는다.")
# else:               #찾고자 하는 값이 해당 리스트에서 몇 개인지 확인해 줌.
#     print(key,"은 ",cnt, "개 존재 함")


# 모든 조건에 만족하는 항목을 전부 찾는 방법
# result = []
# for i in num_ls:
#     if i >= 50:
#         result.append(i)
# print(result)
# 바로 위에 있는 코드를 사용자로부터 키를 입력받아 키값 이상의 값들을 출력하고 그 키값 이상인 값들의 총 갯수를 구하는 프로그램 작성
num = int(input("기준 숫자 입력 : "))
result = []
for i in num_ls:
    if i >= num:
        result.append(i)
print(f"{num}보다 큰 값들은 {result}이며, 갯수는 {len(result)}개이다.")