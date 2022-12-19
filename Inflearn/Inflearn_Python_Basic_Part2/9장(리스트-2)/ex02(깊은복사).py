# 리스트 복사
# 깊은 복사(deep copy) : 주소값을 공유하는 얕은 복사가 아닌 새로운 리스트 객체를 생성
# 새로운 주소값이 할당되어 원본 리스트 객체에는 전혀 영향을 끼치지 않는다.
# 아래와 같이 3가지 방법으로 만든 리스트가 새로운 객체가 된다.
# 이것이 깊은복사의 진정한 방법이다.

# 첫 번째 방법 : list()메서드를 이용
scores = [10,20,30,40,50]
refer = list(scores)
print(f"score의 주소 값 : {id(scores)}")
print(f"refer의 주소 값 : {id(refer)}")
refer[0] = 100
refer.append(-1000)
refer.insert(2,-123)
print(f"score의 주소 값 : {id(scores)}")
print(f"refer의 주소 값 : {id(refer)}")
print(f"scores의 요소값 : {scores}")
print(f"refer의 요소값 : {refer}")
print("-"*40)

import copy
# 2번째 방법 : copy 모듈에 있는 deepcopy(), copy()를 이용하는 방법
scores_copy=[10,20,30,40,50,-10]
# refer_copy = copy.deepcopy(scores)
refer_copy = copy.copy(scores)
print(f"scores_copy의 주소 값 : {id(scores_copy)}")
print(f"refer_copy의 주소 값 : {id(refer_copy)}")
refer_copy[0] = 100
refer_copy.append(-1000)
refer_copy.insert(2,-123)
print(f"score의 주소 값 : {id(scores_copy)}")
print(f"refer의 주소 값 : {id(refer_copy)}")
print(f"scores의 요소값 : {scores_copy}")
print(f"refer의 요소값 : {refer_copy}")
print("-"*40)

# 3번째 방법 : [:]  인덱스를 이용하여 깊은 복사를 하는 방법
scores_index=[10,20,30,40,50,-10,-111]
refer_index = scores[:]
print(f"scores_index의 주소 값 : {id(scores_index)}")
print(f"refer_index의 주소 값 : {id(refer_index)}")
refer_index[0] = 100
refer_index.append(-1000)
refer_index.insert(2,-123)
print(f"score_index의 주소 값 : {id(scores_index)}")
print(f"refer_index의 주소 값 : {id(refer_index)}")
print(f"scores_index의 요소값 : {scores_index}")
print(f"refer_index의 요소값 : {refer_index}")
print("-"*40)
