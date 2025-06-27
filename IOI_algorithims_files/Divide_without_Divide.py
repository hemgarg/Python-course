def divide(ourDividend,ourDivisor):
    
    #Check if divisor is +ve or -ve
    sign = (-1 if((ourDividend < 0) ^
                   (ourDivisor < 0)) else 1);

    ourDividend = abs(ourDividend);
    ourDivisor = abs(ourDivisor);

    quotienNumber = 0
    tempnumber = 0

    for i in range(31,-1,-1):
        if(tempnumber + (ourDivisor << i) <= ourDividend):
            tempnumber += ourDivisor << i
            quotienNumber |= 1 << i
    if sign == -1:
        quotienNumber = -quotienNumber
    return quotienNumber

a = int(input("Enter a for a/b: "))
b = int(input("Enter a for a/b: "))
print("Result of ",a,"/",b,"is",divide(a,b))