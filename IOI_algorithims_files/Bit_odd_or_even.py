def is_evenOdd(n):
    if (n ^ 1 == n + 1):
        return True;
    else:
        return False;

number = int(input("Enter your number"))

if is_evenOdd(number):
    print(number,"Is even")
else:
    print(number,"Is odd")