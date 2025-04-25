import random
randomnumber = random.randint(1,100)
print("*****NUMBER GUESSING GAME******")
print("\n There is a number and you have to guess it. I will tell you if it is higher or lower")
print("Lets start!\n")
def get():
    inum = int(input("Enter a number: "))
    if inum > randomnumber:
        print("Too high! Guess lower\n")
        get()
    elif inum < randomnumber:
        print("Too low! Guess higher\n")
        get()
    elif inum == randomnumber:
        print("YOU WON!!! Exiting...")
        quit()
get()