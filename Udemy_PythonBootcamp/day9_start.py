'''딕셔너리 설명'''

programming_dictionary = {
    "Bug": "버그설명",
    "Function": "함수설명",
}

# retrieving items from dictionary.
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])


# Adding new items to dictionary.
programming_dictionary["Loop"] = "반복설명"

# Create an empty dictionary 빈 사전 만들기
empty_dictionary = {}
# empty_dictionary[] = ""

# Wipe an existing dictionary 사전 비우기
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in a dictionary 딕셔너리 안 의 값 수정하기
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Loop through a dictionary
# for thing in programming_dictionary:
#     print(thing)

# for i in programming_dictionary:
#     print(i)
#     print(programming_dictionary[i])

# for i,j in programming_dictionary.items():
#     print(j)


################################################################################

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lielle", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Korea": {"cities_visted": ["BUSAN", "KANGWONDO", "TAIAHN"], "total_visits": 10}
}
print(travel_log["Korea"])
#Nesting a Dictionary in a List
print("_"*20)
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lielle", "Dijon"],
        "total_visits":12
    },
    {
        "country": "Korea",
        "cities_visted": ["BUSAN", "KANGWONDO", "TAIAHN"],
        "total_visits": 10

    }
]

# print(travel_log["Korea"])
# for i,j in travel_log.items():
#     print(i)
#     print(j)
