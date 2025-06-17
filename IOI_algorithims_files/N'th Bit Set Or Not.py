def setornot(number,n):
    if number & (1 << (n-1)):
        print("\nSet")
    else:
        print("\nNot Set")

        
number = int(input("Enter number"))
n = int(input("Enter bit number"))
setornot(number,n)