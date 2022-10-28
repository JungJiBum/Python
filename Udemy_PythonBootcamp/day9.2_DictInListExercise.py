travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]
def add_new_country(country_visited,times_visited,cities_visited):
    # 딕셔너리를 만들어준다.
    new_d = {}
    #딕셔너리 키값에 맞춰 파라미터를 대입
    new_d["country"] = country_visited
    new_d["visits"] = times_visited
    new_d['cities'] = cities_visited
    # 리스트의 추가 함수는 append를 쓴다.
    travel_log.append(new_d)


add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)