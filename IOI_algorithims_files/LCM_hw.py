lowestnumber = int(input("Enter the lower number "))
greaternumber = int(input("Enter the greater number "))

def calculations():
    currentmultiple = greaternumber
    while True:
        if currentmultiple % lowestnumber == 0:
            break
        else:
            currentmultiple += greaternumber  
    print(f"The LCM of {lowestnumber} and {greaternumber} is {currentmultiple}")       

calculations()


