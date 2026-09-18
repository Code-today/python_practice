#calculating BMI of a person
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)

#entering weight and height in pounds and inches
weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))
#converting weight and height to kg and meters
weight_kg = weight_pounds * 0.453592
height_meters = height_inches * 0.0254
bmi = weight_kg / (height_meters ** 2)
print("Your BMI is:", bmi)
