from calendar import month


age = input("너의 나이는? : ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365 # 90살 까지 몇 일 남았는지
weeks_remaining = years_remaining * 52 # 90살까지 몇 주 남앗는지
months_remaining = years_remaining * 12 # 90살까지 몇 개월 남았는지

print(months_remaining,"개월")
print(weeks_remaining,"주")
print(days_remaining,"일")

message = f"너는 {days_remaining} 일, {weeks_remaining} 주, {months_remaining} 월 남았다."

print(message)