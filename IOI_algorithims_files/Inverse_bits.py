#Get input
uinpt = int(input("Please enter the number who's bits you would like to reverse"))

#Turn it into binray and reverse
uinptbin = bin(uinpt)[2:]
reversed = uinptbin[::-1]

#Turn it back into an integer
int_uinpt = int(reversed,2)

#Print it
print(int_uinpt)