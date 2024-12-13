valid = False
while not valid:
    try:
        n = int(input("Please enter a number"))
        #enter a even number
        while n%2==0:

            print("Bye")
        valid = True
    except ValueError:
        print("Invalid")