theNum = int(input("Enter the Number to evaluate:"))
count = 1
sum_of_integer = 0
while count < theNum:
    div = theNum % count
    if div == 0:
        sum_of_integer += count
    count = count + 1

print("The sum of the integers is:", sum_of_integer)
if sum_of_integer == theNum:
    print("The number is a perfect number")
if sum_of_integer > theNum:
    print("The number is an abundant number")
if sum_of_integer < theNum:
    print("The number is a deficient number")
