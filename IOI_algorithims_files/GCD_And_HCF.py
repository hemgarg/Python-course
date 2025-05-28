numberLargest = int(input("Enter Largest Number"))
numbersmallest = int(input("Enter Smallest Number"))

while(numbersmallest):
    numberStore = numbersmallest
    numbersmallest = numberLargest % numbersmallest
    numberLargest = numberStore
print("HCF is :",numberLargest)