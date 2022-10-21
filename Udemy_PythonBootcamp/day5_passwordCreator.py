# 비밀번호 생성기
# 길이 ? :
# 기호 ? :
# 숫자 ? :
# easy level = 문자,기호,숫자 순 출력
# hard level = 랜덤으로 섞어서 출력
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '&', '*(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many would you like in your password?\n"))
nr_symbols = int(input(f"How many would you like?\n"))
nr_numbers = int(input(f"How many would you like?\n"))

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbol in range(1, nr_symbols+1):
    password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password += random.choice(numbers)

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for symbol in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
# print("password : ", password)
# print("password_list : ", password_list)

passwd = ""
for x in password_list:
    passwd += x
print(f"Your password is {passwd}")
