print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?(S/M/L) :  ")
add_pepperoni = input("Do you want extra pepperoni?(Y/N) : ")
extra_cheese = input("Do you want extra cheese?(Y/N) : ")
'''
Small Pizza : $15
Medium Pizza : $20
Large Pizza : $25

pepperoni for Small Pizza : +$2
pepperoni for Medium Pizza or Large Pizza : +$3

Extra cheese for any size pizza : +$1
'''
bill = 0

if size == "S":
    bill +=15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25
else:
    print("Wrong size")

if add_pepperoni == "Y":
    if size == "S":
        bill+=2
    else:
        bill+=3

if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is ${bill}")