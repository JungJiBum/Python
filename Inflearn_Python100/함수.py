#함수 작성과 함수 호출에 대한 코드 구현
#함수 이름은 a() b()

'''
#[2]: 함수 호출
def a():
    result = "붕어빵"
    result_loc = id(result)
    return result_loc

def b():
    result = "개구리빵"
    result_loc = id(result)
    return result_loc
def c():
    print("붕어붕어빵")

def d():
    print("개굴개구리빵")
'''
#[3] 함수 출력
# print(a())
# print(b())
# c()
# d()

#변수의 메모리 주소값을 출력하여 다른 함수 내 같은 변수의 값들이 어떤 주소를 가지고 있는지 출력
# print("[2-1] a() 함수 내 result 변수의 메모리 주소 : ",a())
# print("[2-2] b() 함수 내 result 변수의 메모리 주소 : ",b())

'''
# 리스트 최고, 최저 점수 함수
#[1] 함수 작성
def max_in_list(lst):
    return max(lst) #max()함수는 리스트 내 요소중 가장 큰 숫자 반환
#[#] 최저 점수 함수 (응용)
def min_in_list(lst):
    return min(lst)

#[2] 영어 점수표 -> list
eng_scores = [10,20,30,40,50,55,60,70,88,99,100]

#[3] 함수 호출 및 결과 출력하기
result = max_in_list(eng_scores)
print(result)
result = min_in_list(eng_scores)
print(result)
'''

# 최저, 최고 점수 동시 출력
'''
def max_min_in_list(lst):
    
    return max(lst), min(lst)

eng_scores =[10,20,30,40,55,60,77,88,99,100]

result = max_min_in_list(eng_scores)
# print(f"최고 점수와 최저 점수 는 {result} 이며 데이터 타입은 {type(result)} 이다")

#[4]: a,b 변수에 각각 최고, 최저 점수 받아 출력하기
a,b = max_min_in_list(eng_scores)

print(f"최고 점수는 {a} 이며 최저 점수는 {b}이다.")
'''

# 오름 차순, 내림 차순 정렬을 sort(), sorted() 함수로 구현
'''
lst = [100,40,70,90,60]
# print(f"원본 정렬 값 : {lst}")
# print('-'*140)
# #lst.sort() -> 오름차순 / lst.sort(reverse=True) -> 내림차순
# lst.sort()
# print(f"sort()함수로 오름차순 : {lst}")
# print('-'*140)
# lst.sort(reverse=True)
# print(f"sort()함수로 내림차순 : {lst}")
# print('-'*140)
asc_ = sorted(lst)
desc_ = sorted(lst, reverse=True)
print(f"원본 : {lst}")
lst.sort()
print(f"[1] sort()함수로 정렬 : {lst}")
print(f"[2] sorted()함수로 정렬 : {asc_} <---->{desc_}")
'''

# 함수 호출 시 입력 파라미터 값을 지정하여 함수를 호출
'''
#[1] 함수 생성
def my_func(id_, name_, strength):
    return id_, name_, strength


#[2] 함수 호출
# result = my_func("HONG","홍길동",1000)
result = my_func(id_="HONG",name_="홍길동",strength=1000)
# print(result,type(result))
a,b,c = my_func(id_="LEE",name_="이순신",strength=10000)

print(f"[2-1]하나의 변수로 리턴값 받아서 출력 : {result} 타입은 {type(result)}")
print(f"하나의 변수의 인덱스를 뽑아보자 1번인덱스 = {result[0]}, 2번인덱스 = {result[1]}, 3번인덱스 = {result[2]}")
print(f"[2-2]여러개 변수로 리턴값 받아서 출력 : {a} , {b} , {c} 각 타입은 {type(a)} {type(b)} {type(c)}")
'''

# 디폴트 파라미터
'''
def calc_tax(price, operator=1.1):
    supply_value = round(price/operator) # --> 공급가
    vat = price - supply_value # ---> 부가세 --> 계산상 편리를 위하여 상품가(소비자가)에서 공급가를 차감하여 계산
    total = round((price/operator) * operator)
    return supply_value, vat, total

# 함수 호출
result = calc_tax(165000)
print(f"공급가 -{result[0]} / 부가세 - {result[1]} / 최종가 - {result[2]}")
'''

# 파라미터 갯수를 알 수 없는 상황에서 함수 호출
# 가변길이 입력 파라미터 --> 함수에서 입력 파라미터를 받을때 * 표시를 해 줌으로써 가변길이라는것을 명시적으로 표시.

# def my_func(*params):
#     n = 0
#     for i in params:
#         n+=i
#     return n

# a = my_func(1,1,1,1)
# print('[2-1] 입력 파라미터 4개의 합 : ',a)
# b = my_func(1,2,3,4,5,6,7,8,9)
# print('[2-2] 입력 파라미터 4개의 합 : {}'.format(b))
# c = my_func(1,2,3,4,5,6,7,8,9,10)
# print(f'[2-3] 입력 파라미터 10개의 합 : {c}')


# 가변길이 입력 파라미터 값을 함수가 받았을 때 그때의 자료형은 무엇인가?
# 가변길이 인수 목록이 전달되면 값이 무엇이고 반복가능한 객체인지
'''
def my_func(*params):
    n = params
    return n, type(n)

a = my_func(1,1,1,1)
print('[2-1] 입력 파라미터 : ',a)
b = my_func(1,2,3,4,5,6,7,8,9)
print('[2-2] 입력 파라미터 : {}'.format(b))

# a = my_func(1,1,1,1)
# print('[2-1] 입력 파라미터 : ',a, type(a))
# b = my_func(1,2,3,4,5,6,7,8,9)
# print('[2-2] 입력 파라미터 : {} type : {}'.format(b,type(b)))
# c = my_func(1,2,3,4,5,6,7,8,9,10)
# print(f'[2-3] 입력 파라미터 : {c} type : {type(c)}')
'''

# 가변길이 입력 파라미터 값들을 함수로 넘겨서 해당 파라미터의 개수와 홀수들의 합을 구하시오
# 리턴은 하나의 값 반환

def my_func(*params):
    cnt = 0
    sum_ = 0
    for i in params:
        cnt +=1
        if i % 2 !=0:
            sum_ +=i

    return cnt, sum_

a, b = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9)
result = my_func(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
print('[2-1] 가변 길이 입력 파라미터의 개수와 홀수 합은 : ',a, ',', b, type(a), type(b)) # -- a,b 변수 각각은 cnt / sum 을 가지고 있으므로 int 타입 --
print('[2-2] result 변수 하나로 리턴되는 결과의 값을 받으면 : ',result, type(result)) # -- result변수는 하나의 변수로 2개의 값을 가지고 있고 tuple타입 --
