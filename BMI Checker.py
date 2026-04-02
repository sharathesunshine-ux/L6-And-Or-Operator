height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))
BMI = weight / (height/100)**2
print("Your BMI is :",BMI)
if BMI <= 18.5:
    print("You are underweighted!")
elif BMI <=25.5:
    print("You are healthy!")
elif BMI <=30.4:
    print("You are overweight!")
elif BMI <=35.6:
    print("You are severely overweight!")
elif BMI <=40.9:
    print("You are obese!")
else:
    print("You are severely obese!")

    