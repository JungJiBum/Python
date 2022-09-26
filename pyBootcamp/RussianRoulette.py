import random
# Angela, Ben, Jenny, Bob, Tom
name_string = input("모두의 이름을 작성하고 구분은 ,로 하라 : ")
names = name_string.split(",")
rand_choice = random.randint(0,len(names -1))

print("{}가 선택 되었다".format(names[rand_choice]))