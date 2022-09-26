# 여러 값이 들어있는 리스트에서 최고값 출력하는 함수 구현
# max()함수 사용 금지

#[2] 리스트
english_score = [33,44,55,66,77,88,99,11,22,60]

#[3] 함수 호출 및 결과 출력
# result = max_in_list(english_score)

def max_in_list(lst):

    first_number = 0

    for i in lst:
        if i > first_number:
            first_number = i
    
    
    return first_number

print(f"내가만든 함수 max 값 : {max_in_list(english_score)}")
print(f"max 함수 값 : {max(english_score)}")

