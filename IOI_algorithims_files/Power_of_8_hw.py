def powerof8(n):
    if n <= 0:
        return False
    while n % 8 == 0:
        n = n // 8
    
    return n == 1

# Input
n = int(input("Please Enter the number to check for power of 8: "))
if powerof8(n):
    print(f"The number {n} is a power of 8")
else:
    print(f"The number {n} isn't a power of 8")
