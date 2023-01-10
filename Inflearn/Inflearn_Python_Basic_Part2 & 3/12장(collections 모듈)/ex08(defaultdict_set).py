# 함수를 이용하여 각 알파벳 글자수를 세어서 키로 저장하고 
# 단어를 값으로 저장하는 딕셔너리를 리턴하는 코드

from collections import defaultdict
# words라는 set을 받아 길이를 키로하고 값을 리스트 값으로 하는 딕셔너리
def counterWords(words):
    grouper = defaultdict(set)
    print(grouper)
    for word in words:
        # word의 길이를 구하여 그 길이를 키로 하고 word의 내용을 값으로 하고있다.
        length = len(word)
        grouper[length].add(word)
    return grouper      # defaultdict(<class 'list'>, {2: ['감자', '사과'], 1: ['귤', '배'], 3: ['오징어', '꼼장어'], 4: ['불가사리']})

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("일본")
    set1.add("우즈베키스탄")
    set1.add("사우디아라비아")
    set1.add("러시아")
    dic1 = counterWords(set1)
    print(set1)
    print(f"dic1 = {dic1}")