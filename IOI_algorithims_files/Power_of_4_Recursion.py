n = int(input("Enter your number: "))

def CheckIfPower(n):
    if (n<=0):
        return False
    if(n==1):
        return True
    if (n%4==0):
        return CheckIfPower(n/4)
    return False

if(CheckIfPower(n)):
    print("Power of 4")
else:
    print("Not power of 4")