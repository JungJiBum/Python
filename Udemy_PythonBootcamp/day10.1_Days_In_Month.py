def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year.")
            else:
                print("Not leap year.")
        else:
            print("Leap Year.")
    else:
        print("Not leap year.")


def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Do Not change any of the code below
year = int(input("Enter a year : "))
month = int(input("Enter a month : "))
days = days_in_month(year,month)
print(days)