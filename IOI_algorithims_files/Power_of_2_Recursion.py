def powerof2(n):

    if n == 1:
        return True

    if n <= 0 or n % 2 != 0:
        return False

    
    
    return powerof2(n/2)

n = int(input("Please enter a number: "))

if(powerof2(n)):
    print(f" {n} is a power of 2")
else:
    print(f"{n} is not a power of 2")    
