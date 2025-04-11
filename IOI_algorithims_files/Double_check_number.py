num=int(input("Please enter the number to check"))
if num >50:
    print("Number is greater than 50")
    if num % 2 == 1:
        print("And it is Odd")
    if num % 2 == 0:
        print("And it is Even")
else:
    print("Number is less than 50")