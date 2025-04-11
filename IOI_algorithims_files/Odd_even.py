number = int(input("Enter number to check "))
print("Number to be checked -",number)

if number == 0:
    print("Even")
elif number % 2 == 1:
    print("Odd")