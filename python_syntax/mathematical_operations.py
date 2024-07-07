# priority of execution of mathematical operations
# PEMDAS :
# Parentheses ()
# Exponents **
# Multiplication *  Division /
# Addition +  Subtraction -

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The formula is BMI = kg / m^2

# 1st input: enter height in meters e.g: 1.65
height = input("What is your height in cm? ")

# 2nd input: enter weight in kilograms e.g: 72
weight = input("What is your weight in kg? ")


new_height = float(height)
new_weight = int(weight)

BMI = (new_weight / (new_height ** 2))
bmi_new = int(BMI)
print(bmi_new)