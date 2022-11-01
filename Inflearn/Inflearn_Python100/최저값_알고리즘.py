
#[2] 리스트
english_score = [33,44,55,66,77,88,99,11,22,60]

def min_in_list(lst):
    
    min_number = lst[0]

    for i in lst:
        if i < min_number:
            min_number = i
    return min_number

print(f"내가만든 min함수 : {min_in_list(english_score)}")
print(f"min함수 : {min(english_score)}")