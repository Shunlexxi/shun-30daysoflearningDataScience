# This program takes Height & Weight, calculate BMI and determines if Obese or Not
# Read and Explore more on Body Mass Index (BMI) @ https://www.calculatorsoup.com/calculators/health/bmi-calculator.php
# https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm

# Underweight :     < 18.5
# Normal weight :   =18.5 to 24.9
# Overweight :      = 25 to 29.9
# Obesity : > 30

height = float(input("Enter Height (in m): "))
weight = float(input("Enter Weight (in kg): "))

#height = 1.7
#weight = 60

#calculating BMI = weight/(height)^2
BMI = weight/pow(height, 2)
print("BMI: ","%.1f" % BMI)

if BMI < 18.5:
    print("You are Underweight!")

elif BMI >= 18.5 and BMI <= 24.9:
    print("You have a Normal weight!") 

elif BMI >= 25 and BMI <= 29.9:
        print("You are Overweight!") 
elif BMI > 30:
    print("You are Obese!") 
