# BMI = weight(kg)/height^2(m^2)

height = float(input("키 입력(m) : "))
weight = float(input("무게 입력(kg) : "))

BMI = weight / pow(height,2)
print(f"키는 {height}m, 무게는 {weight}kg 이다. BMI는 {BMI} 이다.")
if BMI < 18.5:
    print("Your bmi is {}, you are underweight.".foramt(BMI))
elif BMI < 25:
    print("Your bmi is {}, you have a normalweight.".foramt(BMI))
elif BMI < 30:
    print("Your bmi is {}, you are overweight.".foramt(BMI))
elif BMI < 35:
    print("Your bmi is {}, you are obese.".foramt(BMI))
else:
    print("Your bmi is {}, you are clinically obese.".foramt(BMI))