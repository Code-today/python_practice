import random
num = random.randint(0, 1000)
print("Guess My Mpesa Balance Game \n"
      "Range from 0 to Ksh 1000")

guess = int(input("What is your guess:"))
while 0 <= guess <= 1000:
    if guess > num:
        print("That is too high for me")
    elif guess < num:
        print("That is too low for me")
    else:
        print("Correct,my balance is", num)
        break
    guess = int(input("what is your guess:"))
else:
    print("You have Quit,observe rules,my balance is:", num)
