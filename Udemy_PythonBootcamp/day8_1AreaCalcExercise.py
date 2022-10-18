import math
def print_calc(height,width,cover):
    # number_of_cans = round((height*width) / cover) # 반올림
    area = height * width
    number_of_cans = math.ceil(area/cover)
    print(f"You'll need {number_of_cans} cans of paint")

# Don't change the code below 
test_h = int(input("Height of wall : "))
test_w = int(input("width of wall : "))
coverage=5 #제곱
print_calc(height=test_h, width=test_w, cover=coverage)
