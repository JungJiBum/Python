'''딕셔너리 설명'''

programming_dictionary = {
    "Bug":"버그설명",
    "Function":"함수설명",
    }

# retrieving items from dictionary.
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])


# Adding new items to dictionary.
programming_dictionary["Loop"] = "반복설명"

# Create an empty dictionary 빈 사전 만들기
empty_dictionary={}
# empty_dictionary[] = ""

# Wipe an existing dictionary 사전 비우기
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary 딕셔너리 안 의 값 수정하기
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)
