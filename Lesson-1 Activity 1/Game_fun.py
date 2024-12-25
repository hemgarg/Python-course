import random, sys
Playing = True

number = int(random.randint(0, 100))
print("Hello i have made game where you have to guess a number and i will tell you if the number you chose is lower or higher")
while Playing:
    usnumber = int(input("Please now choose a number"))
    if usnumber > number:
        print("Lower!")
    if usnumber < number:
        print("Higher!")
    if usnumber == number:
        print("You got the number! Now exiting...")
        sys.exit()