# 딕셔너리 항목 순회 방법
scores = {"국어": 80, "수학": 95, "영어": 80}

#키값만 출력 루프 반복
# 아래 .keys()를 사용하면 반환값 형태가 dict_keys([]) 타입으로 출력
print(scores.keys(), type(scores.keys()))
# 루프 반복하면 키값만 출력
for sub in scores.keys():
    print(sub, end=" ")
print()
print("-"*40)
# 값만 출력하는 방법
# dict_values([])타입으로 출력
print(scores.values(), type(scores.values()))
for val in scores.values():
    print(val, end=" ")
print()
print("-"*40)

# 키값 동시 출력
# dict_items([(),()])타입
print(scores.items(), type(scores.items()))
for i in scores.items():
    print(i, end=" ")
print()

print("-"*40)
# 딕셔너리 함축(dictionary comprehension)방법은 코드를 간결 -> 가독성 향상
triples = {x: x*x*x for x in range(6)}  # { 출력식(x:x*x*x) 루프}
print(triples, type(triples))
print(triples)

print("-"*40)
# 딕셔너리 정렬(dictionary sort)방법 실습하기
# 파이썬에서 딕셔너리는 근본적으로 요소들이 순서가 없기에 순서대로 저장하지않는다.
dict1 = {"pens":6,"bags":1,"books":5,"bottles":4,"coins":3,"cups":2}
print(dict1)
# 딕셔너리를 리스트로 변환
ls1 = list(dict1)   # 키값만 출력됨
print(ls1)
# 딕셔너리의 키를 정렬하고자 한다면 내장함수 sorted()를 이용
ls2 = sorted(dict1)
print(sorted(dict1))
print(ls2)
print("-"*40)
# 딕셔너리 값을 정렬하고자 한다면 values() 함수와 sorted()를 같이 사용
li3 = sorted(dict1.values())
print(sorted(dict1.values()))
print(li3)
print("-"*40)
# 딕셔너리 값에 따라 키들을 정렬하고 싶은 경우 sorted()에 요소들을 비교할때 사용하는 키를 지정
print(sorted(dict1,key=dict1.__getitem__))
print(dict1.__getitem__)